# File: model_abstract.py
# Description: the file provides a template class for the database operations

class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, reference, theme, verse, fums):
        """
        Inserts entry into database
        :param reference: String
        :param theme: String
        :param verse: String
        :param fums: String
        :return: None
        :raises: Database errors on connection and insertion
        """
        pass

    def remove(self, reference):
        """
        Removes entry from database
        :param reference: String
        :return: None
        :raises: Database errors on connection and insertion
        """
        pass