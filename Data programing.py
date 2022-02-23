#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[75]:


a = 0
def b():
    global a
    a = c(a)
def c(a):
    return a + 2

b()
b()
b()
a


# ## Question 2

# In[76]:


try: 
    def fileLength(file):
        import os
        result = os.stat(file)
        return result.st_size

    print("The size of file in bytes: ",fileLength("C:/idterm.py"))
    
except FileNotFoundError:
    print("idterm.py file not found.")


# ## Question 3

# In[77]:



# Parent class
class Marsupial():
    def __init__(self):
        self.pouch_contents = []
    
    def put_in_pouch(self, thing):
        self.pouch_contents.append(thing)
    
    def __str__(self):
        return "I have {} in my pouch".format(self.pouch_contents)
    
    def __repr__(self):
        return 'Marsupial <{}>'.format(self.pouch_contents)

k = Marsupial()
k.put_in_pouch("doll")
k.put_in_pouch("firetruck")
k.put_in_pouch("kitten")


# In[78]:


k


# In[79]:



# Child class
class Kangaroo(Marsupial):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        print("I am a Kangaroo located at coordinates ", (self.x, self.y))


        
k = Kangaroo(0,0)


# ## Question 4

# In[80]:



# Function defining
def collatz(n):
    if n == 1:
        return n
    else:
        if n%2 == 0:
            n = n/2
            print(n)
            return(collatz(n))
                        
        else:
            n = 3*n + 1
            print(n)
            return(collatz(n))
    
# Function calling
num = int(input("Enter a number: "))
collatz(num)
    


# ## Question 5

# In[81]:



# Funation defining
def binary(integer):
    if integer == 0:
        return 0
    else:
        return (integer % 2 + 10 * binary(int(integer // 2)))
    

# Calling function
n = int(input("Enter a non-negative integer: "))
print(binary(n))


# ## Question 6

# <html>
# <head>
#     <title>test</title>
# </head>
# <body>
#     <h1>W3C Mission</h1>
#     <h2>Principles</h2>
# </body>
# </html>
#     

# In[82]:


html = """<html>
<head>
    <title>test</title>
</head>
<body>
    <h1>W3C Mission</h1>
    <h2>Principles</h2>
</body>
</html>
    """

from bs4 import BeautifulSoup

output = BeautifulSoup(html, 'html.parser')

print(output.prettify())


# In[83]:


print(output.body.h1.text)
print(output.body.h2.text)


# ## Question 7

# In[114]:


pip install requests


# In[115]:


pip install beautifulsoup4


# In[84]:


from bs4 import BeautifulSoup
import requests
   
link=[]
   
## Function defining
def webdir(url):
       
    req = requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
       
    for j in soup.find_all("a"):
          
        site = j.attrs['href']
           
        if site.startswith("/"):
            url = url+site
               
            if url not in  link:
                link.append(url) 
                print(url)
                scrape(url)
   

if __name__ =="__main__":
   
    ## Defining website
    url="http://example.webscraping.com//"
   
   
    ## Function calling
    webdir(url)


# ## Question 9

# In[85]:



# Defining list of words
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# Printing the list of words in uppercase 
print([i.upper() for i in words])

# Printing the list of words in lowercase 
print([j.lower() for j in words])

# Printing the length of list of words 
print([len(k) for k in words])

# Printing the list containing a list for every word of list words, where each list contains the word in uppercase and lowercase and thelength of the word
print([[i.upper() for i in words], [j.lower() for j in words], [len(k) for k in words]])

# Printing list of words in list words containing 4 or more characters  
output = [i for i in words if len(i) >=4]
print(output)


# In[ ]:




