import average
import anagrams
import space

print ("Menu \n 1) Run the Average Program \n 2) Run the Anagrams Program \n 3) Run the Space Program \n 4) Quit \nChoose an option:")
option = int(input())

if option == 1:
    average.Input()
    
elif option == 2:
    anagrams.Input()

elif option == 3:
    space.Input()
