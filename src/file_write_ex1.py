fp = open("note.txt", "w")
if fp != None:
    print ("file open successly")
    fp.write ("Hello\n")
    fp.write ("World\n")
fp.close()

