#main.py
# naive search Vs binary search

# module
from words import words
import random
import time

# sorting words
words_sorted = sorted(words)

# function: naive search
def NaiveSearch(words, key):
    for i in range(len(words)):
        if key == words[i]:
            return i
    return -1

# function: binary search
def BinarySearch(words, key, start=0, end=len(words)-1):
    min = start
    max = end
    mid = (min + max) // 2

    if words[mid] == key:
        return mid
    elif key < words[mid]:
        return BinarySearch(words, key, min, mid-1)
    else:
        return BinarySearch(words, key, mid+1, max)

if __name__ == '__main__':
    start_time = time.time()
    for word in words_sorted:
        NaiveSearch(words_sorted, word)
    end_time = time.time()
    print("Naive search time: ", end_time - start_time)

    start_time = time.time()
    for word in words_sorted:
        BinarySearch(words_sorted, word)
    end_time = time.time()
    print("Binary search time: ", end_time - start_time)