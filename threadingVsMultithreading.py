# ------ Process ---------
# Process: An instance of a program (e.g a python interpreter)
# + Takes advantage of multiple CPUs and cores
# + Seperate memory space -> Memory is not shared between processes
# + Great for CPU-bound processing
# + New process is started independently from other processes
# + Processes are interruptable/killable
# + One GIL (global interpreter lock) for each process -> avoids GIL limitation
# - Heavyweight
# - Starting a process is slower then starting a thread
# - More memory
# - IPC (inter-process-communication) is more complicated

# ------ Threads ---------
# Threads: An entity within a process that can be scheduled (also known as "leightweight" process)
# A process can spawn multiple threadsj
# + All threads within a process share the same memory
# + Leightweight
# + Starting a thread is faster than starting a process
# + Great for I/O-bound tasks
# - Threading is limited by GIL: Only one thread at a time
# - No effect for CPU-bound tasks
# - Not interruptable/killable
# - Careful with race conditions :/

# ------ GIL ---------
# Gil: Global Interpreter Lock (controversial in python community)
# A lock that allows only one thread at a time to execute in Python
# Needed in CPython because memory management is not thread-safe
# Avoid:
# - Use Multiprocessing
# - Use a different, free-threaded Python implementation (Jython, IronPython)
# - Use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy

# Multiprocessing
from multiprocessing import Process
import os
import time

def square_numbers():
  for i in range(100):
    i * i
    time.sleep(0.1)


if __name__ == '__main__':
  print("Now in the main code. Process name is:", __name__)
  processes = []
  num_processes = os.cpu_count()

  # create processes
  for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

  # start process
  for p in processes:
    p.start()
    
  # join ( wait for process to finish, while that happens it blocks the main thread )
  for p in processes:
    p.join()
    
  print("end main")
  
  
# Multithreading
from threading import Thread

def square_numbers():
  for i in range(100):
    i * i
    time.sleep(0.1)

print("Now in the main code. Process name is:", __name__)
threads = []
num_threads = 10

# create threads
for i in range(num_threads):
  t = Thread(target=square_numbers)
  threads.append(t)

# start thread
for t in threads:
  t.start()

# join ( wait for threaed to finish, while that happens it blocks the main thread )
for t in threads:
  t.join()
  
print("end main")