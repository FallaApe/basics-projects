import pickle

def txt():
    student = {}
    sub = []
    mark = []
    name = input("Enter name of student: ")
    clas = int(input("Enter class: "))
    
    b = int(input("No. of subjects: "))

    for i in range(b):
        subss = input("Enter subject: ")
        marks = int(input("Enter marks: "))
        sub.append(subss)
        mark.append(marks)
    
    # store data properly
    student["NAME"] = name
    student["CLASS"] = clas
    student["MARKS"] = dict(zip(sub, mark))

    with open("txt.txt", "a") as file:
        file.write(str(student) + "\n")

    with open("txt.txt", "r") as file:
        print(file.read())


def bin():
    student = {}
    name = input("Enter name of student: ")
    clas = int(input("Enter class: "))
    b = int(input("No. of subjects: "))

    student["NAME"] = name
    student["CLASS"] = clas

    for i in range(b):
        subss = input("Enter subject: ")
        marks = int(input("Enter marks: "))
        student[subss] = marks

    # append binary data
    with open("bin.bin", "ab") as file:
        pickle.dump(student, file)

    # read back all records
    with open("bin.bin", "rb") as file:
        print("Records in binary file:")
        try:
            while True:
                print(pickle.load(file))
        except EOFError:
            pass


def main():
    while True:
        print("\nEnter mode of making a database")
        option = int(input("1) txt file  2) binary file  3) exit: "))

        if option == 1:
            txt()
        elif option == 2:
            bin()
        elif option == 3:
            print("Exiting...")
            break
        else:
            print("Invalid option! Try again.")

        # ask if user wants to continue
        cont = input("\nDo you want to enter more data? (y/n): ").lower()
        if cont != 'y':
            break

main()
