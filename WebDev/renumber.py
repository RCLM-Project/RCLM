#!/usr/bin/env python
##Originally written by Moore
with open('asdf.xml', 'r') as file:
    filedata = file.read()

for x in range(3901,1344,-1):
    filedata = filedata.replace('\"wynken1509_' + str(x), '\"wynken1509_' + str(x + 1))

with open('asdf.xml', 'w') as file:
    file.write(filedata)
