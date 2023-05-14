import mysql.connector

#connecting to database
conn = mysql.connector.connect(
   host = "localhost",
   user = "root",
   password = "",
   database = "swiftuniversity",
   port = 3306
)
#cursor
cur = conn.cursor()
#INSERT 
for i in range(100):
    cur.execute("INSERT INTO users (UserName) VALUES(%s)",(f"MoMo{i}",))

#conn commit
conn.commit()

# select statement
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for r in rows:
   print(f"UserID: {r[0]}, Username = {r[1]}, Email={r[2]}")
#close
conn.close()