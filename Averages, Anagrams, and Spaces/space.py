def Input():
    print("Enter a phrase: ")
    phrase = input()
    Output(phrase)
    return phrase

def Output(phrase):
    print (phrase.replace(" ",""))
