
import sqlite3
import datetime

conn = sqlite3.connect("lite.db")
cur=conn.cursor()
cur.execute("  CREATE TABLE IF NOT EXISTS users_table_bot (user_id NUMERIC NOT NULL PRIMARY KEY, first_name TEXT, last_name TEXT) ")
cur.execute("  CREATE TABLE IF NOT EXISTS links_table_subito (links TEXT NOT NULL PRIMARY KEY, inserttime timestamp) ")
cur.execute("  CREATE TABLE IF NOT EXISTS links_table_immobiliare (links TEXT NOT NULL PRIMARY KEY, inserttime timestamp) ")
cur.execute("  CREATE TABLE IF NOT EXISTS links_table_casa (links TEXT NOT NULL PRIMARY KEY, inserttime timestamp) ")
cur.execute("  CREATE TABLE IF NOT EXISTS links_table_myhome (links TEXT NOT NULL PRIMARY KEY, inserttime timestamp) ")
cur.execute("  CREATE TABLE IF NOT EXISTS links_table_tecnocasa (links TEXT NOT NULL PRIMARY KEY, inserttime timestamp) ")
conn.commit()
conn.close()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def insert(link,table):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT OR IGNORE INTO {} VALUES (?,?)".format(table), (link, datetime.datetime.now()))
    conn.commit()
    conn.close()  



def view(table):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM " + table + " LIMIT 12")
    rows=cur.fetchall()
    conn.close()
    return rows

'''Inserisce una lista di links solo se non esistono'''
def insertIfNotExists(tableName, linksList):
    list_with_new_to_return = []
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    for link in linksList: 
        cur.execute("SELECT links FROM {} WHERE links = ?".format(tableName), (link,))
        data=cur.fetchone()
       
        if data is None:
            # se non esiste lo inserisce
            insert(link, tableName)
            # lo inserisco anche nella lista da restituire
            list_with_new_to_return.append(link)

    conn.close()
    return list_with_new_to_return
            


def insertUsers(user_id, first_name, last_name):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users_table_bot VALUES (?,?,?)", (user_id, first_name, last_name))
    conn.commit()
    conn.close()  


def viewUsers():
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users_table_bot")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE  FROM links_table_casa WHERE links=?",(item,))
    conn.commit()
    conn.close()


#delete('www.casa.it/appartamento/vendita/padova/feriole-selvazzano-dentro-100mq-31335019/')

#  www.casa.it/appartamento/vendita/padova/feriole-selvazzano-dentro-100mq-31335019/




#insert("https://docs.python.org/2/library/sqlite3.html#default-adapters-and-converters", "links_table_subito")
#print(view("links_table_subito"))