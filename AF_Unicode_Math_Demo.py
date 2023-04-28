# AF_Unicode_Math_Demo.py
# Demonstrates basic math operations and set operations using Unicode characters as operators
# Revision 0

import random
from quaternions import Quaternion

class CustomSet(set):
    def __str__(self):
        if not self:
            return "∅"
        return super().__str__()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def intersect(a, b):
    return CustomSet(a.intersection(b))

def union(a, b):
    return CustomSet(a.union(b))

def xor(a, b):
    return CustomSet(a.symmetric_difference(b))

# Unicode math operators
unicode_plus = "＋"
unicode_minus = "－"
unicode_times = "×"
unicode_division = "÷"
empty_set = "∅"
unicode_intersection = "∩"
unicode_union = "∪"
unicode_circled_plus = "⊕"
unicode_less_than_equal_greater = "⋚"
unicode_greater_than_equal_less = "⋛"

for _ in range(10):
    a = random.randint(-5, 50)
    b = random.randint(-15, 55)
    c = random.randint(-5, 50)
    d = random.randint(-15, 55)
    set_ab = CustomSet([a, b])
    set_cd = CustomSet([c, d])
    empty = CustomSet()
    print(f"Empty set: {empty_set} = {empty}")
    print(f"{a} {unicode_plus} {b} = {add(a, b)}")
    print(f"{a} {unicode_minus} {b} = {subtract(a, b)}")
    print(f"{a} {unicode_times} {b} = {multiply(a, b)}")
    print(f"{a} {unicode_division} {b} = {divide(a, b)}")
    print(f"{set_ab} {unicode_intersection} {set_cd} = {intersect(set_ab, set_cd)}")
    print(f"{set_ab} {unicode_union} {set_cd} = {union(set_ab, set_cd)}")
    print(f"{set_ab} {unicode_circled_plus} {set_cd} = {xor(set_ab, set_cd)}")

    complex_a = complex(a, random.choice([b, c, d]))
    complex_b = complex(b, random.choice([a, c, d]))
    complex_c = complex(c, random.choice([a, b, d]))
    complex_d = complex(d, random.choice([a, b, c]))
    complex_r = complex(random.choice([a, b, c, d]), random.choice([a, b, c, d]))
    print(f"{complex_r} {unicode_less_than_equal_greater} {complex_a} = {complex_r.imag == complex_a.imag}")
    complex_r = complex(random.choice([a, b, c, d]), random.choice([a, b, c, d]))
    print(f"{complex_r} {unicode_greater_than_equal_less} {complex_b} = {complex_r.imag == complex_b.imag}")
    complex_r = complex(random.choice([a, b, c, d]), random.choice([a, b, c, d]))
    print(f"{complex_r} {unicode_less_than_equal_greater} {complex_c} = {complex_r.imag == complex_c.imag}")
    complex_r = complex(random.choice([a, b, c, d]), random.choice([a, b, c, d]))
    print(f"{complex_r} {unicode_greater_than_equal_less} {complex_d} = {complex_r.imag == complex_d.imag}")

    q_parts1 = [a, b, c, d]
    random.shuffle(q_parts1)
    q1 = Quaternion(*q_parts1)
    q_parts2 = [a, b, c, d]
    random.shuffle(q_parts2)
    q2 = Quaternion(*q_parts2)
    q_parts3 = [random.choice([q_parts1[index], q_parts1[index], q_parts1[index], q_parts2[index]]) for index in (0, 1, 2, 3)]
    q_parts3[0] += random.randint(-2,2)
    q3 = Quaternion(*q_parts3)
    print(f"{q1} {unicode_less_than_equal_greater} {q3} = {q1.vector == q3.vector}")
    q_parts3 = [random.choice([q_parts1[index], q_parts2[index], q_parts2[index], q_parts2[index]]) for index in (0, 1, 2, 3)]
    q_parts3[0] += random.randint(-2,2)
    q3 = Quaternion(*q_parts3)
    print(f"{q3} {unicode_greater_than_equal_less} {q2} = {q3.vector == q2.vector}")

# ToDo: Explore and discuss the use of other Unicode operators.
