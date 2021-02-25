import pymysql


mypass = 'Muhaz8164'
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)

