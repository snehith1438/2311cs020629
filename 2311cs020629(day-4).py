
n = int(input("Enter a positive integer n: "))


sum_of_evens = 0


for i in range(2, n+1, 2):  # Start from 2 and increment by 2 to get even numbers
    sum_of_evens += i


print("Sum of all even numbers between 1 and", n, "is:", sum_of_evens)
