
add = lambda num1, num2: num1 + num2

#2
even = lambda n: n % 2 == 0

#3
absolute = lambda a, b: abs(a-b)

#4
max_of_three = lambda a, b, c: max(a, b, c)

#5
grade_pass = lambda score: "pass" if score >= 60 else "fail"

#6
def square(x):
    return x * x

#7
def full_name(first, last):
    return f"{first} {last}"

#8
def is_positive(n):
    return n > 0

#9
def discount_price(price):
    if price > 100:
        return price * 0.9
    else:
        return price
    
#10
def last_char(s):
    return s[-1]

#11
num_add_10 = lambda n: n + 10

#12
square1 = lambda width, heigth: width * heigth

#13
age = lambda age: 18 < age < 65

#14
string = lambda string: (string.upper(), len(string))

#15
check_num = lambda num: abs(num) if num < 0 else num * num

#16
score = lambda score: "a" if score >= 90 else "b" if score >= 80 else "c" if score >= 70 else "f"

#17
small_num = lambda a, b, c: min(a, b, c) - max(a, b, c)

#18
divide = lambda a, b: a / b if b > 0 else "Cannot divide"

#19
nums = lambda n: "fizz" if n % 3 == 0 else "buzz" if n % 5 == 0 else "fizzbuzz" if (n % 3 == 0 and n % 5 == 0) else n

#20
discount = lambda price, is_member: price * 0.85 if is_member else price * 0.95 if price > 200 else price