import telebot
#import psycopg2
import get_order
from time import sleep
from multiprocessing import Process
import os

TOKEN = '1248180056:AAFnMlCgD4WaChjloUSQJWDlpjBkAUka6Z0'
bot = telebot.TeleBot(TOKEN)

'''con = psycopg2.connect(
    database="mydb",
    user="rita",
    password="Testing1001",
    host="127.0.0.1",
    port="5432"
)

cur = con.cursor()
cur.execute("SELECT * FROM orders")
rows = cur.fetchall()
for row in rows:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
con.close()'''
GROUP_ID = -455373776

#print("Database opened successfully")

def check_last_order():
    last_order_id = get_order.get_last_order()[0]
    while True:
        if(get_order.get_last_order()[0] != last_order_id):
            last_order_id = get_order.get_last_order()[0]
            bot.send_message(GROUP_ID, 'new order (id='+str(last_order_id)+')')
        sleep(60)

if __name__ == '__main__':
    procs = []
    proc = Process(target=check_last_order)
    procs.append(proc)
    proc.start()
    for proc in procs:
        proc.join()

    bot.polling(none_stop=True)
