import sqlite3


class Store:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect_to_db(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            print(sqlite3.version)
        except Exception as e:
            print(e)

    def create_initial_tables(self):
        inventory_string_table = """CREATE TABLE IF NOT EXISTS inventory (
	id integer PRIMARY KEY,
	productName text NOT NULL,
	price float,
	amount int
);

"""
        customer_string_table = """CREATE TABLE IF NOT EXISTS Customers (
        	id integer PRIMARY KEY,
        	customerName text NOT NULL,
        	address text,
        	is_black_list boolean
        );

        """
        self.create_table(inventory_string_table)
        self.create_table(customer_string_table)

    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    store = Store(".\store_db.db")
    store.connect_to_db()
    store.create_initial_tables()
