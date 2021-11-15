from threading import Thread, Lock, current_thread
from queue import Queue
import time

database_value = 0

# race condition == when 2 or more threads try to modify the same variable at the same time

def increase(lock: Lock):
  global database_value
  
  with lock:
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1) # -> race condition
    database_value = local_copy

if __name__ == "__main__":
  lock = Lock()
  print("start value:", database_value)
  thread1 = Thread(target=increase, args=(lock,))
  thread2 = Thread(target=increase, args=(lock,))
  
  thread1.start()
  thread2.start()
  thread1.join()
  thread2.join()
  
  print("end value:", database_value)
  print("end main")
  
# Queues
def worker(q, lock):
  while True:
    val = q.get()
    with lock:
      print(f'in {current_thread().name} got {val}')
      q.task_done()

if __name__ == "__main__":
  print("Start Main")
  lock = Lock()
  
  queue1 = Queue()
  num_threads1 = 10
  
  for i in range(num_threads1):
    thread = Thread(target=worker, args=(queue1, lock))
    # -> Threads enter infinite loop (while True:) and there are first no items in queue 
    # (come with next for loop). after items are done daemon thread will die 
    # when main thread dies (after "print("End Main")""
    thread.daemon = True 
    thread.start()
    
  for i in range(1, 21):
    queue1.put(i)
    
  queue1.join()
  
  print("End Main")