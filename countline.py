f = open("queryfromfile.txt", "r")
count = 0
for line in f:
    count = count + 1
print(count)
f.close()