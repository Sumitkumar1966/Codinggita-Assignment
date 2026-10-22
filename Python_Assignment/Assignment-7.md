

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


======================================================================================
<pre>
Answers==>>
Q21.

N = int(input())

i = 1
while i <= N:
    print(i)
    i = i + 1

Q22.
    N=5

while N>=1:
    print(N)
    N=N-1

    Q23.

n=10
i=2
while i<=n:
    print(i)
    i=i+2

    Q24.

    n=9
i=1
while i<=9:
    print(i)
    i=i+2

    Q25

    K = 3
N = 15

i = K
while i <= N:
    print(i)
    i = i + K

Q26
    n=10
k=4
i=1
while i<=10:
    print(f"{k}*{i}={k*i}")
    i=i+1

    Q27

    start=2
step=3
i=1
while i<=5:
    print(start)
    start=start+step
    i=i+1


    Q28.
n=5
i=1
sum=0
while i<=5:
    sum=sum+i
    i=i+1
print(sum)
    
Q29

    n=10
i=0
sum=0
while i<=n:
    sum=sum+i
    i=i+2
print(sum)


Q30

    n=7
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+2
print(sum)

Q31.
   price=20
quantity=4
total=0
i=1
while i<=4:
    total=total+price
    i=i+1
print(total)


Q32


    total_saving=25
day=6
total=0
i=1
while i<=day:
    total=total+total_saving
    i=i+1
print(total)

    Q33.

    base=3
power=4
i=1
total=1
while i<=4:
    total=total*base
    i=i+1
print(total)
    
    
Q34

    n=5
i=1
result=1
while i<=n:
    result=result*i
    i=i+1
print(result)

Q35

    start=3
end=7
sum=0
while start<=end:
    sum=sum+start
    start=start+1
print(sum)


    Q36

    n=10
i=2
while n>=i:
    print(n)
    n=n-2

    Q37
    N = 20

while N > 0:
    N = N // 2
    print(N)
    
Q38

    N=11
count=0
while N>=0:
    count=count+1
    N=N-3
    
print(count)

    Q39

    
daily_amount=15
save=20
target=70
count=0
while save<=70:
    count=count+1
    save=save+daily_amount
print(count)

    Q40


    start=20
step=5
while start>=0:
    print(start)
    start=start-step

    Q41
    # n=58321
# count=0
# while n>0:
#     digit=n%10
#     count=count+1
#     n=n//10
# print(count)


# Q42

# n=583
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print(sum)

# Q43

# n=5830
# reverse=0
# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n=n//10
# print(reverse)

# Q44
# n=234
# product=1
# while n>0:
#     digit=n%10
#     product=product*digit
#     n=n//10
# print(product) 

# Q45


# N = 58321

# while N > 0:
#     digit = N % 10
#     print(digit)
#     N = N // 10

# Q46

# N = 58321
# last_digit=N%10

# while N > 0:
#     digit = N % 10
#     N = N // 10
# print(last_digit)
# print(digit)

# q47

# n=583204
# count=0
# while n>0:
#     digit=n%10
#     if digit%2==0:
#         count=count+1
#     n=n//10
# print(count)

# q48

# n=583204
# count=0
# while n>0:
#     digit=n%10
#     if digit%2!=0:
#         count=count+1
#     n=n//10
# print(count)

# Q49

# n=583204
# sum=0
# while n>0:
#     digit=n%10
#     if digit%2==0:
#         sum=sum+digit
#     n=n//10
# print(sum)

# Q50

# n=583204
# largest=0

# while n>0:
#     digit=n%10
#     if digit > largest:
#         largest = digit
#     n=n//10
# print(largest)
      

# Q 51

# n=583204
# smallest=9

# while n>0:
#     digit=n%10
#     if digit < smallest:
#         smallest = digit
#     n=n//10
# print(smallest)


# Q52

# n=123
# y=n

# reverse=0
# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n=n//10
# if reverse==y:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Q 53

# n=505250
# d=5
# count=0
# while n>0:
#     digit=n%10
#     if digit==d:
#         count=count+1
#     n=n//10
# print(count)

# Q 54

# n=77777
# y=n%10
# result="yes"
# while n>0:
#     digit=n%10
    
#     if digit!=y:
#         result="no"
#         break
    
#     n=n//10
# print(result)
  
  
# Q 55

# n=58321
# last=n%10
# sum1=0
# sum2=0
# while n>0:
#     digit=n%10
#     sum2=sum2+digit
#     n=n//10
# sum1=last+digit
# print("first and last digit digit sum:",sum1)
# print("middle digit sum:", sum2-sum1)
    
  
# Q 56
# n=5
# i=1
# fact=1
# while i<=5:
#     fact=fact*i
#     i=i+1
#     print(fact)
    
# Q57

# n=25
# fact=1
# i=1
# while fact<n:
#     i=i+1
#     fact=fact*i
# if fact==n:
#     print("yes")
# else:
#     print("no")  


# Q58

# n=20
# fact=1
# i=0
# while fact*(i+1)<=n:
#     i=i+1
#     fact=fact*i
# print(fact)

# 59

# i = 1

# while i <= 2:
#     j = 1

#     while j <= 3:
#         print(i, j)
#         j += 1

#     i += 1
    
# output 
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3

# q 60

# i = 1

# while i <= 3:
#     j = 1

#     while j <= 2:
#         print(j, end=" ")
#         j += 1

#     print()
#     i += 1
    
# # 1 2 
# 1 2 
# 1 2 


# Q61

# i = 1

# while i <= 3:
#     j = 1

#     while j <= i:
#         print("*", end=" ")
#         j += 1

#     print()
#     i += 1

# output
# * 
# * * 
# * * * 

# Q62
# 123
# 23
# 1
# i = 1

# while i <= 3:
#     j = i

#     while j <= 3:
#         print(j, end=" ")
#         j += 1

#     print()
#     i += 1

# # Q64

# i = 1

# while i <= 2:
#     j = 1

#     while j <= 2:
#         print(i + j)
#         j += 1

#     i += 1

# print("Finished")


# 2
# 3
# 3
# 4
# Finished


# Q65

# i = 1

# while i <= 2:
#     print("A", i)
#     i += 1

# j = 1

# while j <= 3:
#     print("B", j)
#     j += 1
 
# A 1
# A 2
# B 1
# B 2
# B 3   

# Q66


# i = 1
# j = 1

# while i <= 3:
#     while j <= 2:
#         print(i, j)
#         j += 1

#     i += 1

# 1 1
# 1 2


# Q67
# i = 1

# while i <= 3:
#     j = 1

#     while j <= 2:
#         print(i, end="")
#         j += 1

#     print()
#     i += 2
    
# 11
# 33

# Q68


# i = 1

# while i <= 3:
#     j = 1

#     while j < i:
#         print(j, end=" ")
#         j += 1

#     print("X")
#     i += 1

# X
# 1 X
# 1 2 X

# Q69


# i = 1

# while i <= 3:
#     j = 1

#     while j <= 4:
#         if j == 3:
#             break

#         print(i, j)
#         j += 1

#     i += 1
# # 1 1
# # 1 2
# # 2 1
# # 22
# # 31
# # 32

# Q 70


# i = 1

# while i <= 2:
#     j = 1

#     while j <= 4:
#         print(j, end=" ")

#         if j == 2:
#             break

#         j += 1

#     print("|")
#     i += 1
    
# 1 2 |
# 1 2 |

# Q71
# i = 1

# while i <= 2:
#     j = 1

#     while j <= 2:
#         if j == 5:
#             break

#         print(i, j)
#         j += 1

#     i += 1

# 1 1
# 1 2
# 2 1
# 2 2

# Q72

# i = 1

# while i <= 3:
#     j = 1

#     while j <= 3:
#         if j == 2:
#             break

#         print(i, j)
#         j += 1

#     print("Next row")
#     i += 1

# 1 1
# Next row
# 2 1
# Next row
# 3 1
# Next row

# Q73

# i = 1

# while i <= 2:
#     j = 0

#     while j < 4:
#         j += 1

#         if j == 2:
#             continue

#         print(i, j)

#     i += 1
    
# 1 1
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4

# Q74

# i = 1

# while i <= 5:
#     i += 1

#     if i == 3:
#         continue

#     print(i, end=" ")

# 2 4 5 6 

# Q75

# i = 1

# while i <= 3:
#     j = 0

#     while j < 3:
#         j += 1

#         if j == 2:
#             continue

#         print(j, end=" ")

#     print("Row")
#     i += 1
    
# 1 3 Row
# 1 3 Row
# 1 3 Row

# Q76

# 12
# 13
# 21
# 23
# 31
# 32
# i = 1

# while i <= 3:
#     j = 1

#     while j <= 3:
#         if j == i:
#             j += 1
#             continue

#         print(i, j)
#         j += 1

#     i += 1

# Q77


# i = 1

# while i <= 2:
#     j = 0

#     while j < 5:
#         j += 1

#         if j == 2:
#             continue

#         if j == 4:
#             break

#         print(i, j)

#     i += 1
    
# 1 1
# 1 3
# 2 1
# 2 3

# Q78

# i = 1

# while i <= 3:
#     j = 1

#     while j <= 4:
#         if j == 2:
#             j += 1
#             continue

#         if i == 3 and j == 4:
#             break

#         print(i * j, end=" ")
#         j += 1

#     print("End")
#     i += 1

# print("Done")


# 1 3 4 End
# 2 6 8 End
# 3 9 End
# Done

# Q 56
# n=5
# i=1
# fact=1
# while i<=5:
#     fact=fact*i
#     i=i+1
#     print(fact)
    
# Q57

# n=25
# fact=1
# i=1
# while fact<n:
#     i=i+1
#     fact=fact*i
# if fact==n:
#     print("yes")
# else:
#     print("no")  


# Q58

# n=20
# fact=1
# i=0
# while fact*(i+1)<=n:
#     i=i+1
#     fact=fact*i
# print(fact)

# 59

# i = 1

# while i <= 2:
#     j = 1

#     while j <= 3:
#         print(i, j)
#         j += 1

#     i += 1
    
# output 
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3

# q 60

# i = 1

# while i <= 3:
#     j = 1

#     while j <= 2:
#         print(j, end=" ")
#         j += 1

#     print()
#     i += 1
    
# # 1 2 
# 1 2 
# 1 2 


# Q61

# i = 1

# while i <= 3:
#     j = 1

#     while j <= i:
#         print("*", end=" ")
#         j += 1

#     print()
#     i += 1

# output
# * 
# * * 
# * * * 

# Q62
# 123
# 23
# 1
# i = 1

# while i <= 3:
#     j = i

#     while j <= 3:
#         print(j, end=" ")
#         j += 1

#     print()
#     i += 1

# # Q64

# i = 1

# while i <= 2:
#     j = 1

#     while j <= 2:
#         print(i + j)
#         j += 1

#     i += 1

# print("Finished")


# 2
# 3
# 3
# 4
# Finished


# Q65

# i = 1

# while i <= 2:
#     print("A", i)
#     i += 1

# j = 1

# while j <= 3:
#     print("B", j)
#     j += 1
 
# A 1
# A 2
# B 1
# B 2
# B 3   

# Q66


# i = 1
# j = 1

# while i <= 3:
#     while j <= 2:
#         print(i, j)
#         j += 1

#     i += 1

# 1 1
# 1 2


# Q67
# i = 1

# while i <= 3:
#     j = 1

#     while j <= 2:
#         print(i, end="")
#         j += 1

#     print()
#     i += 2
    
# 11
# 33

# Q68


# i = 1

# while i <= 3:
#     j = 1

#     while j < i:
#         print(j, end=" ")
#         j += 1

#     print("X")
#     i += 1

# X
# 1 X
# 1 2 X

# Q69


# i = 1

# while i <= 3:
#     j = 1

#     while j <= 4:
#         if j == 3:
#             break

#         print(i, j)
#         j += 1

#     i += 1
# # 1 1
# # 1 2
# # 2 1
# # 22
# # 31
# # 32

# Q 70


# i = 1

# while i <= 2:
#     j = 1

#     while j <= 4:
#         print(j, end=" ")

#         if j == 2:
#             break

#         j += 1

#     print("|")
#     i += 1
    
# 1 2 |
# 1 2 |

# Q71
# i = 1

# while i <= 2:
#     j = 1

#     while j <= 2:
#         if j == 5:
#             break

#         print(i, j)
#         j += 1

#     i += 1

# 1 1
# 1 2
# 2 1
# 2 2

# Q72

# i = 1

# while i <= 3:
#     j = 1

#     while j <= 3:
#         if j == 2:
#             break

#         print(i, j)
#         j += 1

#     print("Next row")
#     i += 1

# 1 1
# Next row
# 2 1
# Next row
# 3 1
# Next row

# Q73

# i = 1

# while i <= 2:
#     j = 0

#     while j < 4:
#         j += 1

#         if j == 2:
#             continue

#         print(i, j)

#     i += 1
    
# 1 1
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4

# Q74

# i = 1

# while i <= 5:
#     i += 1

#     if i == 3:
#         continue

#     print(i, end=" ")

# 2 4 5 6 

# Q75

# i = 1

# while i <= 3:
#     j = 0

#     while j < 3:
#         j += 1

#         if j == 2:
#             continue

#         print(j, end=" ")

#     print("Row")
#     i += 1
    
# 1 3 Row
# 1 3 Row
# 1 3 Row

# Q76

# 12
# 13
# 21
# 23
# 31
# 32
# i = 1

# while i <= 3:
#     j = 1

#     while j <= 3:
#         if j == i:
#             j += 1
#             continue

#         print(i, j)
#         j += 1

#     i += 1

# Q77


# i = 1

# while i <= 2:
#     j = 0

#     while j < 5:
#         j += 1

#         if j == 2:
#             continue

#         if j == 4:
#             break

#         print(i, j)

#     i += 1
    
# 1 1
# 1 3
# 2 1
# 2 3

# Q78

# i = 1

# while i <= 3:
#     j = 1

#     while j <= 4:
#         if j == 2:
#             j += 1
#             continue

#         if i == 3 and j == 4:
#             break

#         print(i * j, end=" ")
#         j += 1

#     print("End")
#     i += 1

# print("Done")


# 1 3 4 End
# 2 6 8 End
# 3 9 End
# Done

    
</pre>
