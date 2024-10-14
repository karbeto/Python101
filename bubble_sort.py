numbers = [25, 21, 20, 22, 85, 14, 10, 2, 1, 5, 16, 8, 20, 11]
totalSwaps = 0
while True:
    swaps = 0
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            swaps += 1
            totalSwaps += 1

    if (swaps == 0):
        break
print(numbers)
print(totalSwaps)
