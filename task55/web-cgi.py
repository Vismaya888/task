import cgi
form = cgi.FieldStorage()
if form.getvalue('java'):
    java_flag = "ON"
else:
    java_flag = "OFF"
if form.getvalue('Python'):
    python_flag = "ON"
else:
    python_flag = "OFF"

print("content-type:text/html")
print()
print("<html>")
print("<head>")
print("<title>Checkbox - Third CGI Program</title>")
print("</head>")
print("<body>")
#print(form.getvalue("java"))
print("<h2> CheckBox Java is : {0}</h2>".format(java_flag))
print("<h2> CheckBox Python is : {0}</h2>".format(python_flag))
print("</body>")
print("</html>")