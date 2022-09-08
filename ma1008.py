'''
# Q4
start_value = int(input("Start Value = "))
end_value = int(input("End Value = "))
increment = int(input("Increment = "))

for i in range(start_value, end_value + 1, increment):
    print(f"{i} SGD = {i * 3.03} MYR")

j = start_value
while (j <= end_value):
    print(f"{j} MYR = {j / 3.03} SGD")
    j += increment
'''
# Q5
height = int(input("height = "))
output = ""
for i in range(height):
    output = ("AA" if i % 2 == 0 else "BB") + output
    print(output)
    i += 1
