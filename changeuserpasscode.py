#!c:/python27/python.exe
print "Content-type:text/html\r\n\r\n"

import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","library")
cursor=db.cursor()


import cgi,cgitb
form=cgi.FieldStorage()
id=form.getvalue("id")
a=form.getvalue("opass")
b=form.getvalue("npass")
c=form.getvalue("cpass")

print id
print a
print b
print c

up="update registration set password='%s' where id='%s'"%(b,id)
cursor.execute(up)
db.commit()

print"<script>window.location.href='gallary.py';alert('password change successful');</script>"
