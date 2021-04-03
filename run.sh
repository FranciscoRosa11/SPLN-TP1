#!/usr/bin/bash

rm ids/ids.txt

python3 getHTML.py

python3 script.py 'records/record0.html'
python3 script.py 'records/record30.html'
python3 script.py 'records/record60.html'
python3 script.py 'records/record90.html'
python3 script.py 'records/record120.html'

python3 getFromTXT.py