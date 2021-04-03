import requests

file=open("ids/ids.txt","r")
lines = file.readlines()
file.close()

finalIDS = [None] * len(lines)

i = 0

for line in lines:
    x = line.split("\n")
    finalIDS[i] = x[0]
    i += 1

for record in finalIDS:
    r = requests.get('http://pagfam.geneall.net/3418/pessoas.php?id='+record)
    file1 = open("individual/"+record+".html","w+")
    file1.write(r.text)
    file1.close()