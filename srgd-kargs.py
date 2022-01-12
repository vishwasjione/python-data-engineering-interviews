def f(*args,**kwargs):
    print(args, kwargs)

f(2,4)
f(2,3,[5,6])
f(2,3,[5,6],a=1,b=4)