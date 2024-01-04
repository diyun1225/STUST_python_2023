import sqlite3

# 建立或連接到資料庫
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# 創建書籍資訊表格
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name TEXT,
        book_id TEXT UNIQUE,
        year INTEGER,
        author TEXT,
        lend INTEGER,
        lend_time TEXT
    )
''')


# 插入五本初始書籍資料
initial_books = [
    ("Python Programming", "P001", 2022, "John Doe"),
    ("Data Science Basics", "P002", 2023, "Jane Smith"),
    ("JavaScript Fundamentals", "P003", 2021, "Alex Johnson"),
    ("Machine Learning Essentials", "P004", 2022, "Emily Brown"),
    ("Web Development Guide", "P005", 2020, "Michael Wilson")
]

for book in initial_books:
    book_id = book[1]
    cursor.execute('SELECT * FROM books WHERE book_id = ?', (book_id,))
    existing_book = cursor.fetchone()
    if not existing_book:
        cursor.execute('''
            INSERT INTO books (name, book_id, year, author, lend, lend_time)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (*book, 0, None))

conn.commit()

class Book:
    def __init__(self, name,book_id, author, year, is_lend=False, lend_time=None):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.year = year
        self.is_lent = is_lend
        self.lend_time = lend_time

    def borrow_book(self):
        if not self.is_lent:
            self.is_lent = True
            # 借書時間的處理方式可以在這裡加入，例如日期時間資訊
            self.lend_time = "借書時間"
            print(f"成功借閱書籍 '{self.name}'")
        else:
            print(f"抱歉，書籍 '{self.name}' 已被借出")

    def load_from_database(self):
        cursor = self.connection.cursor()
 
        # Load student information
        cursor.execute("SELECT * FROM students WHERE book_id=?", (self.book_id,))
        book_data = cursor.fetchone()
        if book_data:
            self.name = book_data[1]
 
        # Load courses information
        cursor.execute("SELECT * FROM courses WHERE student_id=?", (self.student_id,))
        books_data = cursor.fetchall()
        for books2_data in books_data:
            name = books2_data[1]
            id = books2_data[2]
            year = books2_data[3]
            author = books2_data[4]
            lend = books2_data[5]
            lend_time = books2_data[6]
            self.add_course(name, id, year,author,lend,lend_time)

    
    def return_book(self):
        if self.is_lent:
            self.is_lent = False
            self.lend_time = None
            print(f"成功歸還書籍 '{self.name}'")
        else:
            print(f"這本書 '{self.name}' 不在借閱狀態")

if __name__ == '__main__':
    print("ok")
    book_from_db = Book.get_book_by_book_id(book,"P001")
    if book_from_db:
        print(f"取得書籍 '{book_from_db.name}' 成功")
        book_from_db.borrow_book()
        book_from_db.return_book()
else:
    print("書籍不存在")