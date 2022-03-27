#!/usr/bin/env python3
import sys

from problem5_impl import *

if __name__ == "__main__":
    print("Enter upper bound integer value to find all prime numbers that are less or equal than this one> ")
    try:
        n = int(input())
    except ValueError:
        print(f"You provided not an integer", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print(f"Keyboard interrupt happened", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print(f"EOF reached", file=sys.stderr)
        sys.exit(1)

    print(*prime_nums(n), sep=" ")
