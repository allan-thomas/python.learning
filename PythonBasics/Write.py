with open("test.txt","r") as reader:

    content = reader.readlines()
    reversedcontent = reversed(content)
    with open("test.txt","w") as writer:

        for line in reversedcontent:
            writer.write(line)

with open("test.txt","r") as reader:
    content = reader.readlines()
    for line in content:
        print(line)
