from datetime import date
import sqlite3


con = sqlite3.connect("data.db", check_same_thread=False)
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS sounds_data (
id INTEGER PRIMARY KEY UNIQUE NOT NULL,
filename STR,
format STR,
date STR
)
""")


def add_sound(filename, extension):
    dates = date.today().strftime("%d %m")
    cur.execute("""
    INSERT INTO sounds_data (
    filename,
    format,
    date) VALUES (?, ?, ?)
    """, (filename, extension, dates))
    con.commit()
    return cur.lastrowid


def del_sound_id(sound_id):
    cur.execute("""
    DELETE FROM sounds_data WHERE id = ?
    """, (sound_id,))
    con.commit()


def del_sound_date(sound_date):
    cur.execute("""
    DELETE FROM sounds_data WHERE date = ?
    """, (sound_date,))
    con.commit()


def get_info(sound_id):
    cur.execute("""
    SELECT * FROM sounds_data WHERE id = ?
    """, (sound_id,))
    return cur.fetchone()


def get_all():
    cur.execute("""
    SELECT * FROM sounds_data
    """)
    return cur.fetchall()
