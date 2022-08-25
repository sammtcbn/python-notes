import os

def ReadFile():
  try:
    text_file = open("readfile_ex1.txt", "r")
    lines = text_file.readlines()
    text_file.close()
  except FileNotFoundError:
    print ('config file not found')
    lines = []
  except PermissionError:
    print ('Permission denied')
    lines = []
  return lines

def main():
  content = ReadFile()
  print (content)
  print (len(content))

main()

''' Result:
$ python3 readfile_ex1.py
['aaa\n', 'bbb\n']
2
'''

''' Result when file doesn't exist:
$ python3 readfile_ex1.py
config file not found
[]
0
'''
