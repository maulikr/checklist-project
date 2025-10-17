filesnames = ["1.one.txt", "2.two.txt", "3.three.txt"]

for filename in filesnames:
    filename = filename.replace(".", "-", 1)
    print(filename)
    