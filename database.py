import sqlite3

class Database:

    def __init__(self):

        self.conn = sqlite3.connect(
            "cafe.db"
        )

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT,
            quantity INTEGER,
            price REAL
        )
        """)

        self.conn.commit()

    def insert_item(
        self,
        item_name,
        quantity,
        price
    ):

        self.cursor.execute("""
        INSERT INTO menu(item_name, quantity, price)
        VALUES (?, ?, ?)
        """, (
            item_name,
            quantity,
            price
        ))

        self.conn.commit()

    def fetch_items(self):

        self.cursor.execute(
            "SELECT * FROM menu"
        )

        return self.cursor.fetchall()

    def delete_item(
        self,
        item_id
    ):

        self.cursor.execute(
            "DELETE FROM menu WHERE id=?",
            (item_id,)
        )

        self.conn.commit()

    def update_item(
        self,
        item_id,
        item_name,
        quantity,
        price
    ):

        self.cursor.execute("""
        UPDATE menu
        SET item_name=?, quantity=?, price=?
        WHERE id=?
        """, (
            item_name,
            quantity,
            price,
            item_id
        ))

        self.conn.commit()