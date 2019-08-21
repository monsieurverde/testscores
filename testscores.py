f = open("studentdata.txt", "r")

for aline in f:
    items = aline.split()
    if len(items[1:]) > 6:
        print(items[0])

f.close()
