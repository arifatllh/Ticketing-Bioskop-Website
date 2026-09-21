import sqlite3
import random
from datetime import datetime, timedelta

def add_dummy_reviews():
    conn = sqlite3.connect('cinema.db')
    c = conn.cursor()
    
    # Check if reviews already exist
    c.execute('SELECT COUNT(*) FROM reviews')
    if c.fetchone()[0] > 0:
        print("Reviews already exist.")
        conn.close()
        return

    movies = c.execute('SELECT id FROM movies').fetchall()
    
    # Get a dummy user (admin) or create a dummy user
    c.execute('SELECT id FROM users WHERE role="admin" LIMIT 1')
    admin_user = c.fetchone()
    user_id = admin_user[0] if admin_user else 1

    review_texts = [
        "Film yang sangat bagus, jalan ceritanya menarik!",
        "Visualnya luar biasa, tapi ceritanya agak lambat.",
        "Sangat direkomendasikan untuk ditonton bersama keluarga.",
        "Ekspektasi saya terlalu tinggi, ternyata biasa saja.",
        "Acting pemeran utamanya sangat memukau!"
    ]

    date_now = datetime.now()

    for m in movies:
        movie_id = m[0]
        # Add 2-4 random reviews per movie
        num_reviews = random.randint(2, 4)
        for i in range(num_reviews):
            rating = random.randint(3, 5) # Let's give them good ratings
            review_text = random.choice(review_texts)
            date_str = (date_now - timedelta(days=random.randint(0, 10))).strftime("%Y-%m-%d %H:%M:%S")
            c.execute('INSERT INTO reviews (user_id, movie_id, rating, review_text, date) VALUES (?, ?, ?, ?, ?)',
                     (user_id, movie_id, rating, review_text, date_str))

    conn.commit()
    conn.close()
    print("Dummy reviews added successfully.")

if __name__ == '__main__':
    add_dummy_reviews()
