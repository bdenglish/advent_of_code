from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys

def main():
    fin = open("input_day_6", "r")
    blocks = fin.read().split("\n\n")
    part1 = 0
    for block in blocks:
        c = Counter(block)
        part1 += len(c)
        if '\n' in c:
            part1 -= 1

    part2 = 0
    answer = []
    for block in blocks:
        x = len(block.split())
        c = Counter(block)
        part2 += sum(v == x for _, v in c.items())
        answer.append(sum(v == x for _, v in c.items()))
        if c['\n'] == x:
            part2 -= 1

    print(part1)
    print(part2)
    print(answer)


if __name__ == "__main__":
    main()