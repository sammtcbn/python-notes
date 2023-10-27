def main():
    configfile = open("load_list_from_file.txt", "r")
    data = configfile.read()
    data_into_list = data.split(" ")
    data_into_list = [item.strip() for item in data_into_list]
    print(type(data_into_list))
    print(data_into_list)

if __name__ == '__main__':
    main()
