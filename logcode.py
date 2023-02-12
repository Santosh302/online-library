#!c:/python27/python.exe
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb
form=cgi.FieldStorage()

a=form.getvalue("text3")

b=form.getvalue("text4")


import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","library")
cursor=db.cursor()

sel="select * from adminlogin where email='%s' or password='%s'"%(a,b)
cursor.execute(sel)
data=cursor.fetchone()

if data[1]==a:
  if data[2]==b:
    print "<script>window.location.href='profile.py?id=%s';alert('login success');</script>"%data[0];
  else:
    print "<script>window.location.href='login.py';alert('Password Not Match');</script>" 
else:
  print "<script>window.location.href='login.py';alert('Email Not Match');</script>"
