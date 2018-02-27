
# coding: utf-8

# In[19]:

#Assignment 3.3
#Implement a function longestWord() that takes a list of words and returns the longest one.
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
        word_len.sort()
        #print(word_len)
    return word_len[-1][1]

print(find_longest_word(["Science", "Hello", "World", "!", "Python", "Data"]))



# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



