# function decorator
# allows to add new functionality to another function
import functools

def start_end_decorator(func):
  def wrapper():
    # do something before or after
    print("Start")
    func()
    print("End")
  return wrapper

@start_end_decorator
def print_name():
  print("Alex")
  
# or: print_name = start_end_decorator(print_name)
print_name()

#################
print('##############')

# with arguments
def start_end_dec(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print("Start")
    result = func(*args, **kwargs)
    print("End")
    return result
  return wrapper

@start_end_dec
def add5(x):
  return x + 5

result = add5(10)
print(result)

print(add5.__name__)

# different example:
def repeat(num_times):
  def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator_repeat

@repeat(num_times=3)
def greet(name):
  print(f'Hello {name}')
  
greet("Dieter")


# nested decorators
def start_end_decorator_4(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print("Start")
    result = func(*args, **kwargs)
    print("End")
    return result
  return wrapper

def debug(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    args_repr = [repr(a) for a in args]
    kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
    signature = ", ".join(args_repr + kwargs_repr)
    print(f"Calling {func.__name__}({signature})")
    result = func(*args, **kwargs)
    print(f"{func.__name__!r} returned {result!r}")
    return result
  return wrapper

@debug
@start_end_decorator_4
def say_hello(name):
  greeting = f'Hello {name}'
  print(greeting)
  return greeting

say_hello("dieter")

# class decorators
class CountCalls:
  def __init__(self, func):
    self.func = func
    self.num_calls = 0
  def __call__(self, *args, **kwargs):
    self.num_calls += 1
    print(f'This is executed {self.num_calls} times')
    return self.func(*args, **kwargs)


@CountCalls
def say_hello():
  print("Hello")
  
say_hello()
say_hello()