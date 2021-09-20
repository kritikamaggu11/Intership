#!/usr/bin/env python
# coding: utf-8

# # Python Worksheet 1

# ### Find factorial of number

# In[9]:


num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)


# ### Find whether a number is prime or composite

# In[4]:


num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is Composite number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "is NOT a prime number it is a COMPOSITE number")


# ### Check whether a given string is palindrome or not

# In[10]:


def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "level"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")


# ### To get the third side of right-angled triangle from two given sides

# In[12]:


def sides(a, b):
   h = (a**2 + b**2)**0.5
   return h
print(sides(3,4))


# ### Print the frequency of each of the characters present in a given string

# In[13]:


string=input("Enter the string ")
freq=[None]*len(string)
for i in range(0,len(string)):
  freq[i]=1
  for j in range(i+1,len(string)):
    if(string[i]==string[j]):
        freq[i]=freq[i]+1
        string=string[:j]+'0'+string[j+1:];
print("Character and their frequency");
for i in range(0,len(freq)):
    if(string[i]!=' ' and string[i]!='0'):
        print(string[i]+"="+str(freq[i]))


# In[ ]:





# In[ ]:





# In[ ]:




