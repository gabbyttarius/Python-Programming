count = 0

for even_numbers in range(1, 10):
    if even_numbers % 2 == 0:
        print(even_numbers)
        count += 1

print(f"Total even numbers: {count}")
