'''Write a Python program to construct the following pattern, using a nested for loop '''
'''
*
**
***
****
*****
****
***
**
*
'''
sum = 0
number = int(input("Enter a number to set the base of the triangle : "))

# for i in range(number):
#     print(times*"*")
#     times +=1
# for j in range(number):
#     print(times*"*")
#     times +=1
ceil = (number*(number+1))/2
for j in range(2*(number + 1)):
    if sum>= ceil:
        a-=1
        print(a*"*")
    else:
        a = j
        print(a*"*")
        sum += a
        
    
    

    

    
