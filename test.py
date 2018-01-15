def add(x,y,f):
    return f(x)+f(y)

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax +n
        return ax
    return sum
f = lazy_sum(1,2,3,4,5)
print(f)
print(f())


def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())




def count_1():
        def f(j):
            def g():
                return j*j
            return g
        fs = []
        for i in range(1,4):
            fs.append(f(i))
        return fs

f1, f2, f3 = count_1()

print(f1())
print(f2())
print(f3())
print('---------------------------------')#分隔符

def createCounter():
    def f():
        n = 0
        while True:
            n = n+1
            yield n
    sun = f()
    def counter():
        return next(sun)
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


print('--------------------------')

def createCounter():
    fs=[0]
    def counter():
        fs[0] = fs[0]+1
        return fs[0]
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

print('--------------------------')

def createCounter():
    n = 0
    def f():
        nonlocal n
        n = n+1
        return n
    return f

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

print('--------------------------')


print('------------匿名函数--------------')

def build(x,y):
    return lambda: x*x+y*y

print(build(1,2)())



is_odd = lambda n:n%2==1

L = list(filter(is_odd,range(1,20)))
print(L)

print('---------------装饰器------------------\n')


def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018-1-15')

now()

def log(text):
    def decorater(func):
        def wrapper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorater

@log('execute')
def now():
    print(2018-1-15)

now()
print('---------')
print(now.__name__)


#完整的decorator写法：
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print(" call %s():" %func.__name__)
        return func(*args,**kw)
    return wrapper


#带参数的decorator写法：
import functools

def log(text):
    def decorator(func):
        @functools.warps(func)
        def warpper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return wrapper
        return decorator

print('-------练习------')

import functools
import time


def metric(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        start = time.clock()
        execfunc = func(*args,**kw)
        end = time.clock()
        duration = end-start
        print('%s execued in %s' %(func.__name__,duration))
        return execfunc
    return wrapper

@metric
def fast(x,y):
    time.sleep(0.0012)
    return x+y

f = fast(11,22)
print(f)

@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x*y*z

s = slow(11,22,33)
print(s)
