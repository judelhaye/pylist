#!/usr/bin/python2.7
#coding: utf-8

import cgi, cgitb
from os import listdir
from os.path import isfile, join

cgitb.enable()

####################################
#  HTML generator
####################################
form = cgi.FieldStorage()

URL="http://dead-brain.fr/pylist"
print "Content-type: text/html\n\n"
print "<html><head><title>PyList</title>"
print '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'
print '<link rel="stylesheet" type="text/css" href="style.css" />'
print "</head><body>\n"
print '<h1><a href="', URL, '">&#x2B22; PyList</a> </h1>'
print '<hr />'
print '|| <a href="add.cgi"> ajouter une entrée ?</a> ||'
print '<hr />'

print '<form action="update.cgi" method="post">'
print '<ul>'
print '</ul>'


print '<label for=\'passwd\'>passwd : </label><input type="password" name="passwd">'
print '<input type=submit value="mettre à jour">'
print '</form>'
print '</ul>'
print '</body></html>\n'

