#!/bin/python3

import os


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = list(filter(lambda x: s <= x and x <= t, map(lambda x: a + x, apples)))
    oranges = list(filter(lambda x: s <= x and x <= t, map(lambda x: b + x, oranges)))

    print(len(apples))
    print(len(oranges))


if __name__ == "__main__":
    st = input().split()

    s = int(st[0])
    t = int(st[1])

    ab = input().split()

    a = int(ab[0])
    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
