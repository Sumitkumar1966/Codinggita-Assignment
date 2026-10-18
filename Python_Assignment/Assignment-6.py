#q1
# n=5
# for i in range(n):
#     print("*"*n)


# Q2.
# row = int(input("Enter row no.:"))
# column=int(input("Enter column no.:"))
# for i in range(row):
#     for j in range(column):
#         print("*",end="")
#     print()
    
#q3.

# n=6
# for i in range(1,n):
#     for j in range(i):
#         print("*",end="")
#     print()
    
# Q4.
   
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# Q5.
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

# Q6.
# s="ABCDE"
# for i in range(len(s)):
#     for j in range(i+1):
#         print(s[i],end="")
#     print()


# Q7.
# s="ABCDE"
# for i in range(len(s)):
#     for j in range(i+1):
#         print(s[j],end="")
#     print()

# Q8.

# n=5
# num=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()
    
    
# Q9

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print((i + j+1) % 2, end=" ")
#     print()

# Q10.

# for i in range(5,0,-1):
#     for j in range(i+1,1,-1):
#         print("*",end="")
#     print()

# Q11.

# for i in range(6,1,-1):
#     for j in range(1,i):
#         print(j,end="")
#     print()

# Q12

# s="ABCDE"
# for i in range(len(s),0,-1):
#     for j in range(0,i):
#         print(s[j],end="")
#     print()

# Q13

# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()


# Q14

# for i in range(1,6):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(6-i):
#         print("*",end="")
#     print()


# Q15

# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(i*2-1):
#         print("*",end="")
#     print()
        

# Q16

# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# Q17

# for i in range(1,5):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(i*2-1):
#         print("*",end="")
#     print()
# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# Q18

# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(1,6):
#         print("*",end="")
#     print()

# Q19

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     for j in range(1,2*(5-i)):
#         print(" ",end="")
#     for j in range(i,0,-1):
#         print(j,end="")
        
#     print()
    
# Q20


# n = 5

# for i in range(1, n + 1):
#     for s in range(n - i):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# Q21

# n = 5

# for i in range(1, n + 1):
#     for s in range(n - i):
#         print(" ", end="")

#     for j in range(1, i + 1):
#         print(j, end="")

#     for j in range(i - 1, 0, -1):
#         print(j, end="")

#     print()

# Q22

# n = 5

# for i in range(1, n + 1):
#     for s in range(n - i):
#         print(" ", end="")

#     for j in range(1, i + 1):
#         print(chr(64 + j), end="")

#     for j in range(i - 1, 0, -1):
#         print(chr(64 + j), end="")

#     print()
    
# Q23

n=5
for i in range(n+1,1):
    for j in range()










# n=5
# for i in range(0,n):
#     start=1
#     if i%2==0:
#         start=1
#     for j in range(0,i+1):
#         print(start,end="")
#         if start==0:
#             start=1
#         elif start==1:
#             start=0
#     print()