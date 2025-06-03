# 1. Circle Class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# 2. Person Class
from datetime import datetime
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d")

    def age(self):
        today = datetime.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))


# 3. Calculator Class
class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return a / b if b != 0 else "Division by zero"


# 4. Shape and Subclasses
class Shape:
    def area(self): pass
    def perimeter(self): pass

class CircleShape(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius ** 2
    def perimeter(self): return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
    def perimeter(self): return 4 * self.side


# 5. Binary Search Tree Class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BST:
    def __init__(self): self.root = None

    def insert(self, key):
        def _insert(root, key):
            if root is None: return Node(key)
            if key < root.key: root.left = _insert(root.left, key)
            else: root.right = _insert(root.right, key)
            return root
        self.root = _insert(self.root, key)

    def search(self, key):
        def _search(root, key):
            if root is None or root.key == key: return root
            if key < root.key: return _search(root.left, key)
            return _search(root.right, key)
        return _search(self.root, key)


# 6. Stack Data Structure
class Stack:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None


# 7. Linked List Data Structure
class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self): self.head = None

    def insert(self, data):
        new_node = LLNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp: prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")


# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self): self.items = {}

    def add_item(self, item, price): self.items[item] = price
    def remove_item(self, item): self.items.pop(item, None)
    def total(self): return sum(self.items.values())


# 9. Stack with Display
class StackWithDisplay:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def display(self): print(self.items)


# 10. Queue Data Structure
class Queue:
    def __init__(self): self.items = []
    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.pop(0) if self.items else None


# 11. Bank Class
class Bank:
    def __init__(self): self.accounts = {}

    def create_account(self, name, balance=0):
        self.accounts[name] = balance

    def deposit(self, name, amount):
        if name in self.accounts: self.accounts[name] += amount

    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount
            return True
        return False

    def get_balance(self, name):
        return self.accounts.get(name, "Account not found")
