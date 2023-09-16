#!/usr/bin/env python3

def q1_sum(list):
    total = 0
    for i in list:
        if int(i) % 2 == 0:
            total += int(i)
    print(total)
    return total

def move_vow(string):
    vowels = "aeiouAEIOU"
    string_vowels = ""
    string_consonants = ""
    for letter in string:
        if letter in vowels:
             string_vowels += letter
        else:
            string_consonants += letter
    print(string_vowels + string_consonants)
    return string_vowels + string_consonants

class Memories:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def remember(self, attribute):
        try:
            attribute_value = getattr(self, attribute)
            print(attribute_value)
            return attribute_value
        except AttributeError:
            print(False)
            return False

class Test:
    def __init__(self, subject_name, correct_answers, pasing_mark):
        self.subject_name = subject_name
        self.correct_answers = correct_answers
        self.pasing_mark = pasing_mark
    
paper1 = Test('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Test('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Test('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

class Student:
    def __init__(self, name):
        self.name = name
    def take_test(self, test, answers):
        pass_mark = int(test.pasing_mark[0:-1])
        percent_per_q = 100 / len(test.correct_answers)
        counter = 0
        i = 0
        while i < len(test.correct_answers):
            if answers[i] == test.correct_answers[i]:
                counter += 1
            else: 
                pass
            i += 1
        percent = round(counter * percent_per_q, 1)
        if percent >= pass_mark:
            message = f"{self.name} passed the {test.subject_name} test with the score {percent}%"
            print(message)
            return message
        else:
            message = f"{self.name} failed the {test.subject_name} test!"
            print(message)
            return message
"""
stu1 = Student('Tom')
stu1.take_test(paper3, ['1D', '2C', '3C', '4B', '5D', '6C', '7B'])
stu1.take_test(paper2, ['1C', '2C', '3D', '4A'])
stu2 = Student('John')
stu2.take_test(paper3, ['1B', '2C', '3A', '4A', '5B', '6C', '7A'])
stu2.take_test(paper1, ['1B', '2C', '3A', '4A', '5B']) 
"""

def histogram(list, symbol):
    histogram = ""
    for i in list:
        entry = ""
        entry = i * symbol + "\n"
        histogram += entry
    print(histogram)
    return histogram

def filter_star(dict, num):
    keys = []
    for i in dict:
        if len(dict[i]) == num:
            keys.append(i)
    if len(keys) > 0:
        for i in keys:
            print(f"{i}: {dict[i]}")
    else:
        print("No result found!")

