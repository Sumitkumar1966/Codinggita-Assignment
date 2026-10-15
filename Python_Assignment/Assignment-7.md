<img width="1061" height="1599" alt="image" src="https://github.com/user-attachments/assets/2da08b4d-6538-46e5-9cf3-5c9c28e6b158" /><img width="1080" height="1569" alt="image" src="https://github.com/user-attachments/assets/a1fe7ca1-e8b1-4080-afea-327a6ea88a79" /><img width="1080" height="1569" alt="image" src="https://github.com/user-attachments/assets/d18cd457-6ed0-4fb0-ae6c-ddf77436c7cf" /><img width="1080" height="1298" alt="image" src="https://github.com/user-attachments/assets/82575dc4-faf5-42d6-93cb-78ade87f62a0" /><img width="1080" height="1569" alt="image" src="https://github.com/user-attachments/assets/b2aeb4b9-dcb3-43ef-8340-b5c6082ea0a4" /><img width="1080" height="1569" alt="image" src="https://github.com/user-attachments/assets/59ebca12-0363-4f58-b462-abe0aad73e4f" /><img width="1080" height="1569" alt="image" src="https://github.com/user-attachments/assets/a6bbc441-29c6-4c12-9533-4a89761d9df8" /># Assignment-7

**Topic:** Python While Loop

**Instruction:** Predict the exact output of each program before running it. Pay attention to the condition, statement order, indentation, and variable updates. Write **No output** if nothing is printed and **Infinite loop** if the program does not terminate.

------------------------------------------------------------------------

## Type 1: Output Guessing

### Level 1: Understand the Basic Flow

### Q1. Simple Counting

``` python
i = 1

while i <= 4:
    print(i)
    i += 1
```

**Predicted output:**

``` text
```

### Q2. Counting by Two

``` python
n = 2

while n <= 8:
    print(n, end=" ")
    n += 2
```

**Predicted output:**

``` text
```

### Q3. Reverse Counting

``` python
x = 5

while x >= 1:
    print(x, end=" ")
    x -= 1
```

**Predicted output:**

``` text
```

### Q4. The Condition Is Initially False

``` python
count = 7

while count < 5:
    print("Hello")
    count += 1

print("Finished")
```

**Predicted output:**

``` text
```

------------------------------------------------------------------------

### Level 2: Track the Order of Statements

### Q5. Update Before Printing

``` python
i = 1

while i <= 4:
    i += 1
    print(i, end=" ")
```

**Predicted output:**

``` text
```

### Q6. Print After the Loop

``` python
n = 1

while n <= 3:
    print(n, end=" ")
    n += 1

print("Done")
```

**Predicted output:**

``` text
```

### Q7. Two Updates in One Iteration

``` python
x = 1

while x < 10:
    print(x, end=" ")
    x += 2
    x += 1
```

**Predicted output:**

``` text
```

### Q8. Change the Variable Before Checking Again

``` python
value = 10

while value > 0:
    value -= 3
    print(value, end=" ")
```

**Predicted output:**

``` text
```

------------------------------------------------------------------------

### Level 3: Arithmetic and Accumulation

### Q9. Add the Counter Values

``` python
i = 1
total = 0

while i <= 4:
    total += i
    i += 1

print(total)
```

**Predicted output:**

``` text
```

### Q10. Multiply During Each Iteration

``` python
n = 1
result = 1

while n <= 4:
    result *= 2
    n += 1

print(result)
```

**Predicted output:**

``` text
```

### Q11. Use the Remainder Operator

``` python
n = 11

while n > 0:
    print(n % 3, end=" ")
    n -= 4
```

**Predicted output:**

``` text
```

### Q12. Integer Division

``` python
number = 583

while number > 0:
    print(number // 10, end=" ")
    number //= 10
```

**Predicted output:**

``` text
```

------------------------------------------------------------------------

### Level 4: Conditions and Logical Thinking

### Q13. Print Only When a Condition Is True

``` python
i = 1

while i <= 6:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
```

**Predicted output:**

``` text
```

### Q14. A Conditional Expression Inside a Loop

``` python
n = 1

while n <= 5:
    print("Even" if n % 2 == 0 else "Odd", end=" ")
    n += 1
```

**Predicted output:**

``` text
```

### Q15. The Condition Changes Inside the Loop

``` python
x = 1

while x < 10:
    print(x, end=" ")
    x *= 2
```

**Predicted output:**

``` text
```

### Q16. A Tricky Starting Value

``` python
i = 5

while i > 0:
    print(i, end=" ")
    i -= 2

print("Stop:", i)
```

**Predicted output:**

``` text
```

------------------------------------------------------------------------

### Level 5: Strings and Tricky Cases

### Q17. Build a String Repeatedly

``` python
i = 1
result = ""

while i <= 4:
    result += "A"
    print(result)
    i += 1
```

**Predicted output:**

``` text
```

### Q18. A String Variable Changes Each Time

``` python
word = "PY"

while len(word) < 6:
    print(word)
    word += "T"

print(word)
```

**Predicted output:**

``` text
```

### Q19. Does the Loop Run at All?

``` python
x = 3

while x > 10:
    print("Inside")
    x += 1

print(x)
```

**Predicted output:**

``` text
```

### Q20. Find the Problem

``` python
i = 1

while i <= 4:
    print(i, end=" ")
    i -= 1

print("Finished")
```

**What happens when this program runs?**

Choose one: - A. It prints `1 2 3 4 Finished` - B. It prints
`1 0 -1 -2 ...` and continues indefinitely - C. It prints nothing - D.
It produces a syntax error

**Your answer and reasoning:**

``` text
```

------------------------------------------------------------------------

### Reflection Questions

After completing the worksheet, answer these questions in your own
words:

1.  Why must a loop variable often be updated inside a `while` loop?
2.  Can a `while` loop execute zero times? Give an example from this
    worksheet.
3.  What is the difference between updating a variable before `print()`
    and after `print()`?
4.  How can you recognize a possible infinite loop by reading the code?
5.  Why should you trace the condition again after every update?


# ========================================================================================================================================================

Answers====>>>>

<img width="1080" height="1569" alt="image" src="https://github.com/user-attachments/assets/c7eacfcd-2b67-4463-9c2a-9b18858a6c25" />

<img width="1080" height="1569" alt="image" src="https://github.com/user-attachments/assets/5ee03e16-4f12-4af1-a24d-5c3d465ca0f2" />

<img width="1080" height="1569" alt="image" src="https://github.com/user-attachments/assets/770a1f29-6894-4f10-a22f-f9eea82d6b0a" />

<img width="1080" height="1405" alt="image" src="https://github.com/user-attachments/assets/b8716654-c510-41ff-a908-ca9cd01e283d" />

<img width="899" height="1599" alt="image" src="https://github.com/user-attachments/assets/5cf52d85-15f9-4716-b90d-199348ab7619" />

<img width="950" height="1482" alt="image" src="https://github.com/user-attachments/assets/b758b509-9be3-4e61-9f2e-c3625f47ea87" />
