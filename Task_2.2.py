#task1
for i in range(1, 11):
    print(i)

# task2
for i in range(1, 11):
    print(i)
    if i == 7:
        print("Breaking the loop")
        break 

# task3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    # Check if the number is a multiple of 3
    if num % 3!= 0:
        print(f"number without multiple by 3: {num}")
        continue
    print(f"skipping with number multiple by 3: {num}")


