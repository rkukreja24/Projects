#!C:/Users/Admin/AppData/Local/Programs/Python/Python37-32/python.exe
import cgi


print("Content-type: text/html\r\n\r\n")
print("<html>")
print("<head><title>Thank You!</title></head>")
print("<body>")
form=cgi.FieldStorage()
name=form.getvalue("fname")
email=form.getvalue("email")
msg=form.getvalue("comment")

import mysql.connector as sql
db=sql.connect(host='localhost',
               user='root',
               password='',
               database='foodtruckdatabase')

cur=db.cursor()
s="insert into feedback(Name,Email,Comment) values('{}','{}','{}')".format(name,email,msg)
cur.execute(s)
db.commit()
print('<h2 style="text-align:center">')
print('<span style="font-size:100px;">&#10004;</span>')
print('<br>')
print('Thank you, ' + name + '! for your valuable feedback')
print('<br> <br> <br>')
print('<a href="http://localhost/Project/index.html">Main page</a>')
print("</body>")
