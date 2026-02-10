#1
numbers = [1, 2, 3, 4, 5]
result1 = []
for n in numbers:
    result1.append(n * n)
print(result1)

result2 = [n*n for n in numbers]


#2
nums = [3, 10, 15, 20, 25, 30]
evens1 = []
for n in nums:
    if n % 2 == 0:
        evens1.append(n)
print(evens1)

evens2 = [n for n in nums if n % 2 == 0]


#3
names = ["dan", "sara", "noa"]
upper_names = []
for name in names:
    upper_names.append(name.upper())
print(upper_names)

upper_names2 = [name.upper() for name in names]


#4
nums = [20, 55, 70, 10, 90]
result = []
for n in nums:
    if n > 50:
        result.append(n / 2)
print(result)

result3 = [n/2 for n in nums if n > 50]


#5
words = ["hi", "python", "is", "awesome"]
lengths = []
for w in words:
    if len(w) > 2:
        lengths.append(len(w))
print(lengths)

lengths2 = [w for w in words if len(w) > 2]


#6
squares = [x*x for x in range(10)]

squares2 = []
for x in range(10):
    squares2.append(x*x)


#7
evens = [x for x in range(50) if x % 2 == 0]

evens3 = []
for x in range(50):
    if x % 2 == 0:
        evens3.append(x)


#8
first_letters = [name[0] for name in ["Alice", "Bob", "Charlie"]]

first_letters2 = []
for name in ["Alice", "Bob", "Charlie"]:
    first_letters2.append(name[0])


#9
small_nums = [n for n in nums if n < 100]

small_nums2 = []
for n in nums:
    if n < 100:
        small_nums2.append(n)


#10
modified = [n+5 if n > 10 else n for n in nums]

modified2 = []
for n in nums:
    if n > 10:
        modified2.append(n + 5)
    else:
        modified2.append(n)


#11
multi_by_3 = [n*3 for n in range(1, 21)]


#12
divide_by_5 = [n for n in multi_by_3 if n % 5 == 0]


#13
word_reversed = [w[::-1] for w in ["Alice", "Bob", "Charlie"]]


#14
squares_by3 = [n*n for n in range(1, 31) if n % 3 == 0]


#15
bool_list = [n % 2 == 0 for n in range(1, 16)]
print(bool_list)


#16
temp_list = [n for n in range(0, 50, 2)]
prov_lits = ["HOT" if t > 30 else "COLD" if t < 20 else "OK" for t in temp_list] 
print(prov_lits)


#17
first_names = ["Dan", "Noa", "Yossi"]
last_names = ["Levi", "Cohen", "Mizrahi"]
full_names = [f"{first_names[i]} {last_names[i]}" for i in range(len(first_names))]
print(full_names)


#18
coordinate  = [(x, y) for x in range(3) for y in range(3)]
print(coordinate)


#19
sum_div_by4 = [(x, y) for x in range(1, 11) for y in range(1, 11) if (x + y) % 4 == 0]
print(sum_div_by4)


#20
users = [
{"name": "Dan", "age": 17},
{"name": "Noa", "age": 25},
{"name": "Yossi", "age": 15},
{"name": "Maya", "age": 31}
]

adult_users = [user["name"] for user in users if user["age"] >= 18]
print(adult_users)