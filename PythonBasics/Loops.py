# if loop
greeting = "Good Morning"

if greeting.endswith("g"):
    print("CONDITON MATCHING")
    print("Second line")
else:
    print("CONDITON NOT MATCHING")

# for loop

obj=[1,25,3,1,52,"String"]

for i in obj:
    print(i*2)

# sum of first 5 natural numbers
s=0
for i in range (1,6):
    s=s+i
print(s)

# the 3rd argument in range is the step size, it will print only odd numbers from 1 to 10
s=0
for i in range (1,11,5):
    print(i)

# if we give only 1 argument in range, it will consider it as the end value and start from 0
for i in range(10,5,-1):
    print(i)