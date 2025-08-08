# def fibonacci (num):
#     if num == 1 
#      return 0
#     elif
#      num == 2 or num == 3:
#     return 1
#     else
#     return febonacci (num - 1) + febonacci (num - 2)

def fibonacci(n , rahul={}):
    if n <= 0:
        return 0 
    elif n == 1:
        return 1 
    elif n in rahul:
        return rahul[n]
    else:
        rahul[n] = fibonacci (n-1)+fibonacci (n-2)
        return rahul[n]
print (fibonacci(9))     