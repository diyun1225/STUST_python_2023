import sqlite3

# 建立或連接到資料庫
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# 創建書籍資訊表格
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id TEXT PRIMARY KEY,
        name TEXT,
        id TEXT,
        year TEXT,
        author TEXT,
        lend TEXT,
        lend_time TEXT
    )
''')
conn.commit()
class Book:
    def __init__(self, name, id, year, author, lend=False, lend_time=None):
        self.name = name
        self.id = id
        self.year = year
        self.author = author
        self.lend = lend
        self.lend_time = lend_time

        self.save_to_db()
    

    def borrow_book(self):
        if not self.lend:
            self.lend = True
            # 在這裡可以添加借出時間的處理
            self.lend_time = "借出時間"  # 這邊可以加入借出時間的處理方式，比如日期時間資訊
            print(f"成功借閱書籍 '{self.name}'")
        else:
            print(f"抱歉，書籍 '{self.name}' 已被借出")

    def return_book(self):
        if self.lend:
            self.lend = False
            self.lend_time = None
            print(f"成功歸還書籍 '{self.name}'")
        else:
            print(f"這本書 '{self.name}' 不在借閱狀態")
    def save_to_db(self):
        # 將書籍資訊插入到資料庫
        cursor.execute('''
            INSERT INTO books (name, id, year, author, lend, lend_time)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.name, self.id, self.year, self.author, self.lend, self.lend_time))
        conn.commit()
if __name__ == '__main__':
    my_book = Book("Python基礎入門", "P001", "2022", "某某某","否","未借出")
    my_book.borrow_book()