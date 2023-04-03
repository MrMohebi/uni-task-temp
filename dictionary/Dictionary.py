#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

words = {
    "a": ["abandon", "abroad"],
    "b": ["birth", "break"],
    "c": ["ceb"]
}
while True:
    user = input("enter word")
    if user != "exit":
        last_char = user[-1]
        if last_char in words:
            selector = random.randint(0, len(words[last_char]) - 1)
            print(words[last_char][selector])
