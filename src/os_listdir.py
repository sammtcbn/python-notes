import sys
import os

workdir = os.getcwd()

def main():
	print("workdir - " + workdir + "\n")

	print(os.listdir(workdir))
	print("\n")

	for f in os.listdir(workdir):
		print(f)

main()
