#!/usr/bin/python

def print_full_name(a, b):
    start_s = "Hello "
    end_s = "! You just delved into python."
    final_s = start_s + a + " " + b + end_s
    print(final_s)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
