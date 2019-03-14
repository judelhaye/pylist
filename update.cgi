#!/usr/bin/python2.7
#coding: utf-8

import cgi, cgitb
from os import listdir
from os.path import isfile, join
from itertools import islice

cgitb.enable()

####################################
#  HTML generator
####################################
form = cgi.FieldStorage()
todos = sorted([f for f in listdir("lists/") if isfile(join("lists", f))])

print "Content-type: text/html\n\n"
print "<html><head><title>PyList</title>"
print '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'
print '<META http-equiv="refresh" content="2;URL=<index>">'
print '<link rel="stylesheet" type="text/css" href="style.css" />'
print "</head><body>\n"
print '<h1><a href="">&#x2B22; Dead Organizer</a> - mise à jour des listes </h1>'
print '<hr /> <a href="index.cgi">retour à l\'acceuil</a><hr />'

if form.getvalue("passwd") == "CY99075328":
    if form.getlist('isdone'):
        for item in form.getlist('isdone'):
            print item
            todolist, line = item.split('-')
            index = int(line)
            lines = file("lists/{}".format(todolist), "r").readlines()
            del lines[index]
            file("lists/{}".format(todolist), "w").writelines(lines)
            print 'task deleted.'
else :
    print 'Mauvais mot de passe !'

print '<hr />'
print '</body></html>\n'
