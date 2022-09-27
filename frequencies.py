"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if str(item) not in frequencies:
            frequencies[str(item)] = 0
        frequencies[str(item)] += 1   

    return frequencies

# print(frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4']))