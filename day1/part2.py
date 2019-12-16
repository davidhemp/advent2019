with open('input') as f:
    data = f.read().split("\n")
data = data[:-1]
#data = [14,1969,100756]
total = 0
for part in data:
    total_fuel = 0
    extra_fuel = int(int(part)/3)-2
    while extra_fuel > 0:
        total_fuel += extra_fuel
        extra_fuel = int(int(extra_fuel)/3)-2
    total += total_fuel
print(total)

