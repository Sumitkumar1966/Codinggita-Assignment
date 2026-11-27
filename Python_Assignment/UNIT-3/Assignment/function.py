## Section A — Basic Function Practice

### Q1. Display a Welcome Message

**Task**

Create a function named `display_welcome()` that displays the following message:

```text
================================
   Welcome to Python Programming
       Let's learn Functions!
================================
```

Call the function three times.

**Test your program**

| Test | Expected behaviour |
|---|---|
| 1 | The welcome message is displayed. |
| 2 | The same message is displayed again when the function is called a second time. |
| 3 | The same message is displayed a third time. |

---
# ==============================================================================================
  def display_welcome():
    print("==============================")
    print("   Welcome to Python Programming")
    print("       Let's learn Functions!")
    print("==============================")

display_welcome()
display_welcome()
display_welcome()

### Q2. Student Introduction Card

**Task**

Create a function named `display_student_card(name, age, course)`.

The function should display the student's details in the following format:

**Sample function call**

```python
display_student_card("Rahul", 18, "B.Tech")
```

**Expected output**

```text
+--------------------------------+
|         STUDENT CARD           |
+--------------------------------+
| Name  : Rahul                  |
| Age   : 18                     |
| Course: B.Tech                 |
+--------------------------------+
```

Call the function for at least three students.

**Test cases**

| Name | Age | Course |
|---|---:|---|
| Rahul | 18 | B.Tech |
| Priya | 19 | BCA |
| Aman | 20 | B.Sc |

---

def display_student_card(name, age, course):
    print("+--------------------------------+")
    print("|         STUDENT CARD           |")
    print("+--------------------------------+")
    print("| Name  :", name)
    print("| Age   :", age)
    print("| Course:", course)
    print("+--------------------------------+")

display_student_card("Rahul", 18, "B.Tech")
display_student_card("Priya", 19, "BCA")
display_student_card("Aman", 20, "B.Sc")

### Q3. Square, Cube, and Double

**Task**

Create three separate functions:

- `calculate_square(number)`
- `calculate_cube(number)`
- `calculate_double(number)`

Each function should calculate and display its respective result.

**Sample function calls**

```python
calculate_square(4)
calculate_cube(4)
calculate_double(4)
```

**Expected output**

```text
Square: 16
Cube: 64
Double: 8
```

**Test cases**

| Input | Square | Cube | Double |
|---:|---:|---:|---:|
| 2 | 4 | 8 | 4 |
| 4 | 16 | 64 | 8 |
| 5 | 25 | 125 | 10 |

---
==>
def calculate_square(number):
    print("Square:", number * number)

def calculate_cube(number):
    print("Cube:", number * number * number)

def calculate_double(number):
    print("Double:", number * 2)

calculate_square(4)
calculate_cube(4)
calculate_double(4)
  ### Q4. Simple Interest Calculator

**Task**

Create a function named `calculate_simple_interest(principal, rate, time)`.

Calculate simple interest using:

\[
SI = \frac{P \times R \times T}{100}
\]

Also calculate the final amount:

\[
Amount = Principal + SI
\]

Display both values.

**Sample function call**

```python
calculate_simple_interest(5000, 5, 2)
```

**Expected output**

```text
Principal: 5000
Rate: 5%
Time: 2 years
Simple Interest: 500
Total Amount: 5500
```

**Test cases**

| Principal | Rate | Time |
|---:|---:|---:|
| 5000 | 5 | 2 |
| 10000 | 7 | 3 |
| 2500 | 4 | 1 |

---
def calculate_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    amount = principal + si

    print("Principal:", principal)
    print("Rate:", rate, "%")
    print("Time:", time, "years")
    print("Simple Interest:", si)
    print("Total Amount:", amount)

calculate_simple_interest(5000, 5, 2)
  # =========================================================================================================

  ### Q5. Even or Odd Checker

**Task**

Create a function named `check_even_odd(number)`.

The function should display whether the given number is even or odd.

**Sample function calls**

```python
check_even_odd(12)
check_even_odd(7)
```

**Expected output**

```text
12 is an Even number.
7 is an Odd number.
```

**Test cases**

| Input | Expected output |
|---:|---|
| 12 | Even |
| 7 | Odd |
| 0 | Even |
| -5 | Odd |

---

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is an Even number.")
    else:
        print(number, "is an Odd number.")

check_even_odd(12)
check_even_odd(7)
check_even_odd(0)
check_even_odd(-5)
# ========================================================================================
## Section B — Parameters, Arguments, and Return Values

### Q6. Find the Larger Number

**Task**

Create a function named `find_largest(number_1, number_2)` that returns the larger of the two numbers.

Outside the function:

1. Call the function.
2. Store the returned value in a variable.
3. Display the result.

Do not print the answer from inside the function.

**Sample**

```python
result = find_largest(25, 40)
print("Largest number:", result)
```

**Expected output**

```text
Largest number: 40
```

**Test cases**

| Number 1 | Number 2 | Expected result |
|---:|---:|---:|
| 25 | 40 | 40 |
| 90 | 15 | 90 |
| 12 | 12 | 12 |
| -5 | -2 | -2 |

---

### Q7. Temperature Converter

**Task**

Create two functions:

- `celsius_to_fahrenheit(celsius)` — returns Fahrenheit.
- `fahrenheit_to_celsius(fahrenheit)` — returns Celsius.

Use these formulas:

\[
F = \frac{9}{5} \times C + 32
\]

\[
C = \frac{5}{9} \times (F - 32)
\]

Display the returned values outside the functions.

**Sample**

```python
fahrenheit = celsius_to_fahrenheit(0)
print(fahrenheit)

celsius = fahrenheit_to_celsius(98.6)
print(celsius)
```

**Expected output**

```text
32.0
37.0
```

**Test cases**

| Celsius | Fahrenheit |
|---:|---:|
| 0 | 32 |
| 25 | 77 |
| 100 | 212 |

| Fahrenheit | Celsius |
|---:|---:|
| 32 | 0 |
| 68 | 20 |
| 98.6 | 37 |

---

### Q8. Understand the Difference Between print() and return

**Given code**

Study the following functions:

```python
def calculate_sum_1(a, b):
    print(a + b)


def calculate_sum_2(a, b):
    return a + b
```

**Task**

1. Call both functions with the values `10` and `20`.
2. Store the result of each function call in a separate variable.
3. Display both variables.
4. Predict the output before running the code.

**Expected output structure**

```text
30
30
Result from first function: None
Result from second function: 30
```

**Answer these questions in comments:**

- Which function returns a value?
- Why does the first variable contain `None`?
- Can the value displayed by `print()` be directly stored as the function's return value?

**Additional test cases**

Repeat the experiment with:

| A | B |
|---:|---:|
| 5 | 7 |
| 100 | 250 |

---

### Q9. Total Marks and Percentage

**Task**

Create a function named:

```python
calculate_result(mark_1, mark_2, mark_3, mark_4, mark_5)
```

The function should:

1. Calculate the total marks.
2. Calculate the percentage, assuming every subject is out of 100.
3. Return both the total marks and percentage.

Outside the function, receive both returned values in separate variables and display them.

**Sample**

```python
total, percentage = calculate_result(75, 80, 65, 90, 70)
```

**Expected output**

```text
Total Marks: 380
Percentage: 76.0%
```

**Test cases**

| Subject 1 | Subject 2 | Subject 3 | Subject 4 | Subject 5 |
|---:|---:|---:|---:|---:|
| 75 | 80 | 65 | 90 | 70 |
| 50 | 60 | 55 | 65 | 70 |
| 100 | 95 | 90 | 85 | 80 |

---

### Q10. Rectangle Area and Perimeter

**Task**

Create a function named `rectangle_details(length, breadth)`.

Calculate:

- Area = Length × Breadth
- Perimeter = 2 × (Length + Breadth)

Return both values from the function. Store them in two separate variables outside the function and display them.

**Sample**

```python
area, perimeter = rectangle_details(10, 5)
```

**Expected output**

```text
Area: 50
Perimeter: 30
```

**Test cases**

| Length | Breadth | Area | Perimeter |
|---:|---:|---:|---:|
| 10 | 5 | 50 | 30 |
| 8 | 4 | 32 | 24 |
| 7 | 7 | 49 | 28 |

---
# ==============================================================================================================
  def find_largest(number_1, number_2):
    if number_1 >= number_2:
        return number_1
    else:
        return number_2

result = find_largest(25, 40)
print("Largest number:", result)

# Q7
def celsius_to_fahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit = celsius_to_fahrenheit(0)
print(fahrenheit)

celsius = fahrenheit_to_celsius(98.6)
print(celsius)
# Q8
def calculate_sum_1(a, b):
    print(a + b)

def calculate_sum_2(a, b):
    return a + b

result_1 = calculate_sum_1(10, 20)
result_2 = calculate_sum_2(10, 20)

print("Result from first function:", result_1)
print("Result from second function:", result_2)

# The second function returns a value.
# The first variable contains None because the function
# only prints the result and does not return anything.
# The value displayed by print() cannot be directly
# stored as the function's return value.

def calculate_result(mark_1, mark_2, mark_3, mark_4, mark_5):
    total = mark_1 + mark_2 + mark_3 + mark_4 + mark_5
    percentage = total / 500 * 100
    return total, percentage

total, percentage = calculate_result(75, 80, 65, 90, 70)

print("Total Marks:", total)
print("Percentage:", percentage, "%")

# Q10
def rectangle_details(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

area, perimeter = rectangle_details(10, 5)

print("Area:", area)
print("Perimeter:", perimeter)
# =================================================================================================
## Section C — Default and Keyword Arguments

### Q11. Personalized Greeting

**Task**

Create a function:

```python
greet_user(name, message="Welcome to Python!")
```

The function should display the user's name and greeting message.

Call the function in all three ways:

**A. Pass both arguments**

```python
greet_user("Rahul", "Good Morning!")
```

**B. Use the default message**

```python
greet_user("Priya")
```

**C. Pass the message using a keyword argument**

```python
greet_user("Aman", message="Keep Learning!")
```

**Expected output**

```text
Hello Rahul!
Good Morning!

Hello Priya!
Welcome to Python!

Hello Aman!
Keep Learning!
```

**Test cases:** Use the three function calls shown above and add one more name of your choice.

---

### Q12. Electricity Bill Calculator

**Task**

Create a function named:

```python
calculate_electricity_bill(units, rate=7)
```

Calculate the bill using:

```text
Bill = Units × Rate
```

The default rate is ₹7 per unit. Return the bill and display it outside the function.

Call the function:

1. By passing only units.
2. By passing units and a different rate.
3. By using keyword arguments.

**Sample calls**

```python
bill_1 = calculate_electricity_bill(100)
bill_2 = calculate_electricity_bill(100, 8)
bill_3 = calculate_electricity_bill(rate=6, units=100)
```

**Expected output**

```text
Bill 1: 700
Bill 2: 800
Bill 3: 600
```

**Test cases**

| Units | Rate | Expected bill |
|---:|---:|---:|
| 100 | Default (7) | 700 |
| 150 | 8 | 1200 |
| 200 | 6 | 1200 |

---

### Q13. Employee Salary Calculator

**Task**

Create a function:

```python
calculate_salary(basic_salary, bonus=2000, deduction=500)
```

Calculate the final salary using:

```text
Final Salary = Basic Salary + Bonus - Deduction
```

Return the final salary.

Call the function in these four ways:

1. Pass only the basic salary.
2. Pass basic salary and bonus.
3. Pass all three arguments positionally.
4. Pass the arguments using keyword names.

**Sample calls**

```python
calculate_salary(25000)
calculate_salary(25000, 3000)
calculate_salary(25000, 3000, 1000)
calculate_salary(basic_salary=25000, deduction=800, bonus=4000)
```

**Expected results**

| Function call | Expected salary |
|---|---:|
| `calculate_salary(25000)` | 26500 |
| `calculate_salary(25000, 3000)` | 27500 |
| `calculate_salary(25000, 3000, 1000)` | 27000 |
| `calculate_salary(basic_salary=25000, deduction=800, bonus=4000)` | 28200 |

**Think and answer:** Why must parameters with default values be placed after parameters without default values?

---
  # =======================================================================================
# Q11

def greet_user(name, message="Welcome to Python!"):
    print("Hello", name + "!")
    print(message)

greet_user("Rahul", "Good Morning!")
greet_user("Priya")
greet_user("Aman", message="Keep Learning!")
greet_user("Neha")
# Q12
def calculate_electricity_bill(units, rate=7):
    bill = units * rate
    return bill

bill_1 = calculate_electricity_bill(100)
bill_2 = calculate_electricity_bill(100, 8)
bill_3 = calculate_electricity_bill(rate=6, units=100)

print("Bill 1:", bill_1)
print("Bill 2:", bill_2)
print("Bill 3:", bill_3)
# Q13
def calculate_salary(basic_salary, bonus=2000, deduction=500):
    final_salary = basic_salary + bonus - deduction
    return final_salary

salary_1 = calculate_salary(25000)
salary_2 = calculate_salary(25000, 3000)
salary_3 = calculate_salary(25000, 3000, 1000)
salary_4 = calculate_salary(basic_salary=25000, deduction=800, bonus=4000)

print(salary_1)
print(salary_2)
print(salary_3)
print(salary_4)
# Q14




