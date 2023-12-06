#! /usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
if n % 10 == 1 and (n % 100 < 11 or n % 100 > 19):
    print(n, "программист")
elif n % 10 in (2, 3, 4) and (n % 100 < 12 or n % 100 > 14):
    print(n, "программиста")
else:
    print(n, "программистов")