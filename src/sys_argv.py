import sys

def main():
	procname = sys.argv[0]
	firstname = sys.argv[1]
	lastname = sys.argv[2]
	age = sys.argv[3]

	print("process name " + procname)
	print("first name " + firstname)
	print("last name " + lastname)
	print("age " + age)

main()

# Result:
# $python sys_argv.py sam lin 10
# process name sys_argv.py
# first name sam
# last name lin
# age 10
