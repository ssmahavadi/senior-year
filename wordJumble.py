import random
wordbank = ["apple", "banana", "grape", "orange", "watermelon"]
word = wordbank[random.randrange(0,6)]
correctword = word[:]
jumbledword = ""
while len(word) > 1:
    index = random.randrange(0,len(word)-1)
    jumbledword += word[index]
    word = word[:index] + word[(index+1):]
jumbledword += word
print (jumbledword)
win = False
for x in range (5):
    guess = input("Guess:\n")
    if guess == correctword:
        print ("Correct!")
        win = True
        break
    else:
        print ("Wrong, try again")
        continue
if win == True:
    print ("You won!")
else:
    print ("You lost :/")

