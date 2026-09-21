import sqlite3
import json
from werkzeug.security import generate_password_hash

def init_db():
    conn = sqlite3.connect('cinema.db')
    c = conn.cursor()

    # Drop existing tables to recreate schema cleanly
    c.execute('DROP TABLE IF EXISTS users')
    c.execute('DROP TABLE IF EXISTS movies')
    c.execute('DROP TABLE IF EXISTS orders')
    c.execute('DROP TABLE IF EXISTS booked_seats')

    # Create users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    
    # Create movies table
    c.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            rating TEXT NOT NULL,
            duration TEXT NOT NULL,
            genre TEXT NOT NULL,
            synopsis TEXT NOT NULL,
            cinemas TEXT NOT NULL, -- Stored as JSON string
            showtimes TEXT NOT NULL, -- Stored as JSON string
            img TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')

    # Create orders table
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            booking_id TEXT NOT NULL,
            user_id INTEGER,
            movie_id INTEGER,
            buyer_name TEXT NOT NULL,
            cinema TEXT NOT NULL,
            showtime TEXT NOT NULL,
            seats TEXT NOT NULL,
            payment_method TEXT NOT NULL,
            total INTEGER NOT NULL,
            date TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    ''')

    # Create booked_seats table
    c.execute('''
        CREATE TABLE IF NOT EXISTS booked_seats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER NOT NULL,
            cinema TEXT NOT NULL,
            showtime TEXT NOT NULL,
            seat_id TEXT NOT NULL
        )
    ''')

    # Create reviews table
    c.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            movie_id INTEGER NOT NULL,
            rating INTEGER NOT NULL,
            review_text TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')

    movies_data = [
        ("Avengers: Secret Wars", "R", "145 Menit", "Action, Sci-Fi", "Pahlawan super dari berbagai universe berkumpul untuk menghadapi ancaman multiverse terbesar.", ["XXI Senayan", "CGV Grand Indonesia"], ["10:00", "13:30", "17:00", "20:30"], "https://images.unsplash.com/photo-1626814026160-2237a95fc5a0?q=80&w=400&h=600&fit=crop", "popular"),
        ("Joker: Folie à Deux", "D", "138 Menit", "Crime, Drama", "Arthur Fleck bertemu cinta sejatinya, Harley Quinn, saat berada di Rumah Sakit Negara Arkham.", ["XXI Plaza Indonesia", "Cinepolis Senayan"], ["11:00", "14:15", "18:00", "21:00"], "https://images.unsplash.com/photo-1611250282006-4484dd3fba6b?q=80&w=400&h=600&fit=crop", "popular"),
        ("The Batman Part II", "R", "160 Menit", "Action, Crime", "Batman kembali beraksi di kota Gotham yang semakin dikuasai oleh dunia bawah tanah.", ["CGV Pacific Place", "XXI Kota Kasablanka"], ["09:45", "13:00", "16:45", "20:15"], "https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?q=80&w=400&h=600&fit=crop", "popular"),
        ("Spider-Man 4", "SU", "130 Menit", "Action, Adventure", "Peter Parker memulai kehidupan barunya tanpa identitas superhero yang diketahui orang.", ["XXI Kelapa Gading", "CGV Central Park"], ["10:30", "14:00", "16:30", "19:00"], "https://images.unsplash.com/photo-1635805737707-575885ab0820?q=80&w=400&h=600&fit=crop", "popular"),
        ("Dune: Part Three", "R", "170 Menit", "Sci-Fi, Adventure", "Kelanjutan epik dari peperangan di planet gurun Arrakis.", ["IMAX Kelapa Gading", "XXI Gandaria"], ["10:00", "15:00", "19:30"], "https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=400&h=600&fit=crop", "popular"),
        ("Pengabdi Setan 3", "D", "120 Menit", "Horror", "Keluarga Rini kembali dihantui oleh kutukan masa lalu yang belum selesai.", ["XXI Blok M", "CGV FX Sudirman"], ["13:00", "15:45", "18:30", "21:15"], "https://images.unsplash.com/photo-1505635552518-3448ff116af3?q=80&w=400&h=600&fit=crop", "indo"),
        ("Laskar Pelangi Reborn", "SU", "115 Menit", "Drama", "Kisah inspiratif anak-anak Belitung meraih mimpi mereka di sekolah yang penuh keterbatasan.", ["XXI Senayan", "Cinepolis Pejaten"], ["09:00", "11:30", "14:00", "16:30"], "https://images.unsplash.com/photo-1478720568477-152d9b164e26?q=80&w=400&h=600&fit=crop", "indo"),
        ("Gundala 2", "R", "135 Menit", "Action, Superhero", "Sancaka harus menghadapi ancaman dari musuh baru yang lebih mematikan.", ["XXI Epicentrum", "CGV Slipi"], ["10:15", "13:45", "17:15", "20:45"], "https://images.unsplash.com/photo-1518676590629-3dcbd9c5a5c9?q=80&w=400&h=600&fit=crop", "indo")
    ]

    for m in movies_data:
        c.execute('''
            INSERT INTO movies (title, rating, duration, genre, synopsis, cinemas, showtimes, img, category)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (m[0], m[1], m[2], m[3], m[4], json.dumps(m[5]), json.dumps(m[6]), m[7], m[8]))

    # Add default admin
    hashed_pw = generate_password_hash('admin123')
    c.execute('INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)',
              ('Admin', 'admin@tixnow.com', hashed_pw, 'admin'))
              
    conn.commit()
    conn.close()
    print("Database initialized successfully with new schema!")

if __name__ == '__main__':
    init_db()
