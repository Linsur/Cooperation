# Python

### Hello world

```python
print("hello world!")
```



### Types

```python
a = 28  int
b = 1.5 float
c = "hello" str
d = True  bool
e = None  NoneType
```



### Name.py

```python
name = input("Name:")
print("hello" + name)
print(f"hello,{name}")
```



### Conditions.py

```python
# n = input("Number:") 此时会默认返回字符串，因此整个程序无法运行

n = int(input("Number:")) # 若想解决，需要限制返回值类型  

if n > 0:
	print("n is positive")
elif:
    print("n is negative")
else:
    print("n is zero")
```



### Sequences.py

```python
name = "Harry"

print(name[0]) #该索引将打印字符串的第一个字符
```



```python
names = ["Harry","Ron","Hermione"]

print(names[0]) #该索引将打印数组中的第一个字符串
```



### Data Structures

1. **list**  - sequence of mutable values  列表
2. **tuple**  - sequence of immutable values   元组
3. **set**  - collection of unique values  唯一值集合
4. **dict**  - collection of key-value pairs  键值对字典



### List.py

```python
# Define a list of names
names = ["Harry","Ron","Hermione","Ginny"]

names.append("Draco")

# sort list
names.sort()

print(names)
```



### Sets.py

```python
# Create an empty set
s = set()
# add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(4)

# Delete elements
s.remove(2)

print(f"The set has {len(s)} elements.")
```



### Loops.py

```python
for i in [0, 1, 2, 3, 4, 5]:
	print(i)
```

可以使用range函数简化上述代码

```python
for i in range(6):
	print(i)
```



现在来回顾上面的例子

```python
name = "Harry"
for character in name:
	print(character)
```



```python
names = ['Harry','Ron','Hermione']

for name in names:
	print(name)
```



### Dictionaries.py

```python
houses = {"Harry": "Gryffindor": "Draco": "Slytherin"}

houses["Hermione"] = "Gryffindor"

print(houses["Hermione"])
```



### Functions.py

```python
def square(x):
	return x * x
	
for i in range(10):
	print(f"The square of {i} is {square(i)}.")
```



```python
def square(x):
	return x * x
```

```python
from functions import square #导入functions.py中的square模块

# import functions 导入functions.py中的所有模块

for i in range(10):
	print(f"The square of {i} is {square(i)}.")
```



### Classes.py

```python
class Point():
    def __init__(self, input1, input2): # self 代表点本身
        self.x = input1   # 设置属性把数据储存在.x中
        self.y = input2
     
p = Point(2, 8)
print(p.x)
print(p.y)
```



```python
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
		return self.capacity - len(self.passengers)	

flight = Flight(3)

people = ["Harry","Ron","Hermione","Ginny"]
for person in people:
    if flight.add_passengers(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")
```



### Decorators.py

```python
def announce(f): # 装饰器，可应用于仅当用户登陆后可使用某些功能
    def wrapper():  # 包装函数
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")
    
hello()
        
```



### Lambda.py

```python
people = [
	{"name": "Harry", "house": "Gryffindor"},
	{"name": "Cho", "house": "Ravenclaw"},
	{"name": "Draco", "house": "Slytherin"}
]

# people.sort() 简单的sort函数无法比较字典类型

# Define function to sort
# def f(person):
#    return person["name"] #or house

people.sort(key=lambda person: person["name"])

print(people)
```



### Exception.py

```python
import sys

try:
    x = int(input("x:"))
    y = int(input("y:"))
except ValueError:
    print("Error: Invald input.")
    sys.exit(1)
    
try:
	result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)
    
print(f"{x} / {y} = {result}")
```

