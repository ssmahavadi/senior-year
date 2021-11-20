def Output(result):
    if result == "yes":
        print("The two words are anagrams.")
    else:
        print("The two words are NOT anagrams.")

def Comparison(word1, word2):
    result = ""
    if (sorted(word1)==sorted(word2)):
        result = "yes"
    else:
        result = "no"
    Output(result)

def Input():
    print("Enter the first word: ")
    word1 = input()
    print("Enter the second word: ")
    word2 = input()
    Comparison(word1, word2)
