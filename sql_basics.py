import sqlite3
import pandas as pd

# Part 1. Building the database
conn = sqlite3.connect('db/library.db')
cursor = conn.cursor()

# cursor.executescript("""
# DROP TABLE IF EXISTS Book;
# DROP TABLE IF EXISTS Member;
# DROP TABLE IF EXISTS Book_Loan;

# CREATE TABLE IF NOT EXISTS Book(
#     Book_Id INTEGER PRIMARY KEY,
#     Book_Title TEXT,
#     Author TEXT,
#     Category TEXT,
#     Pages INTEGER,
#     Copies_Available INTEGER
# );

# CREATE TABLE IF NOT EXISTS Member(
#     Member_Id INTEGER PRIMARY KEY,
#     Member_name TEXT
# );

# CREATE TABLE IF NOT EXISTS Book_Loan(
#     Loan_Id INTEGER PRIMARY KEY,
#     Book_Id INTEGER,
#     Member_Id INTEGER
# );

# INSERT INTO Book VALUES
#   (1, 'The Secret Garden', 'Frances Hodgson Burnett', 'Fiction', 331, 4),
#   (2, 'Science Experiments', 'Riya Shah', 'Science', 120, 6),
#   (3, 'Space Adventure', 'Arun Mehta', 'Science', 245, 3),
#   (4, 'History of India', 'Neha Rao', 'History', 310, 2),
#   (5, 'The Jungle Book', 'Rudyard Kipling', 'Fiction', 277, 5),
#   (6, 'Maths Made Easy', 'Anita Das', 'Education', 180, 4),
#   (7, 'Stories for Children', 'Meera Singh', 'Fiction', 150, 7),
#   (8, 'Amazing Animals', 'Kabir Khan', 'Science', 210, 3);
  
# INSERT INTO Member VALUES
#   (1, 'Aarav'), (2, 'Diya'), (3, 'Kabir'), (4, 'Meera');
  
# INSERT INTO Book_Loan VALUES
#   (1, 1, 1), (2, 3, 2), (3, 5, 3), (4, 2, 4);
# """)

# conn.commit()

# print("Library Database Ready!")

# Part 2
# tables = pd.read_sql("""
#     SELECT * FROM sqlite_master WHERE type = 'table';
# """, conn)

# print(tables)

# read the full book table and check its shape
books = pd.read_sql("""SELECT * FROM Book""", conn)
print(books)
print("Rows and Columns: ", books.shape)

# fectch only the book id, title and author
book_details = pd.read_sql("""
    SELECT Book_Id, Book_Title, Author FROM Book;
""", conn)
print(book_details)

# fetch book and member