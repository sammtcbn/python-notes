import os

def main():
    base_name = os.path.basename(__file__)
    print ('base name is ' + base_name)

    log_name = os.path.basename(__file__).split('.')[0] + '.log'
    print ('log filename is ' + log_name)

    log_full_path = os.path.join(os.getcwd(), log_name)
    print ('log full path is ' + log_full_path)

    # in one line
    filename = os.path.join(os.getcwd(), os.path.basename(__file__).split('.')[0]+'.log')
    print ('log full path is ' + filename)

if __name__ == '__main__':
	main()
