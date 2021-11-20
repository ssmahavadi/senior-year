def Output(average):
    print ("Your average is: " + str(average))

def Average(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    Output(avg)

def Input():
    print ("Enter grade 1:")
    grade1 = int(input())
    print ("Enter grade 2: ")
    grade2 = int(input())
    print ("Enter grade 3: ")
    grade3 = int(input())
    Average(grade1, grade2, grade3)
