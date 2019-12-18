import PyPDF2
import re
import os
import json

object = PyPDF2.PdfFileReader("test.pdf")
NumPages = object.getNumPages()

offset = 8
ref = {}
words = []
with open("words.txt", "r") as file:
    for cnt, line in enumerate(file):
        words.append(str(line.rstrip('\n')))
        print(words)


for i in range(0, NumPages):
    print("page " + str(i) + " / " + str(NumPages))
    PageObj = object.getPage(i)
    Text = PageObj.extractText()
    for w in range (0, len(words)): 
        parola = words[w]
        ref.setdefault(parola, [])
        ResSearch = re.search(parola, Text)
        if ResSearch:
            ref[parola].append(i - offset)
            print("found at     ")
            print(str(i - offset))


reference = open("reference.txt", "w")
reference.write("Words:       Pages:")
reference.write("\n")
for k,v in ref.items():
    reference.write(str(k))
    reference.write("    ")
    for i in range(0, len(v)):
        if i != 0:
            reference.write(", ")
        reference.write(str(v[i]))
        
    reference.write("\n")
reference.close()
