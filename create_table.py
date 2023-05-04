import psycopg2
from psycopg2 import Error
from connection import create_connection
import logging


def create_table(conn, ex_sql):
    cur = conn.cursor()
    cur.execute(ex_sql)
    cur.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sql_execute = """
        DROP TABLE IF EXISTS grades CASCADE;
        DROP TABLE IF EXISTS disciplines CASCADE;
        DROP TABLE IF EXISTS students CASCADE;
        DROP TABLE IF EXISTS teachers CASCADE;
        DROP TABLE IF EXISTS groups CASCADE;

        CREATE TABLE IF NOT EXISTS groups (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE
        );

        CREATE TABLE IF NOT EXISTS teachers (
        id SERIAL PRIMARY KEY,
        fullname TEXT
        );

        CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        fullname TEXT,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
        );

        CREATE TABLE IF NOT EXISTS disciplines (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
        );

        CREATE TABLE IF NOT EXISTS grades (
        id SERIAL PRIMARY KEY,
        student_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE,
        discipline_id INTEGER,
        FOREIGN KEY (discipline_id) REFERENCES disciplines (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE,
        grade INTEGER,
        date_of DATE
        );
    """

    with create_connection() as conn:
        print("Connection successful")
        try:
            create_table(conn, sql_execute)
        except psycopg2.Error as e:
            logging.error(e)