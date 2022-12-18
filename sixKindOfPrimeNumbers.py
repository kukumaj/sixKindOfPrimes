def reduce_to_single_digit(n: int) -> int:
    return n % 9 if n % 9 != 0 else 9

def is_prime(n: int) -> bool:
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

max_prime = int(input("Enter the maximum prime number limit: "))
result_counts = {i: 0 for i in (1, 2, 4, 5, 7, 8)}
total_count = 0
for i in range(2, max_prime+1):
    if is_prime(i):
        result = reduce_to_single_digit(i)
        if result in (1, 2, 4, 5, 7, 8):
            result_counts[result] += 1
            total_count += 1
probabilities = {result: count / total_count for result, count in result_counts.items()}

# Print the results in separate lines
for i in (1, 2, 4, 5, 7, 8):
    print(f"{i}: {probabilities[i]:.3f}")