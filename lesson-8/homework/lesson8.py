1.
try:
    num = int(input("Enter a number: "))
    result = num / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
2.
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("That's not a valid integer!")
3.
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
4.
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    raise TypeError("Inputs must be numbers")
5.
try:
    with open("/root/protected_file.txt", "r") as file:
        content = file.read()
except PermissionError:
    print("Permission denied.")
6.
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index out of range.")
7.
try:
    num = input("Enter a number (press Ctrl+C to interrupt): ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")
8.
try:
    result = 1 / 0
except ArithmeticError:
    print("An arithmetic error occurred.")
9.
try:
    with open("file.txt", encoding="utf-8") as file:
        content = file.read()
except UnicodeDecodeError:
    print("Cannot decode file with UTF-8 encoding.")
10.
try:
    my_list = [1, 2, 3]
    my_list.upper()
except AttributeError:
    print("List object has no attribute 'upper'.")


 File Input/Output Exercises

1.
with open("sample.txt", "r") as file:
    print(file.read())
2.
n = 3
with open("sample.txt") as file:
    for i in range(n):
        print(file.readline(), end="")
3.
with open("sample.txt", "a") as file:
    file.write("\nAppended line.")
with open("sample.txt", "r") as file:
    print(file.read())
4.
n = 3
with open("sample.txt") as file:
    lines = file.readlines()
    print("".join(lines[-n:]))
5.
with open("sample.txt") as file:
    lines = [line.strip() for line in file]
print(lines)
6.
with open("sample.txt") as file:
    content = ""
    for line in file:
        content += line
print(content)
7.
with open("sample.txt") as file:
    arr = file.readlines()
print(arr)
8.
with open("sample.txt") as file:
    words = file.read().split()
    max_len = max(len(word) for word in words)
    print([word for word in words if len(word) == max_len])
9.
with open("sample.txt") as file:
    print("Line count:", sum(1 for _ in file))
10.
from collections import Counter
with open("sample.txt") as file:
    words = file.read().replace(",", "").split()
    freq = Counter(words)
print(freq)
12.
my_list = ["apple", "banana", "cherry"]
with open("output.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")
14.
with open("file1.txt") as f1, open("file2.txt") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())
17.
with open("sample.txt") as file:
    content = file.read().replace("\n", "")
print(content)
21.
import string
letters = string.ascii_lowercase
n = 5  # letters per line
with open("alphabet.txt", "w") as file:
    for i in range(0, len(letters), n):
        file.write(letters[i:i+n] + "\n")





























