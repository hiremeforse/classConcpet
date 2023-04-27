class Test():

    # def test(self):
    #     print("this is the class based view")
    
    def __init__(self):
        print("0 arg constuctor")

t = Test()


class Myclass():
    
    def m1(self, val1, val2):
        print(val1,val2)
        self.val1 = val1
        self.val2 = val2
        self.m2()

    def m2(self):
        print("m2 method is exectued")
        print(self.val1+self.val2)

t = Myclass()
t.m1(10,20)
t.m2()


class test:
    a = 10 
    def __init__(self,a):
        print("local args", a)
        print("converted Args", self.a)

t = test(100)



class operations():

    def __init__(self,a,b):
        print(a,10)

        # conversion of local variable to class level use self keyword
        self.a = a 
        self.b = b
        print("local constructor end")
    def add(self):
        print(self.a + self.b)
    
    def mul(self):
        print(self.a * self.b)

t = operations(10,20)
t.add()
t.mul()


class Emp:

    def __init__(self,eid,ename,esal):

        print("constutor arguments")
    
        # conversion local to class level

        self.eid = eid
        self.ename = ename
        self.esal = esal

        print("ending of this", eid,ename,esal)

    def disp(self):
        print(" in disp function ")
        a = self.ename
        print(a)
        print("eid id: {} ename : {} esal : {}".format(self.eid,self.ename,self.esal))


t = Emp(1,"punit",1900000)
t.disp()


class test:

    def __str__(self):
        return "this is string data "

t = test()
# print(t)


def test(function):

    print("outside function")

    def inside(self):
        print("this is inside function")


    return inside

t = test("ghjkl")
print(t)



def my_decorator_func(func):
    print("this is outside func")
    def wrapper_func():
        print("inside this it is there")
        func()
        print("after this is created")
    return wrapper_func

@my_decorator_func
def my_func():
    print("calling")
    pass

print(my_func())



def punittest(args,**kwargs):

    print(args)
    for key,values in kwargs.items():
        print(key,values)

a = punittest("punitkulkarni mirafra technologies", name="punit",surname="kulkarni")
print(a)


d = { "kulkarni" : 8765432, "this" : 456789876,"apple" : 128765432345678343}


a = sorted(d.items() ,key= lambda x : x[1])
print(a)



def loginrequired(func):
    print("outside of the function")
    def test1(self):
        print("insdide of the fucntion")

        func()
    
    return test1

@loginrequired
def add():
    print("this is for self printing")


print(add())


def my_decorator_func(func):
    print("this is outside func")
    def wrapper_func():
        print("inside this it is there")
        func()
        print("after this is created")
    return wrapper_func

@my_decorator_func
def my_func():
    print("calling")
    pass

print(my_func())

def testing(func):
    print("what is this ")
    def do_this():
        print(self.a ,self.b)
        print("this is before passing")
        func()
    return do_this

@testing
def testing(a,b):
    print("this is there for testing")
a = testing(10,20)
print(a)








print("____________________")



def binary_search(target,li):


    start = 0 
    end = len(li) -1 


    while (start <= end):
        mid = start + end // 2 

        if li[mid] == target:
            print(mid)
            break
        elif li[mid] > target:
            end = mid -1 
        else:
            start = mid +1 

li = [1,2,3,4,5,6,7]
a = binary_search(6,li)
print(a)





class Parent:
    a = 10 
    b = 20 


class child(Parent):
    def test(self):
        print("this is inside the child")
        print(self.a,self.b)


c = child()
c.test




#Conversions on local variables to class level variables

class Myclass():
    
    def m1(self,val1,val2):
        print(val1,val2)
        self.val1 = val1
        self.val2 = val2
    
    def m2(self):
        print(self.val1,self.val2)


t = Myclass()
t.m1(10,20)
t.m2()