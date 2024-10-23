'''
 open file.txt read print and close
'''

f = open("file.txt", "r")
data = f.read()
print(data)
f.close()