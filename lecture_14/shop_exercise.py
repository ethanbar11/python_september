import sqlite3


class Store:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect_to_db(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
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

    def insert_product(self, productName, price, amount):
        sql_query = ''' INSERT INTO inventory(productName,price,amount)
                  VALUES(?,?,?) '''
        curr = self.conn.cursor()
        curr.execute(sql_query, (productName, price, amount))
        self.conn.commit()
        return curr.lastrowid

    def insert_customer(self, customerName, address):
        sql_query = ''' INSERT INTO Customers( customerName, address, is_black_list)
                  VALUES(?,?,?) '''
        curr = self.conn.cursor()
        curr.execute(sql_query, (customerName, address, False))
        self.conn.commit()
        return curr.lastrowid

    def print_inventory(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM inventory")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def print_customers(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM customers")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def __is_customer_exists(self, customer_name):
        cur = self.conn.cursor()
        cur.execute("SELECT customerName FROM customers where customerName=?", (customer_name,))
        rows = cur.fetchall()
        return len(rows) > 0

    def __is_customer_in_black_list(self, customer_name):
        cur = self.conn.cursor()
        cur.execute("SELECT is_black_list FROM customers where customerName=?", (customer_name,))
        rows = cur.fetchall()
        print(rows[0])
        print(rows[0][0])
        return bool(rows[0][0])

    def __validate_enough_items(self, order):
        for item in order:
            cur = self.conn.cursor()
            cur.execute("SELECT amount FROM inventory where productName=?", (item[0],))
            rows = cur.fetchall()
            if (len(rows) <= 0):
                raise ValueError("Not enough items of type {} !".format(item[0]))
            items_amount_in_inventory = rows[0][0]
            if item[1] > items_amount_in_inventory:
                raise ValueError("Not enough items of type {} !".format(item[0]))

    def make_order(self, customer_name, order):
        # Order is going to be like [('Avocado',5),('Meat,10)]
        if not self.__is_customer_exists(customer_name):
            print('NO NO NO! Customer does not exist!!!!')
            return
        is_customer_in_black_list = self.__is_customer_in_black_list(customer_name)
        if is_customer_in_black_list:
            print('Calling police')
            return
        try:
            items_in_order = self.__validate_enough_items(order)
        except ValueError as e:
            print(e)
            # Adding the customer to the black list.

            return
        # Decreasing items from inventory


if __name__ == '__main__':
    store = Store(".\store_db.db")
    store.connect_to_db()
    store.insert_product('Avocado', 20, 5)
    store.insert_product('Shampoo', 500, 5)
    store.create_initial_tables()
    store.make_order('Ethan', [('Avocado', 5), ('Shampoo', 9)])
    # store.insert_customer('Ethan', 'Somewhere in Haifa')
    # store.print_customers()
    # store.insert_product('Woho', 5, 5)
    # store.print_inventory()
