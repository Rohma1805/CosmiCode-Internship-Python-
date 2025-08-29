#Task4:

from collections import Counter, defaultdict, OrderedDict, deque, namedtuple

#1.Counter Example:
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_count = Counter(fruits)
print("Fruit Count:", fruit_count)

#2.defaultdict Example:
student_grades = defaultdict(int)
student_grades["Haider"] = 85
student_grades["Usman"] = 90
print("\n Grades:", dict(student_grades))
print("Missing student grade:", student_grades["Rohma"])

#3.OrderedDict Example:
ordered = OrderedDict()
ordered["Math"] = 95
ordered["Physics"] = 88
ordered["Chemistry"] = 92
print("\nOrderedDict:", ordered)

#4.deque Example:
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
print("\nDeque after operations:", dq)

#5.namedtuple Example:
Person = namedtuple("Person", "name age city")
p1 = Person("Rohma", 21, "Lahore")
print("\n Namedtuple Person:", p1)
print("Name:", p1.name, " | Age:", p1.age, " | City:", p1.city)
