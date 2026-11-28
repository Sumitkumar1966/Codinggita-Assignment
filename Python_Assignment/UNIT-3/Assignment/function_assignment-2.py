
# Part A — Output Guessing Questions

**Total: 20 Questions**

For every question:
- Read the code carefully.
- Write the exact output, including line breaks and spaces where relevant.
- If a function returns a value but does not print it, remember that the value will not appear automatically.

## Section 1 — Parameters, Arguments, and Basic Return Values

### Q1. Function Call with Two Arguments

Predict the output:

```python
def show_details(name, age):
    print("Name:", name)
    print("Age:", age)


show_details("Riya", 19)
show_details("Aman", 20)
```

*Hint: Check how each positional argument is assigned to its matching parameter.*

### Q2. Returning a Value

Predict the output:

```python
def calculate_sum(a, b):
    return a + b


answer = calculate_sum(12, 8)
print("Answer:", answer)
print(calculate_sum(5, 7))
```

*Hint: Trace the returned values and notice where each value is printed.*

### Q3. Return Does Not Mean Print

Predict the output:

```python
def multiply(a, b):
    result = a * b
    return result


multiply(4, 5)
print("Function completed")
```

*Hint: A returned value is not displayed unless it is printed or used.*

### Q4. Using a Returned Value in Another Calculation

Predict the output:

```python
def square(number):
    return number * number


result = square(5)
final_result = result + 10

print(result)
print(final_result)
```

*Hint: First calculate the returned square, then use that value in the next expression.*

### Q5. Returning Multiple Values

Predict the output:

```python
def calculate(number):
    return number + 5, number * 2


first, second = calculate(10)

print(first)
print(second)
print(first + second)
```

*Hint: Match the first returned value with the first variable and the second with the second.*

---

## Section 2 — Returning Values and Reusing Them

### Q6. Calling a Function More Than Once

Predict the output:

```python
def get_price(price, quantity):
    return price * quantity


bill_1 = get_price(50, 3)
bill_2 = get_price(20, 4)

print("Bill 1:", bill_1)
print("Bill 2:", bill_2)
print("Total:", bill_1 + bill_2)
```

*Hint: Calculate each function call separately, then add the stored results.*

### Q7. Function Call Inside Another Function Call

Predict the output:

```python
def add(a, b):
    return a + b


def double(number):
    return number * 2


answer = double(add(5, 3))
print(answer)
```

*Hint: Evaluate the inner function call before evaluating the outer function call.*

### Q8. Returning Two Calculated Values

Predict the output:

```python
def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter


a, p = rectangle(6, 4)

print("Area:", a)
print("Perimeter:", p)
```

*Hint: Calculate area and perimeter separately, then match them with the returned variables.*

### Q9. Using the Same Returned Value Twice

Predict the output:

```python
def get_discount(price):
    return price * 10 / 100


discount = get_discount(500)
final_price = 500 - discount

print("Discount:", discount)
print("Final price:", final_price)
print("Double discount:", discount * 2)
```

*Hint: The returned discount is stored once and reused in both later calculations.*

### Q10. Difference Between Print and Return

Predict the output:

```python
def first_function(number):
    print(number * 2)


def second_function(number):
    return number * 2


result_1 = first_function(6)
result_2 = second_function(6)

print("First result:", result_1)
print("Second result:", result_2)
```

*Hint: Compare what each function displays with what each function returns.*

---
# =====================================================================================================================
  # Q1
def show_details(name, age):
    print("Name:", name)
    print("Age:", age)


show_details("Riya", 19)
show_details("Aman", 20)

output===>>>>
Name: Riya
Age: 19
Name: Aman
Age: 20

# Q2
def calculate_sum(a, b):
    return a + b


answer = calculate_sum(12, 8)
print("Answer:", answer)
print(calculate_sum(5, 7))
OUTPUT===>>>|

Answer: 20
12
# Q3
def multiply(a, b):
    result = a * b
    return result


multiply(4, 5)
print("Function completed")

OUTPUT:
Function completed
# Q4
def square(number):
    return number * number


result = square(5)
final_result = result + 10

print(result)
print(final_result)

#25
#35
# Q5

def calculate(number):
    return number + 5, number * 2


first, second = calculate(10)

print(first)
print(second)
print(first + second)

# 15
# 20
# 35

# Q6
def get_price(price, quantity):
    return price * quantity


bill_1 = get_price(50, 3)
bill_2 = get_price(20, 4)

print("Bill 1:", bill_1)
print("Bill 2:", bill_2)
print("Total:", bill_1 + bill_2)

# Bill 1: 150
# Bill 2: 80
# Total: 230


# Q7. Function Call Inside Another Function Call

def add(a, b):
    return a + b


def double(number):
    return number * 2


answer = double(add(5, 3))
print(answer)

# Output:
# 16


# Q8. Returning Two Calculated Values

def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter


a, p = rectangle(6, 4)

print("Area:", a)
print("Perimeter:", p)

# Output:
# Area: 24
# Perimeter: 20


# Q9. Using the Same Returned Value Twice

def get_discount(price):
    return price * 10 / 100


discount = get_discount(500)
final_price = 500 - discount

print("Discount:", discount)
print("Final price:", final_price)
print("Double discount:", discount * 2)

# Output:
# Discount: 50.0
# Final price: 450.0
# Double discount: 100.0


# Q10. Difference Between Print and Return

def first_function(number):
    print(number * 2)


def second_function(number):
    return number * 2


result_1 = first_function(6)
result_2 = second_function(6)

print("First result:", result_1)
print("Second result:", result_2)

# Output:
# 12
# First result: None
# Second result: 12
