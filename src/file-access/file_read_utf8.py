fp = open("file_read_utf8.txt", "r")
if fp != None:
    content = fp.read()
fp.close()

print (content)
print ("\n")

print (content.encode('UTF-8'))
print ("\n")

print (content.encode('UTF-8').decode('UTF-8'))
