#!c:/python27/python.exe
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb
form=cgi.FieldStorage()

a=form.getvalue("text1")
b=form.getvalue("text2")
c=form.getvalue("text3")
d=form.getvalue("text4")
#print a
#print b
#print c
#print d


import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","library")
cursor=db.cursor()
#print "ok"

ins="insert into contact(name,email,subject,massage) values('%s','%s','%s','%s')"%(a,b,c,d)
cursor.execute(ins)
db.commit()
print"<script>window.location.href='contact.py';alert('contact data save');</script>"