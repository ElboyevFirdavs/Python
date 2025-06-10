def insert_underscores(txt):
    result = ""
    i = 0
    while i < len(txt):
        result += txt[i]
        if (i + 1) % 3 == 0 and txt[i] not in 'aeiou' and (i + 1 >= len(txt) or txt[i+1] != '_'):
            result += '_'
        i += 1
    if result.endswith('_'):
        result = result[:-1]
    return result

# Test
print(insert_underscores("hello"))           # hel_lo
print(insert_underscores("assalom"))         # ass_alom
print(insert_underscores("abcabcabcdeabcdefabcdefg"))  # abc_abc_abcd_abcd_abcdef


2. Integer Squares Exercise
n = int(input())
for i in range(n):
    print(i ** 2)


3. Loop-Based Exercises

1.
i = 1
while i <= 10:
    print(i)
    i += 1
2.
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
3.
n = int(input("Enter number: "))
total = sum(range(1, n+1))
print("Sum is:", total)

4.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i)

5.
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 100 < num < 200:
        print(num)

6..
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Total digits:", count)


7.
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
8.
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

13.
num = int(input("Enter a number: "))
fact = 1
for i in range(2, num + 1):
    fact *= i
print(f"{num}! = {fact}")



4. Return Uncommon Elements of Lists

from collections import Counter

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    result = []

    for item in (count1 - count2).elements():
        result.append(item)
    for item in (count2 - count1).elements():
        result.append(item)

    return result

# Test
print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]
































