import os
import string

os.chdir('C:\Users\FILBERT\Documents\Filbert 2\Python')

file = open("text.txt", "r")
text = file.read().lower()
output1 = ""
for i in text:
    if i not in string.punctuation:
        output1 += i
text = output1
lst = text.split(" ")
d = {}
for j in lst:
    if j not in d:
        d[j] = 1
    else:
        d[j] = 1
output2 =[]
for k in d:
    if d[k] == 1:
        output2.append(k)
print(output2)











#(╯°□°）╯︵ ┻━┻