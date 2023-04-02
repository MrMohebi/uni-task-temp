#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
dict = {
    "a" : ["abandon","abroad"],
    "b":["birth","break"],
    "c":["ceb"]
}
while True:
    user = input("enter word")
    if user !="exit":
        last_char = user[-1]
        if last_char in dict:
            selector = random.randint(0, len(dict[last_char])-1)
            print(dict[last_char][selector])

