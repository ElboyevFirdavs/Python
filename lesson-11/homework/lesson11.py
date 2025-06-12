1.
# 1. Virtual muhit yaratish
python -m venv venv

# 2. Virtual muhitni aktivlashtirish
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Paketlarni o‘rnatish
pip install numpy pandas

2.
# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# string_utils.py

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


3.
geometry/
│
├── __init__.py
└── circle.py

# geometry/circle.py

import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius

# geometry/__init__.py

from .circle import calculate_area, calculate_circumference


file_operations/
│
├── __init__.py
├── file_reader.py
└── file_writer.py


# file_operations/file_reader.py

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


# file_operations/file_writer.py

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)


# file_operations/__init__.py

from .file_reader import read_file
from .file_writer import write_file


4.
# main.py

from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

# Math operations
print("Add:", add(3, 4))
print("Divide:", divide(10, 2))

# String utils
print("Reverse:", reverse_string("Python"))
print("Vowels:", count_vowels("OpenAI"))

# Geometry
print("Circle area (r=5):", calculate_area(5))
print("Circle circumference (r=5):", calculate_circumference(5))

# File operations
write_file("sample.txt", "Hello, world!")
print("Read from file:", read_file("sample.txt"))

