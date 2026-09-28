# Q1. Positive Number

n = int(input())

if n > 0:
    print("Positive Number")


# Q2. Voting Eligibility Check

age = int(input())

if age >= 18:
    print("Eligible to Vote")


# Q3. Temperature Warning

temp = int(input())

if temp > 40:
    print("High Temperature")


# Q4. Divisible by 5

n = int(input())

if n % 5 == 0:
    print("Divisible by 5")


# Q5. Free Delivery

amount = int(input())

if amount >= 1000:
    print("Free Delivery")


# Q6. Character Check

ch = input()

if ch == "A":
    print("You entered A")


# Q7. Password Length Check

password = input()

if len(password) >= 8:
    print("Strong Length")


# Q8. Number of Digits

n = int(input())

if 100 <= n <= 999:
    print("Three Digit Number")


# Q9. Even or Odd

n = int(input())

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q10. Pass or Fail

marks = int(input())

if marks >= 40:
    print("Pass")
else:
    print("Fail")
    
# Q11. Adult or Minor

age = int(input())

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Q12. Number Sign

n = int(input())

if n > 0:
    print("Positive")
else:
    print("Non-Positive")


# Q13. Divisible by 3

n = int(input())

if n % 3 == 0:
    print("Divisible by 3")
else:
    print("Not Divisible by 3")


# Q14. Login Password

correct_password = "python123"
password = input()

if password == correct_password:
    print("Login Successful")
else:
    print("Invalid Password")


# Q15. Username Check

username = input()

if username == "admin":
    print("Welcome Admin")
else:
    print("Invalid Username")


# Q16. Greater Between Two Numbers

a, b = map(int, input().split())

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Both are Equal")


# Q17. Hot or Comfortable

temperature = int(input())

if temperature > 30:
    print("Hot")
else:
    print("Comfortable")


# Q18. Shopping Discount Eligibility

amount = int(input())

if amount >= 5000:
    print("Discount Available")
else:
    print("No Discount")


# Q19. Grade Calculator

marks = int(input())

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")


# Q20. Temperature Category

temperature = int(input())

if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Warm")
else:
    print("Cold")