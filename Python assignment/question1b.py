
# Write a function that takes a string and returns the dictionary with each character as key and its count as value.

dic={}
word1 = input('Enter a word:')
#using set and count
def func(word):
    split_word = set(word)
    for i in split_word:
        dic[i]=word.count(i)
    return sorted(dic.items())
print(func(word1))

#using dictionary
dic1={}
def func1(word):
    for keys in word:
        dic1[keys] = dic1.get(keys,0)+1
    return dic1
print(func1(word1))

#using collection counter
from collections import Counter
def func2(word):
    c = Counter(word)
    return dict(c)
print(func2(word1))


