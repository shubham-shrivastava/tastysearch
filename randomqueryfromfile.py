import random
from random_words import RandomWords
rw = RandomWords()
count = 0
writeword = ""
file = open("sampled.txt", "r")
queries = open("queryfromfile.txt", "a")
for line in file:
    data = ""
    cont = 0
    if "review/text" in line:
        tokens = line.split()
        for i in range(random.randint(3, 10)):
            myword = random.choice(tokens)
            writeword = myword
            if i == 0:
                if myword.isalpha():
                    queries.write(myword)
                else:
                    queries.write(str(rw.random_words()[0]))
            else:
                if myword.isalpha():
                    queries.write(" ")
                    queries.write(myword)
                else:
                    queries.write(" ")
                    queries.write(str(rw.random_words()[0]))
        if count == 50000:
            break
        count = count + 1
        queries.write("\n")
print(count)
file.close()
queries.close()
