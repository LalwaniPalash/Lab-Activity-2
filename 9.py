import time

print("Program to calculate sun of 1-10!")
time.sleep(2)

N = 1

for i in range(1, 11):
    N *= i

# Print the result
print(f"The sum of numbers from 1 to 10 is: {N}")