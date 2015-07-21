import cgi

print "Content-type: text/html \n\n"

form = cgi.FieldStorage()
q = form["q"].value
print "This is" + q
