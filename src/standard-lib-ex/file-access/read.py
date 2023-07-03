fp = open("read.txt", "r")
if fp != None:
    print ("file open successly")
    str1 = fp.read()
    print (str1)
fp.close()

