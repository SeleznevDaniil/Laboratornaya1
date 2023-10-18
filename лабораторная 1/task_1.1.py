numbers = list(map(float, input().split()))
sum = sum(numbers)
length = len(numbers) + 1

current = 0
currentWasSet = True
lostIndex = -1
for number in numbers:
    lostIndex += 1
    if(number - current > 1.0 and currentWasSet):
        break
    currentWasSet = True
    current = number
numbers.insert(lostIndex, sum / length)
print(numbers)
