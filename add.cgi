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
todos = sorted([f.split('.')[0] for f in listdir("lists/") if isfile(join("lists", f))])

print "Content-type: text/html\n\n"
print "<html><head><title>Dead Organizer</title>"
print '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'
print '<link rel="stylesheet" type="text/css" href="style.css" />'
print "</head><body>\n"
print '<h1><a href="">&#x2B22; PyList</a> - ajouter une tache </h1>'
print '<hr /> <a href="index.cgi">retour à l\'acceuil</a><hr />'

if form.getvalue('todo') != None :
    if form.getvalue('passwd') == "CY99075328":
        todo = cgi.escape(form.getvalue('todo').decode('utf-8'))
        todolist = cgi.escape(form.getvalue('todolist'))
        with open('lists/{}.txt'.format(todolist), "a") as f :
            f.write("{}\n".format(todo.encode("utf-8")))
    else :
        print 'Mauvais mot de passe'

else:
    print 'entrez une tâche à accomplir'

print '<form  action="add.cgi" method="post">'
print '<label for=\'todolist\'>Liste</label>'
print '<select name="todolist">'
for todo in todos:
    print '<option>{}</option>'.format(todo)
print '</select>'
print '<label for=\'todo\'>Tâche : </label><input type="text" name="todo"><br />'
print '<label for=\'passwd\'>passwd : </label><input type="password" name="passwd">'
print '<br /><input type="submit" value="ajouter">'
print '</form>'
print '<hr />'
print '</body></html>\n'
