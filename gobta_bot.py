import time 
print(time.ctime())  # show current time

print("hello, this a gobta bot")
print("\n")
namee = input("pls enter your name: ")

while True:
    print("\n")
    print("what would u like to do", namee, "?")
    print("""1) Set a timer 
2) lottery machine
3) textfile for data base 
4) exit """)
    print("\n")
    a = int(input("enter option: "))
    
    if a == 1:
        import time
        print("enter time in seconds")
        a = int(input("duration of timer: "))
        for i in range(a, 0, -1):  # countdown
            print("00:00:", i)
            time.sleep(1)
        print("times up")
        continue

    if a == 3:
        while True:
            print("__enter students detail__")
            name = input("enter name of the student: ")
            clas = int(input("enter class of the student: "))
            age = int(input("enter age of the student: "))
            a = open("studentt.txt", "a")  # open file to write
            a.write("\n")
            a.write("__student_data__\n")
            a.write(name + "\n")
            a.write(str(clas) + "\n")
            a.write(str(age))
            print("details entered")
            b = input("do you want to add more students? y/n: ")
            if b == "y":
                continue
            if b == "n":
                a.close()
                print("bye")
                break
            else:
                print("error")
                continue
            
    if a == 2:
        from random import *
        a = randint(1, 10)  # lucky number
        while True:
            b = randint(1, 10)  # user number
            print("your lottery no. is", b)
            c = int(input("'press 1' to check lottery: "))
            if b == a:
                print("yay, u won 1 million! ")
                break
            else:
                print("no lottery this time")
                d = int(input("press 1 to buy one more ticket/press 2 to exit"))
                if d == 1:
                    continue
                elif d == 2:
                    print("gambling is fun :)")
                    break
            
    if a == 4: 
        print("bye bye!")
        break
    else:
        print("error, try again")
        continue
