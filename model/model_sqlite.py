# File: model/model_sqlite.py
# Description: the file provides the backend for memoverse storage

"""
The memoverse data is stored in the SQLite database and has the following look:

+-----------+-------------------+-------+--------------+
| Reference | Theme             | Verse | Fums         |
+===========+===================+=======+==============+
| EX.1.22   | State of the Dead | <p... | <script>...  |
+-----------+-------------------+-------+--------------+

This can be created with the following SQL (see bottom of this file):
create table memoverse (reference text, theme text, verse text, fums text);

"""
from .model_abstract import Model
import sqlite3

# Defines the file name for the database
DB_FILE = "entries.db"

class model(Model):
    def __init__(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        # Makes sure the database exists
        try:
            cursor.execute("select count(rowid) from memoverse")
        except sqlite3.OperationalError:
            cursor.execute("create table memoverse (reference text, theme text, verse text, fums text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: reference, theme, verse, and fums
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM memoverse")
        return cursor.fetchall()

    def insert(self, reference, theme, verse, fums):
        """
        Inserts entry into database
		:param reference: String
        :param theme: String
        :param verse: String
        :param fums: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {"reference":reference, "theme":theme, "verse":verse, "fums":fums}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into memoverse (reference, theme, verse, fums) VALUES (:reference, :theme, :verse, :fums)", params)

        connection.commit()
        cursor.close()
        return True
