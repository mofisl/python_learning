import functools
import time
def time_master(func):
    @functools.wraps(func)
    def call_func():
        start = time.time()
        func()
        end = time.time()
        print(f'{(start - end):.2f}')
    return call_func
@time_master
def myfunc():
    time.sleep(2)
myfunc()