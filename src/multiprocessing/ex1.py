import multiprocessing
import os
import time
import random
from datetime import datetime

def msgprint(msg):
    print(datetime.now(), msg)

# Define a worker function that each process will execute
def worker_function(index):
    msgprint(f"Process {os.getpid()} is processing task {index}")
    time.sleep(random.randint(5, 9))
    msgprint(f"Process {os.getpid()} is processing task {index} bye")
    return index * 2  # Perform some simple task and return the result

if __name__ == "__main__":
    msgprint("======= create pool ======")
    # Create a pool of processes with a maximum of 4 processes
    pool = multiprocessing.Pool(processes=4)

    # Submit multiple tasks to the pool, each invoking worker_function
    results = []
    for i in range(10):
        msgprint(f"======= sumit task {i} to pool ======")
        results.append(pool.apply_async(worker_function, args=(i,)))

    # Wait for all tasks to complete and gather results
    msgprint("======= pool close ======")
    pool.close()
    msgprint("======= pool join ======")
    pool.join()  # Wait for all processes to complete

    msgprint("======= pool join done ======")
    # Print the results
    for result in results:
        print(f"Task result: {result.get()}")

"""
Result:


$ python ex1.py
2024-05-03 14:46:18.051040 ======= create pool ======
2024-05-03 14:46:18.063523 ======= sumit task 0 to pool ======
2024-05-03 14:46:18.063606 ======= sumit task 1 to pool ======
2024-05-03 14:46:18.063627 ======= sumit task 2 to pool ======
2024-05-03 14:46:18.063663 ======= sumit task 3 to pool ======
2024-05-03 14:46:18.063689 ======= sumit task 4 to pool ======
2024-05-03 14:46:18.063713 ======= sumit task 5 to pool ======
2024-05-03 14:46:18.063975 ======= sumit task 6 to pool ======
2024-05-03 14:46:18.064026 ======= sumit task 7 to pool ======
2024-05-03 14:46:18.064038 ======= sumit task 8 to pool ======
2024-05-03 14:46:18.064046 ======= sumit task 9 to pool ======
2024-05-03 14:46:18.064061 ======= pool close ======
2024-05-03 14:46:18.064041 Process 77442 is processing task 0
2024-05-03 14:46:18.064128 ======= pool join ======
2024-05-03 14:46:18.064115 Process 77443 is processing task 1
2024-05-03 14:46:18.064217 Process 77444 is processing task 2
2024-05-03 14:46:18.064242 Process 77445 is processing task 3
2024-05-03 14:46:23.064357 Process 77443 is processing task 1 bye
2024-05-03 14:46:23.064978 Process 77443 is processing task 4
2024-05-03 14:46:25.064315 Process 77442 is processing task 0 bye
2024-05-03 14:46:25.064477 Process 77444 is processing task 2 bye
2024-05-03 14:46:25.064972 Process 77442 is processing task 5
2024-05-03 14:46:25.065172 Process 77444 is processing task 6
2024-05-03 14:46:26.064488 Process 77445 is processing task 3 bye
2024-05-03 14:46:26.064978 Process 77445 is processing task 7
2024-05-03 14:46:28.065219 Process 77443 is processing task 4 bye
2024-05-03 14:46:28.065524 Process 77443 is processing task 8
2024-05-03 14:46:31.065473 Process 77444 is processing task 6 bye
2024-05-03 14:46:31.065788 Process 77444 is processing task 9
2024-05-03 14:46:32.065240 Process 77442 is processing task 5 bye
2024-05-03 14:46:33.065201 Process 77445 is processing task 7 bye
2024-05-03 14:46:35.065734 Process 77443 is processing task 8 bye
2024-05-03 14:46:36.065970 Process 77444 is processing task 9 bye
2024-05-03 14:46:36.067213 ======= pool join done ======
Task result: 0
Task result: 2
Task result: 4
Task result: 6
Task result: 8
Task result: 10
Task result: 12
Task result: 14
Task result: 16
Task result: 18

"""
