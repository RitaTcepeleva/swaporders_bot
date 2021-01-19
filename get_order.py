import psycopg2

con = psycopg2.connect(
    database="mydb",
    user="rita",
    password="Testing1001",
    host="127.0.0.1",
    port="5432"
)

#cur = con.cursor()

def get_last_order():
    cur = con.cursor()
    cur.execute("SELECT * FROM orders")
    rows = cur.fetchall()
    last_order = rows[len(rows)-1]
    #last_order_id = last_order[0]
    return last_order

print(get_last_order())
