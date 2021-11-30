from multiprocessing import Process, Value, Array, Lock, Queue, Pool
import time

def add_100(number, lock, array):
  for i in range(100):
    time.sleep(0.01)
    
    with lock:
      number.value += 1
      
    for i in range(len(array)):
      with lock:
        array[i] += 1
      
      
def square(numbers, queue):
  for i in numbers:
    queue.put(i*i)
    
def make_negative(numbers, queue):
  for i in numbers:
    queue.put(-1 * i)
    
def cube(number):
  return number * number * number
    
if __name__ == "__main__":
  lock = Lock()
  shared_number = Value('i', 0)
  shared_array = Array('d', [0.0, 100.0, 200.0])
  print('Number at beginning is', shared_number.value)
  print('Array at beginning is', shared_array[:])
  
  p1 = Process(target=add_100, args=(shared_number, lock, shared_array))
  p2 = Process(target=add_100, args=(shared_number, lock, shared_array))
  
  p1.start()
  p2.start()
  
  p1.join()
  p2.join()
  
  print('Number at end is:', shared_number.value)
  print('Array at end is', shared_array[:])
  
  ###### with queue
  numbers = range(1, 6)
  q = Queue()
  p3 = Process(target=square, args=(numbers, q))
  p4 = Process(target=make_negative, args=(numbers, q))
  
  p3.start()
  p4.start()

  p3.join()
  p4.join()
  
  while not q.empty():
    print(q.get())
    
  ######  Pool
  pool = Pool()
  # map, apply, join, close -> methods
  numbers = range(10)
  # execute function by different processess
  result = pool.map(cube, numbers)
  
  # only one function
  # result = pool.apply(cube, 10)
  
  pool.close()
  pool.join()
  
  print(result)
  