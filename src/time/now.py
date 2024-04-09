from datetime import datetime

def get_current_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def main():
    now1 = datetime.now()
    print(now1)
    print(get_current_timestamp())

if __name__ == '__main__':
    main()
