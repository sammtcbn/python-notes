import threading
import time

def threadfun(name, sec):
    print("[Thread-{}] start".format(name))
    for _ in range(sec):
        print("[Thread-{}] ...".format(name), end="\n", flush=True)
        time.sleep(1)
    print("[Thread-{}] bye".format(name))

def main():
    print("[Main] start")
    thread1 = threading.Thread(target=threadfun, args=("a", 3,))
    thread2 = threading.Thread(target=threadfun, args=("b", 6,))
    thread1.start()
    thread2.start()
    print("[Main] ...")
    thread1.join()
    thread2.join()
    print("[Main] bye")

if __name__ == '__main__':
    main()

"""
Result:

[Main] start
[Thread-a] start
[Thread-a] ...
[Thread-b] start
[Thread-b] ...
[Main] ...
[Thread-a] ...
[Thread-b] ...
[Thread-a] ...
[Thread-b] ...
[Thread-a] bye
[Thread-b] ...
[Thread-b] ...
[Thread-b] ...
[Thread-b] bye
[Main] bye

"""
