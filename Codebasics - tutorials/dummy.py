f = open("README.md", "w+")

f.writelines("This is a Readme file")
for line in f:
    print(line)