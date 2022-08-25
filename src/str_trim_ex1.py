import os

def str_trim(str):
    return str.rstrip(' \t\r\n')

def ReadFile():
  try:
    text_file = open("str_trim_ex1.txt", "r")
    lines = text_file.readlines()
    text_file.close()
    print ('before trim:')
    print (lines)
    for idx, item in enumerate(lines):
        lines[idx] = str_trim(lines[idx])
  except FileNotFoundError:
    print ('config file not found')
    lines = []
  return lines

def main():
  content = ReadFile()
  print ('after trim:')
  print (content)

main()

''' Result:
$ python3 str_trim_ex1.py
before trim:
['aaa\n', 'bbb  \n', 'ccc\t\t\t\n', '  ddd ee\t ff  \n']
after trim:
['aaa', 'bbb', 'ccc', '  ddd ee\t ff']
'''
