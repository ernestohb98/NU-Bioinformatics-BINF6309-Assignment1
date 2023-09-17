#!/usr/bin/env python
#hello_you.py
import sys
def hello_name(x="you"):
    print(f'Hello, {x}!')

if __name__ == "__main__":
    try:
        hello_name(sys.argv[1])
    except IndexError:
        hello_name()