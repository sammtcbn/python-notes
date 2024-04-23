import threading
import time

def thread1fun():
    print("[Thread1] start")
    for _ in range(3):
        print("[Thread1] aaa", end="\n", flush=True)
        time.sleep(1)
    print("[Thread1] bye ")

def thread2fun():
    print("[Thread2] start")
    for _ in range(5):
        print("[Thread2] bbbbb", end="\n", flush=True)
        time.sleep(1)
    print("[Thread2] bye ")

def main():
    print("[Main] start")
    thread1 = threading.Thread(target=thread1fun)
    thread2 = threading.Thread(target=thread2fun)
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
[Thread1] start
[Thread1] aaa
[Thread2] start
[Thread2] bbbbb
[Main] ...
[Thread1] aaa
[Thread2] bbbbb
[Thread1] aaa
[Thread2] bbbbb
[Thread1] bye
[Thread2] bbbbb
[Thread2] bbbbb
[Thread2] bye
[Main] bye
"""
