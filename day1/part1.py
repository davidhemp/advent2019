with open('input') as f:
    data = f.read().split("\n")
data = data[:-1]
total = 0
for part in data:
    total += int(int(part)/3)-2
print(total)

