###

#q1
n = int(input("Enter a number: "))
fact = 1

for i in range (1, n + 1):
    fact *= 1
    print("factorial=",fact)

#q2
n=int(input("enter a number:"))
temp = n
digits = len(str(n))
s = 0

while temp > 0:
    d = temp % 10
    s += d ** digits
    temp //= 10


if s == n:
    
    print("Armstrong number")
else:
    print("Not an armstrong number")

#q3
n = int(input("enter number of terms: "))
a, b = 0, 1
print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#q4
n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
           print("Not a prime number")
        break
    else:
        print("Prime Number")
else:
    print("not a Prime Number")
                  


#q5
n = int(input("Enter a number: "))
temp = n
rev = 0

while temp > 0:
   rev = rev * 10 + temp % 10
   temp //= 10

if n == rev:
    print("palindrome number")
else:
     print("not a palindrome number")

 #Q6
n =int(input("Enter a number: "))
sum = 0

while n > 0:
     sum = sum + (n % 10)
     n = n // 10

print("Sum of digits = ", sum)


#q7
count = 0

for i in range(1, 101):
    if i % 5 == 0 or i % 7 == 0:
        print(i)
        count += 1

print("Total count =", count)

#q8
s = input("Enter a string: ")
print("Uppercase string:",s.upper())

#q9
n = int(input("Enter a number:"))

for i in range(1,11):
    print(n,"*",i,"=",n * i)

#q10
for i in range(n):
    for j in range (1, n - i + 1):
        print (j, end ="")


for k in range(2 * i - 1):
    print("*", end="")

    for j in range(n -1 ,0, -1):
        print(j, end="")


print()

#q11
n = int(input("Enter value of n: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + (1 / i)

print("sum of the series is:",sum)    

    


     
 

 
    



