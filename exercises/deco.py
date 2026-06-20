import time
from typing import Callable, Coroutine, Any
from functools import wraps
import asyncio

def deco_time(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper

@deco_time
def test():
    time.sleep(1)
    return "Done"

print(test())

#test = deco_time(test)

def limit(limit : int):
    def wrapper(func: Callable):
        def inner(*args, **kwargs):
            nonlocal limit
            if limit <= 0:
                print("Limit exceeded")
                return None
            
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            limit -= 1
            print(f"Execution time: {end - start}")
            return result
        return inner
    return wrapper

@limit(2)
def my_func(slepp_time : int):
    '''Decorator to limit the number of calls to a function and measure execution time.'''
    time.sleep(slepp_time)
    return "Done"

#my_func = limit(2)(my_func)
my_func(1)
my_func(1)  
my_func(1)


def limit_calls(limit : int):
    def wrapper(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            '''Decorator to limit the number of calls to a function.'''
            nonlocal limit
            if limit <= 0:
                print("Limit exceeded")
                return None
            
            result = func(*args, **kwargs)
            limit -= 1
            return result
        return inner
    return wrapper


print(my_func.__doc__)
print(my_func.__name__)


#deco for asynchronous functions
def deco_async(coroutine_func : Callable[..., Coroutine[Any, Any, Any]]):
    async def wrapper(*args, **kwargs):
        res = await coroutine_func(*args, **kwargs)
        return res
    return wrapper

@deco_async
async def async_func():
    await asyncio.sleep(0.5)
    return 1

asyncio.run(async_func())
#await async_func() in Jupyter
#async_func = deco_async(async_func)