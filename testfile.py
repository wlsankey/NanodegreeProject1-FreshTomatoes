#!/usr/bin/env python

import fresh_tomatoes
import cgi
import cgitb
cgitb.enable() #for troubleshooting


print ("Content-Type: text/html")
print ()

form = cgi.FieldStorage()
variable = form["q"].value

print (variable)