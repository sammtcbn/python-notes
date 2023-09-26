import os

def main():
	base_name = os.path.basename(__file__)
	print ('base name is ' + base_name)

	log_name = os.path.basename(__file__).split('.')[0] + '.log'
	print ('log name is ' + log_name)

if __name__ == '__main__':
	main()
