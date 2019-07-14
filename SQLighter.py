import sqlite3,random

class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM Games').fetchall()

    def select_single_inter(self, r, a):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            if a == 1:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%inter%" AND (age = "6-9" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 2:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%inter%" AND (age = "10-17" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 3:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%inter%" AND (age = "10-17" OR age = "0" OR age = "14-17") ORDER BY RANDOM() LIMIT 1 ').fetchall()

    def select_single_street(self, r, a):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            if a == 1:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%street%" AND (age = "6-9" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 2:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%street%" AND (age = "10-17" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 3:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%street%" AND (age = "10-17" OR age = "0" OR age = "14-17") ORDER BY RANDOM() LIMIT 1 ').fetchall()

    def select_single_joke(self, r, a):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            if a == 1:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%joke%" AND (age = "6-9" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 2:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%joke%" AND (age = "10-17" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 3:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%joke%" AND (age = "10-17" OR age = "0" OR age = "14-17") ORDER BY RANDOM() LIMIT 1 ').fetchall()

    def select_single_relax(self, r, a):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            if a == 1:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%relax%" AND (age = "6-9" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 2:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%relax%" AND (age = "10-17" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 3:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%relax%" AND (age = "10-17" OR age = "0" OR age = "14-17") ORDER BY RANDOM() LIMIT 1 ').fetchall()

    def select_single_touch(self, r, a):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            if a == 1:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%touch%" AND (age = "6-9" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 2:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%touch%" AND (age = "10-17" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 3:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%touch%" AND (age = "10-17" OR age = "0" OR age = "14-17") ORDER BY RANDOM() LIMIT 1 ').fetchall()

    def select_single_quick(self, r, a):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            if a == 1:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%quick%" AND (age = "6-9" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 2:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%quick%" AND (age = "10-17" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 3:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%quick%" AND (age = "10-17" OR age = "0" OR age = "14-17") ORDER BY RANDOM() LIMIT 1 ').fetchall()

    def select_single_know(self, r, a):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            if a == 1:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%know%" AND (age = "6-9" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 2:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%know%" AND (age = "10-17" OR age = "0" OR age = "6-13") ORDER BY RANDOM() LIMIT 1 ').fetchall()
            if a == 3:
                return self.cursor.execute('SELECT * FROM Games WHERE type LIKE "%know%" AND (age = "10-17" OR age = "0" OR age = "14-17") ORDER BY RANDOM() LIMIT 1 ').fetchall()
                
    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM Games').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
