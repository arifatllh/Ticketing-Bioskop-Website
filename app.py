from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, Response
import sqlite3
import random
import json
import csv
import io
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'super_secret_cinema_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def get_db_connection():
    conn = sqlite3.connect('cinema.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    hero_events = [
        {"title": "Promo Akhir Pekan", "desc": "Diskon 20% untuk semua film IMAX!", "img": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=1200&h=400&fit=crop"},
        {"title": "Penayangan Perdana", "desc": "Saksikan film blockbuster terbaru minggu ini.", "img": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=1200&h=400&fit=crop"},
        {"title": "Nonton Bareng Aktor", "desc": "Meet and Greet dengan pemeran utama.", "img": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=1200&h=400&fit=crop"}
    ]
    
    unique_showtimes = set()
    processed_movies = []
    
    # Pre-calculate avg_rating for all movies
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    
    for m in movies:
        m_dict = dict(m)
        m_dict['cinemas'] = json.loads(m_dict['cinemas'])
        m_dict['showtimes'] = json.loads(m_dict['showtimes'])
        
        reviews = conn.execute('SELECT rating FROM reviews WHERE movie_id = ?', (m_dict['id'],)).fetchall()
        m_dict['avg_rating'] = sum(r['rating'] for r in reviews) / len(reviews) if reviews else 0
        
        processed_movies.append(m_dict)
        for st in m_dict['showtimes']:
            unique_showtimes.add(st)
            
    conn.close()
        
    all_showtimes = sorted(list(unique_showtimes))
        
    movies_popular = [m for m in processed_movies if m['category'] == 'popular']
    movies_indo = [m for m in processed_movies if m['category'] == 'indo']
    movies_intl = [m for m in processed_movies if m['category'] == 'popular']
    
    return render_template('home.html', hero_events=hero_events, movies_popular=movies_popular, movies_indo=movies_indo, movies_intl=movies_intl, all_showtimes=all_showtimes, all_movies=processed_movies)

@app.route('/category/<string:cat>')
def category(cat):
    conn = get_db_connection()
    db_cat = 'popular' if cat == 'intl' else cat
    
    movies = conn.execute('SELECT * FROM movies WHERE category = ?', (db_cat,)).fetchall()
    
    processed_movies = []
    for m in movies:
        m_dict = dict(m)
        m_dict['cinemas'] = json.loads(m_dict['cinemas'])
        m_dict['showtimes'] = json.loads(m_dict['showtimes'])
        
        reviews = conn.execute('SELECT rating FROM reviews WHERE movie_id = ?', (m_dict['id'],)).fetchall()
        m_dict['avg_rating'] = sum(r['rating'] for r in reviews) / len(reviews) if reviews else 0
        
        processed_movies.append(m_dict)
        
    conn.close()
        
    cat_titles = {
        'popular': 'Film Paling Populer',
        'indo': 'Film Indonesia',
        'intl': 'Film Internasional'
    }
    title = cat_titles.get(cat, 'Kategori Film')
    
    return render_template('category.html', movies=processed_movies, title=title)

@app.route('/api/search')
def api_search():
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify([])
        
    conn = get_db_connection()
    movies = conn.execute("SELECT id, title, genre, img FROM movies WHERE title LIKE ?", ('%' + query + '%',)).fetchall()
    conn.close()
    
    results = [dict(m) for m in movies]
    return jsonify(results)

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    conn = get_db_connection()
    movie = conn.execute('SELECT * FROM movies WHERE id = ?', (movie_id,)).fetchone()
    
    if not movie:
        conn.close()
        return "Film tidak ditemukan", 404
        
    m_dict = dict(movie)
    m_dict['cinemas'] = json.loads(m_dict['cinemas'])
    m_dict['showtimes'] = json.loads(m_dict['showtimes'])
    
    reviews = conn.execute('''
        SELECT r.*, u.name as user_name 
        FROM reviews r 
        JOIN users u ON r.user_id = u.id 
        WHERE r.movie_id = ? 
        ORDER BY r.date DESC
    ''', (movie_id,)).fetchall()
    
    avg_rating = 0
    if reviews:
        avg_rating = sum(r['rating'] for r in reviews) / len(reviews)
        
    can_review = False
    if session.get('user_id'):
        user_order = conn.execute("SELECT id FROM orders WHERE user_id = ? AND movie_id = ? AND status = 'Confirmed'", (session['user_id'], movie_id)).fetchone()
        if user_order:
            can_review = True
            
    conn.close()
    return render_template('movie.html', movie=m_dict, reviews=reviews, avg_rating=avg_rating, can_review=can_review)

@app.route('/review/<int:movie_id>', methods=['POST'])
def add_review(movie_id):
    if not session.get('user_id'):
        return redirect(url_for('login'))
        
    rating = int(request.form.get('rating'))
    review_text = request.form.get('review_text')
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conn = get_db_connection()
    conn.execute('INSERT INTO reviews (user_id, movie_id, rating, review_text, date) VALUES (?, ?, ?, ?, ?)',
                 (session['user_id'], movie_id, rating, review_text, date_now))
    conn.commit()
    conn.close()
    flash('Review berhasil ditambahkan!', 'success')
    return redirect(url_for('movie_detail', movie_id=movie_id))

@app.route('/book/<int:movie_id>', methods=['GET'])
def book(movie_id):
    if not session.get('user_id'):
        flash('Silakan login terlebih dahulu untuk memesan tiket.', 'error')
        return redirect(url_for('login', next=request.url))
        
    cinema_selected = request.args.get('cinema')
    showtime_selected = request.args.get('showtime')
    
    if not cinema_selected or not showtime_selected:
        flash('Silakan pilih bioskop dan jam tayang terlebih dahulu.', 'error')
        return redirect(url_for('movie_detail', movie_id=movie_id))
        
    conn = get_db_connection()
    movie = conn.execute('SELECT * FROM movies WHERE id = ?', (movie_id,)).fetchone()
    
    if not movie:
        conn.close()
        return "Film tidak ditemukan", 404
        
    m_dict = dict(movie)
    m_dict['cinemas'] = json.loads(m_dict['cinemas'])
    m_dict['showtimes'] = json.loads(m_dict['showtimes'])
    
    seats_db = conn.execute('SELECT seat_id FROM booked_seats WHERE movie_id = ? AND cinema = ? AND showtime = ?', (movie_id, cinema_selected, showtime_selected)).fetchall()
    booked_seats = [s['seat_id'] for s in seats_db]
    conn.close()
    
    # Cinema Grid Capacity Logic
    # XXI = 6 rows (A-F), 20 cols = 120 seats
    # CGV = 10 rows (A-J), 10 cols = 100 seats
    # Default = 6 rows (A-F), 10 cols = 60 seats
    cinema_upper = cinema_selected.upper()
    if 'XXI' in cinema_upper:
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        cols = 12
    elif 'CGV' in cinema_upper:
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        cols = 10
    else:
        rows = ['A', 'B', 'C', 'D', 'E', 'F']
        cols = 10
        
    # For dummy visual if empty, just prepopulate a few matching the row bounds
    if not booked_seats:
        booked_seats = ['A1', 'B2', 'C3', 'D4']
        
    return render_template('book.html', movie=m_dict, cinema_selected=cinema_selected, showtime_selected=showtime_selected, booked_seats=booked_seats, rows=rows, cols=cols)

@app.route('/ticket', methods=['POST'])
def generate_ticket():
    movie_id = int(request.form.get('movie_id'))
    buyer_name = request.form.get('buyer_name')
    seats_str = request.form.get('selected_seats')
    payment_method = request.form.get('payment_method')
    cinema = request.form.get('cinema')
    showtime = request.form.get('showtime')
    user_id = session.get('user_id', None)
    
    conn = get_db_connection()
    movie = conn.execute('SELECT * FROM movies WHERE id = ?', (movie_id,)).fetchone()
    m_dict = dict(movie) if movie else {}
    
    seats_list = [s.strip() for s in seats_str.split(',')]
    booking_id = f"TIX-{random.randint(100000, 999999)}"
    total_price = len(seats_list) * 50000
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conn.execute('''
        INSERT INTO orders (booking_id, user_id, movie_id, buyer_name, cinema, showtime, seats, payment_method, total, date, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'Pending')
    ''', (booking_id, user_id, movie_id, buyer_name, cinema, showtime, seats_str, payment_method, total_price, date_now))
    
    for seat in seats_list:
        conn.execute('INSERT INTO booked_seats (movie_id, cinema, showtime, seat_id) VALUES (?, ?, ?, ?)', (movie_id, cinema, showtime, seat))
        
    conn.commit()
    conn.close()
    
    ticket_data = {
        "booking_id": booking_id,
        "movie": m_dict,
        "buyer_name": buyer_name,
        "seats": seats_str,
        "payment_method": payment_method,
        "cinema": cinema,
        "showtime": showtime,
        "total": total_price,
        "date": date_now,
        "status": "Pending"
    }
    
    return render_template('ticket.html', ticket=ticket_data)

@app.route('/history')
def order_history():
    if not session.get('user_id'):
        flash('Silakan login untuk melihat riwayat.', 'error')
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    orders = conn.execute('''
        SELECT o.*, m.title as movie_title, m.img as movie_img 
        FROM orders o 
        JOIN movies m ON o.movie_id = m.id 
        WHERE o.user_id = ? 
        ORDER BY o.id DESC
    ''', (session.get('user_id'),)).fetchall()
    conn.close()
    
    return render_template('history.html', orders=orders)

@app.route('/ticket/<string:booking_id>')
def view_ticket(booking_id):
    if not session.get('user_id'):
        flash('Silakan login untuk melihat tiket.', 'error')
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    order = conn.execute('''
        SELECT o.*, m.title as movie_title, m.img as movie_img 
        FROM orders o 
        JOIN movies m ON o.movie_id = m.id 
        WHERE o.booking_id = ? AND o.user_id = ?
    ''', (booking_id, session.get('user_id'))).fetchone()
    conn.close()
    
    if not order:
        flash('Tiket tidak ditemukan.', 'error')
        return redirect(url_for('order_history'))
        
    m_dict = {
        'title': order['movie_title'],
        'img': order['movie_img']
    }
    
    ticket_data = {
        "booking_id": order['booking_id'],
        "movie": m_dict,
        "buyer_name": order['buyer_name'],
        "seats": order['seats'],
        "payment_method": order['payment_method'],
        "cinema": order['cinema'],
        "showtime": order['showtime'],
        "total": order['total'],
        "date": order['date'],
        "status": order['status']
    }
    
    return render_template('ticket.html', ticket=ticket_data)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        hashed_pw = generate_password_hash(password)
        
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)',
                         (name, email, hashed_pw, 'customer'))
            conn.commit()
            flash('Pendaftaran berhasil! Silakan login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email sudah terdaftar!', 'error')
        finally:
            conn.close()
            
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        next_url = request.form.get('next')
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ? AND role = ?', (email, role)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_role'] = user['role']
            flash('Login berhasil!', 'success')
            
            if role == 'admin':
                return redirect(url_for('admin_dashboard'))
            if next_url:
                return redirect(next_url)
            return redirect(url_for('home'))
        else:
            flash('Email atau password salah!', 'error')
            
    return render_template('login.html', next_url=request.args.get('next', ''))

@app.route('/logout')
def logout():
    session.clear()
    flash('Anda telah logout.', 'success')
    return redirect(url_for('home'))

# --- ADMIN ROUTES ---
@app.route('/admin')
def admin_dashboard():
    if session.get('user_role') != 'admin':
        flash('Akses ditolak!', 'error')
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    
    orders_db = conn.execute('''
        SELECT o.*, m.title as movie_title 
        FROM orders o 
        JOIN movies m ON o.movie_id = m.id 
        ORDER BY o.id DESC
    ''').fetchall()
    
    total_revenue = 0
    total_tickets = 0
    daily_revenue = {}
    top_movies_dict = {}
    
    for o in orders_db:
        if dict(o).get('status', 'Pending') == 'Confirmed':
            total_revenue += o['total']
            num_tickets = len(o['seats'].split(','))
            total_tickets += num_tickets
            
            date_str = o['date'].split(' ')[0]
            daily_revenue[date_str] = daily_revenue.get(date_str, 0) + o['total']
            
            m_title = o['movie_title']
            top_movies_dict[m_title] = top_movies_dict.get(m_title, 0) + num_tickets
            
    daily_revenue_list = [{"date": k, "revenue": v} for k, v in sorted(daily_revenue.items(), reverse=True)]
    top_movies_list = [{"title": k, "tickets": v} for k, v in sorted(top_movies_dict.items(), key=lambda item: item[1], reverse=True)]
    
    movie_stats = []
    for m in movies:
        m_dict = dict(m)
        cinemas = json.loads(m_dict['cinemas'])
        showtimes = json.loads(m_dict['showtimes'])
        m_dict['cinemas'] = cinemas
        m_dict['showtimes'] = showtimes
        
        total_seats_all = 0
        booked_all = 0
        
        # Breakdown by cinema and showtime
        breakdown = []
        
        for c in cinemas:
            c_upper = c.upper()
            if 'XXI' in c_upper: cap = 120
            elif 'CGV' in c_upper: cap = 100
            else: cap = 60
            
            for st in showtimes:
                total_seats_all += cap
                # count seats for this specific cinema+showtime combo
                count = conn.execute('SELECT COUNT(*) as c FROM booked_seats WHERE movie_id = ? AND cinema = ? AND showtime = ?', (m_dict['id'], c, st)).fetchone()['c']
                
                # Default visual offset if empty
                if count == 0:
                    count = 4
                    
                booked_all += count
                
                breakdown.append({
                    "cinema": c,
                    "showtime": st,
                    "capacity": cap,
                    "booked": count,
                    "available": cap - count
                })
                
        available_all = total_seats_all - booked_all
        m_dict['breakdown'] = breakdown
        movie_stats.append({**m_dict, "total_seats": total_seats_all, "booked": booked_all, "available": available_all})
        
    conn.close()
        
    return render_template('admin.html', movies=movie_stats, orders=orders_db, total_revenue=total_revenue, total_tickets=total_tickets, daily_revenue=daily_revenue_list, top_movies=top_movies_list)

@app.route('/admin/export/report')
def admin_export_report():
    if session.get('user_role') != 'admin':
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    orders_db = conn.execute('''
        SELECT o.*, m.title as movie_title 
        FROM orders o 
        JOIN movies m ON o.movie_id = m.id 
        WHERE o.status = 'Confirmed'
        ORDER BY o.id DESC
    ''').fetchall()
    conn.close()
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Booking ID', 'Tanggal', 'Pemesan', 'Film', 'Bioskop', 'Jadwal', 'Kursi', 'Total Pendapatan'])
    
    for o in orders_db:
        writer.writerow([
            o['booking_id'],
            o['date'],
            o['buyer_name'],
            o['movie_title'],
            o['cinema'],
            o['showtime'],
            o['seats'],
            o['total']
        ])
        
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=Laporan_Penjualan_TixNow.csv"}
    )

@app.route('/admin/order/confirm/<int:order_id>', methods=['POST'])
def admin_confirm_order(order_id):
    if session.get('user_role') != 'admin':
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    conn.execute("UPDATE orders SET status = 'Confirmed' WHERE id = ?", (order_id,))
    conn.commit()
    conn.close()
    flash('Pesanan berhasil divalidasi.', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/movie/add', methods=['POST'])
def admin_add_movie():
    if session.get('user_role') != 'admin':
        return redirect(url_for('login'))
        
    cinemas_list = [c.strip() for c in request.form['cinemas'].split(',')]
    showtimes_list = [s.strip() for s in request.form['showtimes'].split(',')]
    
    img_url = "https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=400&h=600&fit=crop"
    if 'img' in request.files:
        file = request.files['img']
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_url = url_for('static', filename='uploads/' + filename)
    
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO movies (title, rating, duration, genre, synopsis, cinemas, showtimes, img, category)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        request.form['title'],
        request.form['rating'],
        request.form['duration'],
        request.form['genre'],
        request.form['synopsis'],
        json.dumps(cinemas_list),
        json.dumps(showtimes_list),
        img_url, 
        "popular"
    ))
    conn.commit()
    conn.close()
    
    flash('Film berhasil ditambahkan.', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/movie/edit/<int:movie_id>', methods=['POST'])
def admin_edit_movie(movie_id):
    if session.get('user_role') != 'admin':
        return redirect(url_for('login'))
        
    cinemas_list = [c.strip() for c in request.form['cinemas'].split(',')]
    showtimes_list = [s.strip() for s in request.form['showtimes'].split(',')]
    
    conn = get_db_connection()
    movie = conn.execute('SELECT img FROM movies WHERE id = ?', (movie_id,)).fetchone()
    img_url = movie['img']
    
    if 'img' in request.files:
        file = request.files['img']
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_url = url_for('static', filename='uploads/' + filename)
            
    conn.execute('''
        UPDATE movies 
        SET title=?, rating=?, duration=?, genre=?, synopsis=?, cinemas=?, showtimes=?, img=?
        WHERE id=?
    ''', (
        request.form['title'],
        request.form['rating'],
        request.form['duration'],
        request.form['genre'],
        request.form['synopsis'],
        json.dumps(cinemas_list),
        json.dumps(showtimes_list),
        img_url,
        movie_id
    ))
    conn.commit()
    conn.close()
    flash('Film berhasil diperbarui.', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/movie/delete/<int:movie_id>', methods=['POST'])
def admin_delete_movie(movie_id):
    if session.get('user_role') != 'admin':
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    conn.execute('DELETE FROM movies WHERE id = ?', (movie_id,))
    conn.execute('DELETE FROM booked_seats WHERE movie_id = ?', (movie_id,))
    conn.commit()
    conn.close()
    
    flash('Film berhasil dihapus.', 'success')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
