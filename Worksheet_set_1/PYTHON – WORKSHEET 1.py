#!/usr/bin/env python
# coding: utf-8

# # PYTHON – WORKSHEET 1

# Q11. Write a python program to find the factorial of a number. 

# In[6]:


import math
def fact(n):
    return(math.factorial(n))
num=int(input("enter the number:"))
f=fact(num)
print("factorial of",num,"is",f)


# Q12. Write a python program to find whether a number is prime or composite

# In[3]:


num=int(input("Enter any number:"))
if num>1:
    for i in range(2, num):
        if(num % i) == 0:
            print(num,"is NOT a prime number")
            break
    else:
        print(num,"is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime nor composite number")
else:
    print(num,"is NOT a prime number it is a COMPOSITE number")


# Q13. Write a python program to check whether a given string is palindrome or not.

# In[12]:


my_str = 'AIBOHPHOBIA'
my_str = my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# Q14. Write a Python program to get the third side of right-angled triangle from two given sides. 

# In[15]:


import math

a = float(input("Enter base:"))
b = float(input("Enter height:"))

c = math.sqrt(a**2+b**2)
print("Hypotenuse=",c)


# Q15. Write a python program to print the frequency of each of the characters present in a given string. 

# In[38]:


from collections import Counter

test_str = "PARAS GANDHARWAL"

res = Counter(test_str)

print ("Count of all characters in PARAS GANDHARWAL is :\n " + str(res))

