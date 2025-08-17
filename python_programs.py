# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 13:15:33 2025

@author: soulr
"""

## Program 1

A=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for i in range(0, len(A)):
    A[i]=A[i] + 1

print(A)

## Program 2

A=[1,2,3,4]
B=[1,1,2,2]
C=[ ]

print("Original list 1 is :" ,A)
print("Original list 2 is :" ,B)

for i in range(0,len(A)):
    C.append(A[i]+B[i])

print("The resultant list is:",C)

## Program 3

numbers = [2,5,7,8,3,6,4,9,10]
even_sum = 0
odd_sum = 0

for i in range(len(numbers)):
    
    if numbers[i] % 2 == 0:
        even_sum += numbers[i]
    else:
        odd_sum += numbers[i]

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

## Program 4

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice (1/2/3/4): ")
if choice in ('1', '2', '3', '4'):
 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))

 if choice == '1':
 print("Result:", num1, "+", num2, "=", num1 + num2)
 elif choice == '2':
 print("Result:", num1, "-", num2, "=", num1 - num2)
 elif choice == '3':
 print("Result:", num1, "*", num2, "=", num1 * num2)
 elif choice == '4':
 if num2 == 0:
 print("Error! Division by zero.")
 else:
 print("Result:", num1, "/", num2, "=", num1 / num2)
else:
 print("Invalid choice! Please select a valid operation.")

## Program 5
import statistics as st
import numpy as np

marks = np.array([5,6,1,3,4,5,6,2,7,8,6,5,4,6,5,1,2,3,4])
marks_mean=np.mean(marks)

print("The Mean(average of marks)is : ",marks_mean)

marks_median= np.median(marks)

print(" The Median( middle value of the sorted marks) is : ",marks_median)

marks_mode= st.mode(marks)

print( " The Mode (the most frequent occurred number) : ",marks_mode)

## Program 6
import pandas as pd

f1=pd.read_csv("C:\\Users\\soulr\\OneDrive\\Documents\\Book.csv")

print(f1.head(10))

## Program 7
import pandas as pd
name = ["aparna", "pankaj", "sudhir", "zayn"]
scr = [70, 40, 85, 98]
dict = {'name': name, 'score': scr}
df = pd.DataFrame(dict)
df.to_csv('C:\\Users\\soulr\\Documents\\Books.csv', index=False)
f1=pd.read_csv("C:\\Users\\soulr\\Documents\\Books.csv")
print(f1)


