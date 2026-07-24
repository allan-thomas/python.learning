file = open("PythonBasics/test.txt")
# print(file.read())

# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()
val = file.readlines()

for line in file.readlines():
    print(line)
    print(len(line))

print(len(val))
file.close()