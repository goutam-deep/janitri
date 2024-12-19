'''for  row in range(10):
    for col in range(10):
        if col<=10//2 or row>=10//2:
            print(" ",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#print("anil")
#print("hello world")
#functions 
'''def add():
    a,b=10,20
    print(f"sum of {a} and {b}  :",a+b)
add()'''
'''add()
print("anil")
print("hello world")
add()
'''
#with parameters and with return type
'''def add(n1,n2):
    return n1+n2
var=add(10,20)
print(var)'''

#without parameters and with return type
'''def add():
    n1=65
    n2=54
    return n1*n2'''
'''def gautham():
    print("my name si gautham")
    def anil():
        print("my nme is anil")
    anil()
gautham()
'''
'''for name in range(6):
    print("gautham",end="@")

'''
'''a=10
a="anil"
print(a)
def add (a,b,c=10):
    print(a+b+c)
add(a=10,b=20,c=0)'''
'''l1=["anil",1,"true","deep","true","nandhan"]
# a=l1.count("true")
# print(a)'''
# '''for row in range(1,5):
#     for col in range(1,5):
#         print(col,end=" ")
#     print()'''
# def aditye():
#     def local_raudy():
#         def shayaty_bhai():
#             def rocky():
#                 print("kiya vhahiye tereko ... kaam")
            # rocky()
        # shayaty_bhai()
    # local_raudy()
# aditye()
# def movie():
#     def entertanment():
#         print(" power packed aution & entertanment")
#         def moral():
#             print("life is movie we all are actors")
#     

#include<stdio.h>
# int main()




def factrol(num:int =0):
    if num==1 or num==0:
        return 1
    else:
        return num * factrol(num-1)

factrol()