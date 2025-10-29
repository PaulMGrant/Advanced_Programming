#Title: Mrs. Higgins' Rare Books
#Author: Paul Grant
#Date: 09/10/2025
#Description: SQLite Assignment

import sqlite3


def create_connection(db_name):
    #Create and return a database connection.
    return sqlite3.connect(db_name)


def create_table(conn):
    #Create the Book table if it doesn't already exist.
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Book (
                BookID INTEGER PRIMARY KEY,
                Title TEXT NOT NULL,
                AuthorSurname TEXT NOT NULL,
                YearPublished INTEGER NOT NULL
            );
            """
        )


def insert_books(conn, books):
    #Insert multiple book records using parameterised queries.
    with conn:
        conn.executemany(
            """
            INSERT INTO Book (Title, AuthorSurname, YearPublished)
            VALUES (?, ?, ?);
            """,
            books,
        )


def update_year_published(conn, book_id, new_year):
    #Update the YearPublished for a book by BookID.
    with conn:
        conn.execute(
            """
            UPDATE Book
            SET YearPublished = ?
            WHERE BookID = ?;
            """,
            (new_year, book_id),
        )


def fetch_all_books(conn):
    #Retrieve and display all book records.
    cursor = conn.execute("SELECT * FROM Book;")
    books = cursor.fetchall()

    print("\nAll Books:")
    print("-" * 50)
    for book in books:
        print(
            f"BookID: {book[0]:<3} | "
            f"Title: {book[1]:<25} | "
            f"Author: {book[2]:<15} | "
            f"Year: {book[3]}"
        )


def fetch_books_before_2000(conn):
    #Retrieve and display books published before the year 2000.
    cursor = conn.execute(
        "SELECT * FROM Book WHERE YearPublished < 2000;"
    )
    books = cursor.fetchall()

    print("\nBooks Published Before 2000:")
    print("-" * 50)
    for book in books:
        print(
            f"BookID: {book[0]:<3} | "
            f"Title: {book[1]:<25} | "
            f"Author: {book[2]:<15} | "
            f"Year: {book[3]}"
        )


def main():
    #Main program execution.
    db_name = "catalogue.db"
    conn = create_connection(db_name)

    create_table(conn)

    # Sample book data (Title, AuthorSurname, YearPublished)
    books = [
        ("To Kill a Mockingbird", "Lee", 1960),
        ("1984", "Orwell", 1949),
        ("The Great Gatsby", "Fitzgerald", 1925),
        ("The Road", "McCarthy", 2006),
    ]

    insert_books(conn, books)

    # Update one book’s publication year using its BookID
    update_year_published(conn, 4, 2007)

    # Commit changes and close connection
    conn.commit()

    # Reopen connection for retrieval
    conn = create_connection(db_name)
    fetch_all_books(conn)
    fetch_books_before_2000(conn)

    conn.close()


if __name__ == "__main__":
    main()
