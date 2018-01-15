import math

def quadratic(a,b,c):
    det = b*b-4*a*c
    if det<0:
        print("No solution")
        return None
    elif det==0:
        return -b/(2*a),-b/(2*a)
    else:
        x1 = (-b+math.sqrt(b*b-4*a*c))/2*a
        x2 = (-b-math.sqrt(b*b-4*a*c))/2*a
        return x1,x2

def power(x,n=2):
    s = 1
    while n>0:
        s = s*x
        n = n-1
    return s

def enroll(name,gender,age=6,city='Shanghai'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

def add_end(L=[]):
    L.append('END')
    return L
def add_end2(L=None):
    if L is None:
        L = []
    L.append("END")
    return L

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum +n*n
    return sum

def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)

def person1(name,age,*,city='Beijing',job):
    print(name,age,city,job)

def product(x,y=1,*args):
    s = 1
    for n in args:
        s = s*n
    return x*y*s

def product1(numbers):
    if len(numbers)==0:
        raise TypeError("please input one number at least")
    else:
        s = 1
        for i in numbers:
            s = s*i
        return s

def product2(*args):
    if len(args)==0:
        raise TypeError("please input one number at least")
    else:
        s = 1
        for i in args:
            s = s*i
        return s

def fact(n):
    return fact_iter(n,1)

def fact_iter(n,product):
    if n == 1:
        return product
    return fact_iter(n-1,n*product)

def trim(s):
    if s[:1] == ' ':
        s = s[1:]
        s = trim(s)
    if s[-1:] == ' ':
        s = s[:-1]
        s = trim(s)
    return s

def min_max(L):
    min = L[0]
    max = L[0]
    for i in L:
        if i>max:
            max = i
        if i<min:
            min = i
    return min,max
   # print('max is:',max,'min is:',min)

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'Done'

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

def trianges():
    (x for x in range)

def add(x,y,f):
    return f(x)+f(y)


from functools import reduce

def product(x,y=1):
    return x*y

def prod(L):
    return reduce(product,L)

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch:CHAR_TO_FLOAT[ch],s)
    point = 0
    def to_flaot(f,n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f*10+n
        else:
            point = point*10
            return f+n/point
    return reduce(to_flaot,nums,0.0)

def is_odd(L):
    return L%2==1


