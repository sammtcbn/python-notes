try:
    fp = open ("test.txt", "r")
    print (fp.read())
    fp.close()
except FileNotFoundError:
    print ("file not found")
