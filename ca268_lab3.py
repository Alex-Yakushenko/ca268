#!/usr/bin/env python3

def sum_q1(n):
    if n == 0:
        return 0
    else:
        return n + sum_q1(n - 1)
#print(sum_q1(6))

def reverse_int(n):
    if n < 10:
        return n
    last =  n % 10
    reverse_remaining = reverse_int(n // 10)
    number = f"{last}{reverse_remaining}"
    return number
print(reverse_int(12345))

def reverse_str(message):
    if len(message) == 1:
        return message
    last = message[-1]
    reverse_remaining = reverse_str(message[:-1])
    reversed_message = last + reverse_remaining
    return reversed_message
print(reverse_str("hello there"))

def inverse_list(my_list):
    if len(my_list) == 1:
        return my_list
    last =  my_list[-1]
    reverse_remaining = inverse_list(my_list[:-1])
    reversed_list = [last]
    reversed_list.extend(reverse_remaining)
    return reversed_list
#print(inverse_list([1, 2, 3, 4, 5]))
#print(inverse_list([[1], [2], [3], [4], [5]]))

def multiply(n, times):
    if times == 1:
        return n
    if times < 0:
        changed = True
        times = -times
    else:
        changed = False
    total = n + multiply(n, times - 1)
    if n < 0 and changed:
        total = -total
    return total

#couldn't get my code to work for all test cases
"""
print(multiply(-51, 4))
print(multiply(51, -4))
print(multiply(-51, -4))
print(multiply(51, 4))
"""

def pronic_check(n, x=0):
    if x * (x + 1) == n:
        return True
    if x * (x + 1) > n:
        return False
    return pronic_check(n, x + 1)
#print(pronic_check(110))

def length(message, len=0):
    if message:
        len = 1 + length(message[:-1])
    else:
        return 0
    return len
print(length("hello"))
