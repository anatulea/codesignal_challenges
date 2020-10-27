# def fizzBuzz(n):
#     for i in range(1, n+1):
#         if i%3==0 and i%5==0:
#             print("FizzBuzz")
#         elif i%3==0:
#             print("Fizz")
#         elif i%5==0:
#             print("Buzz")
#         else:
#             print (i)

def fizzBuzz(n=100):
    mylist=[]
    for i in range(1, n+1):
        if i%3==0 and i%5==0:
            mylist.append("FizzBuzz")
        elif i%3==0:
            mylist.append("Fizz")        
        elif i%5==0:
            mylist.append("Buzz")  
        else:
            mylist.append(str(i))     
    return mylist
print(fizzBuzz())