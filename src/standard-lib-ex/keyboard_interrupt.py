import sys
import os

def main():

	for i in range(10000000):
		try:
			print(i)
		except KeyboardInterrupt:
			print("Program terminated by keyboard interrupt!")
			raise SystemExit

	print("bye")

main()

# Result:

# ...
# 120112
# 120113
# 120114
# 120115
# ^C120117
# Program terminated by keyboard interrupt!
