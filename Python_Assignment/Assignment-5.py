# Q1. Predict the Loop Values
# Without running the code, write the values printed:

# for i in range(2, 15, 3):
#     print(i)
# Output==>> 2,5,8,11,14


# Q2. Reverse range() Prediction
# Predict the output:

# for i in range(15, 2, -3):
#     print(i)

# output=15,12,9,6,3


# q3.How many literations

# for i in range(4, 31, 5):
#     print(i)
# output=4,9,14,19,24,29

# Q4.Correct the boundry

# for i in range(3, 18, 3):
#     print(i)
# # Output=3,6,9,12,15

# Q5. Number and Distance from 20

# for i in range(5,11):
#     print(i,20-i)

# Q6. Number, Square and Cube

# for i in range(1,7):
#     print(i,i*i,i*i*i)

# Q7. Sum of Numbers in a Range
# sum=0
# for i in range(5,11):
#     sum=sum+i
# print(sum)

# Q8. Count Multiples of 3
# N=int(input())
# count=0
# for i in range(1,N+1):
#     if i%3==0:
#       count=count+1
# print(count)
    
    
# Q9. Sum of Multiples of 4    

# N=int(input())
# sum=0
# for i in range(1,N+1):
#     if i%4==0:
#         sum=sum+i
# print(sum)


# Q10. Count Numbers with Two Conditions
# N=int(input())
# count=0
# for i in range(1,N+1):
#     if i%3==0 and i%5==0:
#        count=count+1
# print(count) 

# Q11. Sum Numbers Except Multiples of 3
# N=int(input())
# sum=0
# for i in range(1,N+1):
#     if i%3!=0:
#         sum=sum+i
# print(sum)


# Q12. Count Even and Odd Together

# N=int(input())
# odd=0
# even=0
# for i in range(1,N+1):
#     if i%2==0:
#         even=even+1
#     else:
#         odd=odd+1
# print("Even=",even)
# print("odd=",odd)


# Q13. Running Sum


    
# N=int(input())
# sum=0
# for i in range(1,N+1):
#     sum=sum+i
#     print(sum)
    
    
    
# Q14. Running Product

# N=int(input())
# product=1
# for i in range(1,N+1):
#     product=product*i
#     print(product)

#  Q15. Factorial of a Number


# N = int(input("Enter N: "))

# fact = 1

# for i in range(1, N + 1):
#     fact = fact * i

# print("Factorial =", fact)


# Q16. Factorial from 1 to N

# N = int(input("Enter N: "))

# fact = 1

# for i in range(1, N + 1):
#     fact = fact * i
#     print(f"{i}! = {fact}")

# Q17. Product of Even Numbers

# N = int(input("Enter N: "))

# product=1

# for i in range(1, N + 1):
#     if i%2==0:
#         product=product*i
# print("product=",product)
        
# Q18. Product of Odd Numbers

# N = int(input("Enter N: "))

# product=1

# for i in range(1, N + 1):
#     if i%2!=0:
#         product=product*i
# print("product=",product)


# Q19. Double Factorial — Even Numbers

# N = int(input("Enter N: "))
# product=1
# for i in range(N,1,-2):
#     product=product*i
# print("product=",product)


# Q20. Sum of Squares

# N = int(input("Enter N: "))
# sum=0
# for i in range(1,N+1):
#     sum=sum+i*i
# print("Sum=",sum)


# Q21. Sum of Cubes

# N = int(input("Enter N: "))
# sum=0
# for i in range(1,N+1):
#     sum=sum+i**3
# print("Sum=",sum)


# Q22. Factorial-Based Sum

# N = int(input("Enter N: "))
# sum=0
# product=1
# for i in range(1,N+1):
#     product=product*i
#     sum=sum+product
# print("Sum=",sum)

# Q23. Count Digits Using a Loop
# import math
# n = int(input("Enter a no.: "))

# count = 0
# log_value=int(math.log10(n))

# sum=0
# for i in range(log_value+1):
#     count=count+1
# print(count)
    
# Question 24

# n=int(input("Enter no."))
# import math
# sum=0
# for i in range(int(math.log10(n))+1):
    
#     sum=sum+n%10
#     n=n//10
    
# print(sum)

# question no 25

# n=int(input("Enter no."))
# import math
# product=1
# for i in range(int(math.log10(n))+1):
    
#     product=product*(n%10)
#     n=n//10
    
# print(product)

# Question 26

# n=int(input("Enter no."))
# import math
# count=0
# for i in range(int(math.log10(n))+1):
#     y=n%10
#     if y%2==0:
#         count=count+1
#     n=n//10
# print(count)

# Question 27
# n=int(input("Enter no."))
# import math
# sum=0
# for i in range(int(math.log10(n))+1):
#     y=n%10
#     if y%2==0:
#         sum=sum+y
#     n=n//10
# print(sum)


# Question no. 28


# n = int(input("Enter no. "))

# largest = 0

# for i in range(len(str(n))):
#     digit = n % 10

#     if digit > largest:
#         largest = digit

#     n = n // 10

# print(largest)

# Question 29

# n = int(input("Enter no. "))

# smallest=9

# for i in range(len(str(n))):
#     digit = n % 10

#     if digit < smallest:
#         smallest = digit

#     n = n // 10

# print(smallest)

# question 30

# n = int(input("Enter a number: "))
# reverse = 0

# for i in range(len(str(n))):
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# print(reverse)

# Question 31

# n=int(input("enter no."))
# original=n
# reverse=0
# for i in range(len(str(n))):
#     y=n%10
#     reverse=reverse*10+y
#     n=n//10
# if original==reverse:
#     print("palindrome")
# else:
#     print("non-palindrome")

# question 32

# n = int(input("Enter a number: "))
# y=int(input("enter no."))
# count = 0

# for i in range(len(str(n))):
#     digit = n % 10
#     if digit==y:
#         count=count+1
   
#     n = n // 10
# print(count)

# question 33

# n = int(input("Enter a number: "))

# for i in range(len(str(n))):
#     digit = n % 10
#     n = n // 10
#     digit=n
# print(digit)

# question 34

# n = int(input("Enter a number: "))
# largest=0
# smallest=9
# for i in range(len(str(n))):
#     digit = n % 10
#     if digit<smallest:
#         smallest=digit
        
#     if digit>largest:
#         largest=digit
    
#     n=n//10
# print(largest-smallest)
    
    
# Question - 35

# N=int(input("Enter no."))
# for i in range(1,len(str(N))+1):
#     digit=N%10
#     N=N//10
#     print(digit , i)

#Question -36

# N=int(input("Enter no."))
# y=abs(N)
# sum=0
# for i in range(1,len(str(N))+1):
#     digit=N%10
#     sum=sum+digit**3
#     N=N//10
# print(sum)
# if y==sum:
#     print("armstrong no.")
# else:
#     print("Non-armstrong")
    

# Question-37

# string=input("Enter no.")
# for i in range(0,len(string)):
#     print(i,string[i])
  
  
# question -38

# string=input("Enter no.")
# count=0
# for ch in string:
#     count=count+1
# print("length=",count)

#question-39

# string=input("Enter your string:").lower()
# vowel=0
# consonant=0
# for ch in string:
#     if ch in "aeiou":
#         vowel=vowel+1
#     else:
#         consonant=consonant+1
# print("vowel",vowel)
# print("consonant",consonant)
        
        
        
# Question 40

# s = input("Enter a string: ")
# target = input("Enter target character: ")

# count = 0

# for ch in s:
#     if ch == target:
#         count += 1

# print("Count:", count)

# Question 41

# s = input("Enter a string: ")
# target = input("Enter target character: ")

# for ch in s:
#         if target==ch:
#             print(s.index(target))

# question 42

# s = input("Enter a string: ")

# lowercase=0
# uppercase=0

# for ch in s:
#     if ch.islower():
#         lowercase=lowercase+1
#     else:
#         uppercase=uppercase+1
# print(uppercase)
# print(lowercase)
            
            
#question 43



# s = input("Enter a string: ")

# for ch in s:
#     print(ch, ord(ch))
        
# Question 44

# s = input("Enter a string: ")

# for ch in s:
#     if ch not in "aeiou":
#         print(ch,end="")
        
# question 45

# s = input("Enter a string: ")

# for i in range(len(s)):
#     if i==(len(s)+1)//2:
#         print(s[i])

# question 46

# s = input("Enter a string: ")

# s = input("Enter a string: ")

# mid = len(s) // 2

# print("First half:", s[:mid])
# print("Second half:", s[mid:])

# question 47

# s = input("Enter a string: ")

# n = len(s)
# first = ""
# second = ""
# middle = ""

# for i in range(n):
#     if i < n // 2:
#         first += s[i]
#     elif n % 2 != 0 and i == n // 2:
#         middle = s[i]
#     else:
#         second += s[i]

# print("First half:", first)

# if n % 2 != 0:
#     print("Middle character:", middle)

# print("Second half:", second)

# Question n0. 48

# s = input("Enter a string: ")
# first=""
# second=""
# for i in range(len(s)):
#     if i<len(s)//2:
#         first=first+s[i]
#     else:
#         second=second+s[i]
# if first==second:
#     print("Equal half")
# else:
#     print("different half")

 
 
# Question 49

# s = input("Enter a string: ")

# n = len(s)
# symmetric = True

# for i in range(n // 2):
#     if s[i] != s[n - 1 - i]:
#         symmetric = False
#         break

# if symmetric:
#     print("Symmetric")
# else:
#     print("Not Symmetric")


# Question 50

# s = input("Enter a string: ")
# for i in range(len(s)):
#     if i%2==0:
#         print(s[i],end="")

# queestion 51

# s = input("Enter a string: ")
# odd=0
# even=0
# for i in range(len(s)):
#     if i%2==0:
#         even=even+1
#     elif i%2!=0:
#         odd=odd+1
# print("Even", even)
# print("Odd:",odd)
    
    
# Question 52
# s = input("Enter a string: ")
# string_1=""
# string_2=""
# for i in range(len(s)):
#     if i%2==0:
#         string_1=string_1+s[i+1]
#     elif i%2!=0:
#         string_1=string_1+s[i-1]
# final=string_1
# print(final)


# question 53
    
    
# n=int(input("Enter no.:"))
# largest=0
# second=0
# for i in range(len(str(n))):
#     digit == n%10
#     if digit >largest:
#         second=largest
#         digit= largest
#         n=n//10
# print(second)
# print(largest)
        
 
# n = int(input("Enter no.: "))

# largest = -1
# second = -1

# while n > 0:
#     digit = n % 10

#     if digit > largest:
#         second = largest
#         largest = digit
#     elif digit > second and digit != largest:
#         second = digit

#     n = n // 10

# print(second)
# print(largest)
    
# Question  54

# s = input("Enter a string: ")

# count = 1
# longest = 1

# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count = count + 1
#     else:
#         count = 1

#     if count > longest:
#         longest = count

# print(longest)
           
# question 55

# s = input("Enter a string: ")
# target=input("enter ch:")
# count=0
# for ch in s:
#     if ch==target:
#         count=count+1
# print(f"{count} frequency:{(count/len(s))*100}")

# Question 56

# s=int(input("enter your no.:"))
# sum=0
# for i in range(len(str(s))):
#     digit = s % 10
#     sum=sum+digit
#     s=s//10
#     print(sum)
    
         
 # 57
 
s=int(input("Enter your no.:"))
even=0
odd=0
for i in range(len(str(s))):
    digit = s % 10
    if digit%2==0:
        even=even+1
    else:
        odd=odd+1
    s=s//10
        
print(even,odd)
if even>odd:
    print("More Even Digits")
elif even==odd:
    print("Equal")
else:
    print("More odd Digits")
 
 
 # # 58


# # n = int(input("Enter a number: "))
# # result = 0

# # for i in range(len(str(n))):
# #     digit = n % 10

# #     if i % 2 == 0:
# #         result = result + digit
# #     else:
# #         result = result - digit

# #     n = n // 10

# # print(result)


# # 59

# # 2
# # 6
# # 12
# # 20
# # 30

# # 60

# 5

# # 61

# # sum = 0
# # for i in range(1, 6):
# #     sum = sum+i
# # print(sum)

# # 62

# # n = int(input())
# # total = 0

# # for i in range(n):
# #     expense = int(input())

# #     total = total + expense

# #     if i == 0:
# #         highest = expense
# #         lowest = expense
# #     else:
# #         if expense > highest:
# #             highest = expense

# #         if expense < lowest:
# #             lowest = expense

# # print("Total expense:", total)
# # print("Highest expense:", highest)
# # print("Lowest expense:", lowest)


# #62
# # n=int(input("enter your no.:"))
# # total=0
# # highest=0
# # lowest=9
# # for i in range(n):
# #     expense=int(input("Enter your expenses:"))
# #     total=total+expense
# #     if i==0:
# #         highest=expense
# #         lowest=expense
# #     else:
# #         if expense>highest:
# #             highest=expense
            
# #         if expense<lowest:
# #             lowest=expense
            
# # print("Total expense:", total)
# # print("Highest expense:",highest)
# # print("Lowest expense:",lowest)
        
        
# 63
# n=int(input("enter your no.:"))
# total=0
# for i in range(n):
#     marks=int(input("Enter your marks:"))
#     total=total+marks
#     if i==0:
#         highest=marks
#         lowest=marks
#     else:
#         if marks>highest:
#             highest=marks
            
#         if marks<lowest:
#             lowest=marks
# print("total",total)
# average=total/n
# print("average:",average)
# print("highest:",highest)
# print("Lowest:",lowest)   

# 64

# n=int(input("enter no.:"))
# present=0
# absent=0
# for i in range(n):
#     att=input("Enter A or P:")
#     if att=="P":
#         present=present+1
#     else:
#         absent=absent+1
        
# print(present)
# print(absent)
# print("Present:",present)
# print("Absent:",absent)
# print("Attandance:",(present/(present+absent)*100))       
        

# 65

# n=int(input("enter no.:"))
# total=0
# count=0
# for i in range(n):
#     units=int(input("enter units:"))
#     total=total+units
#     if units>10:
#         count=count+1
# print("TOtal units:",total)
# print("Days before 10:",count)


# 66

# n=int(input("enter no.:"))
# total=0
# count=0
# for i in range(n):
#     prices=int(input("enter units:"))
#     total=total+prices
#     if prices>1000:
#         count=count+1
# print("TOtal Bill:",total)
# print("prices above 1000:",count)

# 67

# n=int(input("enter no.:"))
# success=0
# failed=0
# count=0
# for i in range(n):
#     attempts=input("enter attempts:")
#     if attempts=="success":
#         success=success+1
#     else:
#         failed=failed+1
# print("Successful:",success)
# print("Failed:",failed)
# print("Success Rate:",success/(success+failed)*100)
    
# 68

# n = int(input("Enter a positive integer: "))

# digits = 0
# total = 0
# even = 0
# odd = 0

# for i in range(1000):  # loop will stop when n becomes 0
#     if n == 0:
#         break

#     digit = n % 10
#     digits = digits + 1
#     total = total + digit

#     if digits == 1:
#         largest = digit
#         smallest = digit
#     else:
#         if digit > largest:
#             largest = digit

#         if digit < smallest:
#             smallest = digit

#     if digit % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1

#     n = n // 10

# print("Digits:", digits)
# print("Sum:", total)
# print("Largest:", largest)
# print("Smallest:", smallest)
# print("Even Digits:", even)
# print("Odd Digits:", odd)



# 69

s = input("Enter a string: ")

total = 0
vowels = 0
consonants = 0
uppercase = 0
lowercase = 0
even_index = 0

for i in range(len(s)):
    ch = s[i]
    total = total + 1

    if i % 2 == 0:
        even_index = even_index + 1

    if ch != " ":
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

        if ch.isupper():
            uppercase = uppercase + 1
        elif ch.islower():
            lowercase = lowercase + 1

print("Total Characters:", total)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Even Index Characters:", even_index)
 
 
 
 
 



     
