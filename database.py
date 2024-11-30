import sqlite3

DB_PATH = "high_scores.db"

def initialize_database():
    """Creates the database and table if they do not exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS high_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            highest_score INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def get_highest_score(player_name="Player 1"):
    """Fetch the highest score for the given player."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT highest_score FROM high_scores WHERE player_name = ?", (player_name,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else 0

def update_highest_score(new_score, player_name="Player 1"):
    """Update the highest score if the new score is higher."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT highest_score FROM high_scores WHERE player_name = ?", (player_name,))
    row = cursor.fetchone()

    if row:
        if new_score > row[0]:
            cursor.execute("UPDATE high_scores SET highest_score = ? WHERE player_name = ?", (new_score, player_name))
    else:
        cursor.execute("INSERT INTO high_scores (player_name, highest_score) VALUES (?, ?)", (player_name, new_score))

    conn.commit()
    conn.close()