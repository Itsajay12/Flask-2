import sqlite3
con=sqlite3.connect('database3.db')
print('opened db ')
con.execute('create table book(name char(20),author char(20),pdf char(20));')
print("ceated")
con.close()