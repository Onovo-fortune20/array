#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[11]:


words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}

for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
        
#words is an arrav with element    
#by_letter is empty
#letter is equal to the first character of the first word in the array 
#since it is not in the empty function it will append the word
 #basically its looping through the first letter of each word in the array.


# In[ ]:




