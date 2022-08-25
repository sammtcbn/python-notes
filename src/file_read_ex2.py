fp = open("note.txt", "r")
if fp != None:
    print ("file open successly")
    lst1 = fp.readlines()
    print (lst1)
    for line in lst1:
        print (line, end="")
fp.close()

