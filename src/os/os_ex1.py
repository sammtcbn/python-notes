import os

path=os.getcwd()
print(path)

os.chdir (path)

os.mkdir('newDir')

os.rename('newDir', 'newDir2')

os.rmdir('newDir2')

fp = open("aa.txt", "w")
fp.close()
