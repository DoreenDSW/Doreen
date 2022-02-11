a=1
b=1
number=input("Please enter a interger number you want:")
print (number)
for x in range (int(input)):
	c=a+b
	a=b
	b=c
	print(c)

milk_tea="红茶"
milk_tea1="绿茶"
milk_tea2="奶茶"
milk_tea_price=3000
print("我们有红茶，绿茶，奶茶，奶绿请输入想的要奶茶下单。输入'价格'查询价格。")
need=input()
if (need == "价格"):
    print("红茶：3000元，绿茶：4000元，奶茶：5000元")
    print("如果需要请输入需要的奶茶，如果不需要请输'结束'。")
    need=input()
    if (need == "结束"):
        print("谢谢惠顾。")
    if (need==milk_tea):
        print(milk_tea,milk_tea_price)
    elif(need==milk_tea1):
        print(milk_tea1,milk_tea_price+1000)
    elif(need==milk_tea2):
        print(milk_tea2,milk_tea_price+2000)
    else:
        print("白白")


a=0 
b=0
c=100
import random
random_number = random.randint(0,100)
while a!=random_number:
    a=input("Please Enter the number you gussed?")
    a=int(a)
    if random_number<a:
        print(b,a)
        c=a
    elif random_number>a:
        print(a,c)
        b=a
    elif random_number==a:
        print(random_number)


def array():
    return[[1,2,3],[4,5,6],[7,8,9]]
def print_array(x):
    for a in x:
        for b in a: 
            print(b)
print_array(array())


def array():
    return[[1,2,3],[4,5,6],[7,8,9]]
def print_array(x):
    i=0
    while i<len(x):
        print(x[i])
        i=i+1
print_array(array())


def array():
    return[[1,2,3],[4,5,6],[7,8,9]]
def print_array(x):
    i=0
    while i<len(x):
        a=0
        while a<len(x[i]):
            print(x[i][a])
            a=a+1
        i=i+1
print_array(array())





milk_tea="红茶"
milk_tea1="绿茶"
milk_tea2="奶茶"
milk_tea_price=3000
print("我们有红茶，绿茶，奶茶，奶绿请输入想的要奶茶下单。输入'价格'查询价格。")
need=input()
if (need == "价格"):
    print("红茶：3000元，绿茶：4000元，奶茶：5000元")
    print("如果需要请输入需要的奶茶，如果不需要请输'结束'。")
    need=input()
    if (need == "结束"):
        print("谢谢惠顾。")
    if (need==milk_tea):
        print(milk_tea,milk_tea_price)
    elif(need==milk_tea1):
        print(milk_tea1,milk_tea_price+1000)
    elif(need==milk_tea2):
        print(milk_tea2,milk_tea_price+2000)
    else:
        print("白白")


a=0 
b=0
c=100
import random
random_number = random.randint(0,100)
while a!=random_number:
    a=input("Please Enter the number you gussed?")
    a=int(a)
    if random_number<a:
        print(b,a)
        c=a
    elif random_number>a:
        print(a,c)
        b=a
    elif random_number==a:
        print(random_number)


def array():
    return[[1,2,3],[4,5,6],[7,8,9]]
def print_array(x):
    for a in x:
        for b in a: 
            print(b)
print_array(array())


def array():
    return[[1,2,3],[4,5,6],[7,8,9]]
def print_array(x):
    i=0
    while i<len(x):
        print(x[i])
        i=i+1
print_array(array())


def array():
    return[[1,2,3],[4,5,6],[7,8,9]]
def print_array(x):
    i=0
    while i<len(x):
        a=0
        while a<len(x[i]):
            print(x[i][a])
            a=a+1
        i=i+1
print_array(array())





