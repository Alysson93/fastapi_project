import sqlite3

# check_same_thread=False

def get_db_connection():
    conn = sqlite3.connect('src/infra/db/store.db')
    conn.execute('''
       CREATE TABLE IF NOT EXISTS products (
			id TEXT PRIMARY KEY,
			name TEXT NOT NULL,
			price REAL NOT NULL,
			qtd INTEGER NOT NULL,
			created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
			updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
       ) 
    ''')
    conn.row_factory = sqlite3.Row
    return conn