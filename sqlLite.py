
import sqlite3
import datetime

conn = sqlite3.connect("lite.db")
cur=conn.cursor()
cur.execute("  CREATE TABLE IF NOT EXISTS users_table_bot (user_id NUMERIC NOT NULL PRIMARY KEY, first_name TEXT, last_name TEXT, pending INTEGER, admin INTEGER, company TEXT) ")
cur.execute("  CREATE TABLE IF NOT EXISTS edas_table_pdf (user_id NUMERIC NOT NULL PRIMARY KEY, inserttime timestamp, pdf_name TEXT) ")

conn.commit()
conn.close()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def insertUsers(user_id, first_name, last_name, pending=1, admin=0, company="non inserito"):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users_table_bot VALUES (?,?,?,?,?,?)", (user_id, first_name, last_name, pending, admin, company))
    conn.commit()
    conn.close()  


def linkPdf(user_id, insertTime, pdfName):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT OR IGNORE INTO edas_table_pdf VALUES (?,?,?)", (user_id, insertTime, pdfName))
    conn.commit()
    conn.close()  

def getUser(id):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users_table_bot where user_id =?", (id,))
    rows=cur.fetchall()
    conn.close()
    return rows

def setAdmin(id):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE users_table_bot SET admin=1,pending=0 WHERE user_id =?", (id,))
    conn.commit()
    conn.close() 

def setPending(id):
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE users_table_bot SET pending=0 WHERE user_id =?", (id,))
    conn.commit()
    conn.close() 


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
    print(rows)
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
            



def viewUsers():
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users_table_bot")
    rows=cur.fetchall()
    conn.close()
    return rows

def getPendingUsers():
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users_table_bot WHERE pending = 1")
    rows=cur.fetchall()
    conn.close()
    return rows

def getAdminUsers():
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users_table_bot WHERE admin = 1")
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