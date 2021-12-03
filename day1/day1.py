with open("input.txt") as file:
    previous = int(file.readline())
    count = 0
    for line in file:
        count += (current := int(line)) > previous
        previous = current

print(count)
