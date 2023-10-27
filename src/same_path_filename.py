import os

def main():
  fn = os.path.dirname(os.path.abspath(__file__)) + "/app.ini"
  print (fn)

main()

''' Result:
$ python3 same_path_filename.py
/home/sam/spe/lang/python/src1/app.ini
'''
