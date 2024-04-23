import threading
import time

def thread1fun(sec):
    print("[Thread1] start")
    for _ in range(sec):
        print("[Thread1] aaa", end="\n", flush=True)
        time.sleep(1)
    print("[Thread1] bye ")

def thread2fun(sec):
    print("[Thread2] start")
    for _ in range(sec):
        print("[Thread2] bbbbb", end="\n", flush=True)
        time.sleep(1)
    print("[Thread2] bye ")

def main():
    print("[Main] start")
    thread1 = threading.Thread(target=thread1fun, args=(2,))
    thread2 = threading.Thread(target=thread2fun, args=(4,))
    thread1.start()
    thread2.start()
    print("[Main] ...")
    thread1.join()
    thread2.join()
    print("[Main] bye")

if __name__ == '__main__':
    main()

