import requests

r = requests.get('http://pagfam.geneall.net/3418/pessoas_search.php?start=0&orderby=&sort=&idx=0&search=')
f = requests.get('http://pagfam.geneall.net/3418/pessoas_search.php?start=30&orderby=&sort=&idx=0&search=')
g = requests.get('http://pagfam.geneall.net/3418/pessoas_search.php?start=60&orderby=&sort=&idx=0&search=')
j = requests.get('http://pagfam.geneall.net/3418/pessoas_search.php?start=90&orderby=&sort=&idx=0&search=')
k = requests.get('http://pagfam.geneall.net/3418/pessoas_search.php?start=120&orderby=&sort=&idx=0&search=')

file = open("record0.html", "w+")
file.write(r.text)
file.close()

file = open("record30.html", "w+")
file.write(f.text)
file.close()

file = open("record60.html", "w+")
file.write(g.text)
file.close()

file = open("record90.html", "w+")
file.write(j.text)
file.close()

file = open("record120.html", "w+")
file.write(k.text)
file.close()