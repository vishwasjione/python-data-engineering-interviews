
def f1(*args,**kargs):
    print(args)
    print(kargs)
    for i in args:
        print (i)
    for i in enumerate(kargs.items()):
        print(i)

f1(1,3,4,[4,5],x=5)

