import mysql.connector as mysql

mydb=mysql.connect(host="localhost",user="root",password="root",database="bank")
mycus=mydb.cursor()

n=int(input("enter bill"))
p=int(input("enter amt paid"))
query="update hotel set paid= {} where bill_no= {}".format(p,n)

mycus.execute(query)


mydb.commit()

mycus.execute("select * from hotel;")

data=mycus.fetchall()

for i in data:
    print(i)


