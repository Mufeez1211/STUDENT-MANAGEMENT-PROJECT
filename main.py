
import json

with open("students.json", "r") as file:
    students = json.load(file)

print("=" * 65)
print("     Student Management System")
print("=" * 65)

print("\nComplete Student Data")
print("-" * 65)

for student in students:
    print("ID   :", student["id"])
    print("Name :", student["name"])
    print("Age  :", student["age"])
    print("Class:", student["class"])
    print("Marks")
    print("English :", student["marks"]["English"])
    print("Maths   :", student["marks"]["Maths"])
    print("Social  :", student["marks"]["Social"])
    print("=" * 65)

while True:
    print("\n")
    print("=" * 65)
    print("       Main Menu")
    print("=" * 65)
    print("1. Show All Students")
    print("2. Search student by ID")
    print("3. Search Student by Name")
    print("4. Show Student Result")
    print("5. Find Highest Scorer")
    print("6. Find Lowest Scorer")
    print("7. Show Passed Students")
    print("8. Show Failed Students")
    print("9. Show Students With Marks Below 60")
    print("10. Show Students With Marks 90+")
    print("11. Exit")

    choice = input("\nEnter Your Choice : ")

    if choice == "1":

        print("\n")
        print("=" * 65)
        print("             All Students")
        print("=" * 65)

        for student in students:

            print("ID    :", student["id"])
            print("Name  :", student["name"])
            print("Age   :", student["age"])
            print("Class :", student["class"])

            print("English :", student["marks"]["English"])
            print("Maths   :", student["marks"]["Maths"])
            print("Social  :", student["marks"]["Social"])

            print("-" * 65)

    elif choice == "2":

        search_id = input("\nEnter Student ID: ")

        found = False

        for student in students:

            if student["id"] == search_id:

                print("\n")
                print("=" * 65)
                print("             Student Found")
                print("=" * 65)

                print("ID    :", student["id"])
                print("Name  :", student["name"])
                print("Age   :", student["age"])
                print("Class :", student["class"])

                print("\nMarks")
                print("English :", student["marks"]["English"])
                print("Maths   :", student["marks"]["Maths"])
                print("Social  :", student["marks"]["Social"])

                found = True
                break

        if found == False:
            print("\nStudent ID not found.")

    elif choice == "3":

        search_name = input("\nEnter Student Name to get details: ")

        found = False

        for student in students:

            if student["name"].lower() == search_name.lower():

                print("\n")
                print("=" * 65)
                print("          Student Name Found")
                print("=" * 65)

                print("ID    :", student["id"])
                print("Name  :", student["name"])
                print("Age   :", student["age"])
                print("Class :", student["class"])

                print("\nMarks")
                print("English :", student["marks"]["English"])
                print("Maths   :", student["marks"]["Maths"])
                print("Social  :", student["marks"]["Social"])

                found = True
                break

        if found == False:
            print("\nStudent Name not found.")

    elif choice == "4":

        search_id = input("\nEnter Student ID: ")

        found = False

        for student in students:

            if student["id"] == search_id:

                english = student["marks"]["English"]
                maths = student["marks"]["Maths"]
                social = student["marks"]["Social"]

                total = english + maths + social
                average = total / 3
                percentage = (total / 300) * 100

                print("\n")
                print("=" * 65)
                print("             Student Result")
                print("=" * 65)

                print("ID    :", student["id"])
                print("Name  :", student["name"])
                print("Age   :", student["age"])
                print("Class :", student["class"])

                print("-" * 65)

                print("Total      :", total, "/300")
                print("Average    :", round(average, 2))
                print("Percentage :", round(percentage, 2), "%")

                if average >= 90:
                    grade = "A+"
                elif average >= 80:
                    grade = "A"
                elif average >= 70:
                    grade = "B"
                elif average >= 60:
                    grade = "C"
                elif average >= 50:
                    grade = "D"
                else:
                    grade = "F"

                if english >= 35 and maths >= 35 and social >= 35:
                    status = "Pass"
                else:
                    status = "Fail"

                print("Grade  :", grade)
                print("Status :", status)

                found = True
                break

        if found == False:
            print("\nStudent not found.")

    elif choice == "5":

        highest_student = None
        highest_average = 0

        for student in students:

            english = student["marks"]["English"]
            maths = student["marks"]["Maths"]
            social = student["marks"]["Social"]

            total = english + maths + social
            average = total / 3

            if average > highest_average:
                highest_average = average
                highest_student = student

        print("\n")
        print("=" * 65)
        print("             Highest Scorer")
        print("=" * 65)

        print("ID      :", highest_student["id"])
        print("Name    :", highest_student["name"])
        print("Average :", round(highest_average, 2))

        print("English :", highest_student["marks"]["English"])
        print("Maths   :", highest_student["marks"]["Maths"])
        print("Social  :", highest_student["marks"]["Social"])

    elif choice == "6":

        lowest_student = None
        lowest_average = 101

        for student in students:

            english = student["marks"]["English"]
            maths = student["marks"]["Maths"]
            social = student["marks"]["Social"]

            total = english + maths + social
            average = total / 3

            if average < lowest_average:
                lowest_average = average
                lowest_student = student

        print("\n")
        print("=" * 65)
        print("             Lowest Scorer")
        print("=" * 65)

        print("ID      :", lowest_student["id"])
        print("Name    :", lowest_student["name"])
        print("Average :", round(lowest_average, 2))

        print("English :", lowest_student["marks"]["English"])
        print("Maths   :", lowest_student["marks"]["Maths"])
        print("Social  :", lowest_student["marks"]["Social"])

    elif choice == "7":

        print("\n")
        print("=" * 65)
        print("             Passed Students")
        print("=" * 65)

        for student in students:

            english = student["marks"]["English"]
            maths = student["marks"]["Maths"]
            social = student["marks"]["Social"]

            if english >= 35 and maths >= 35 and social >= 35:
                print(student["id"], "|", student["name"])
            else:
                continue

    elif choice == "8":

        print("\n")
        print("=" * 65)
        print("             Failed Students")
        print("=" * 65)

        for student in students:

            english = student["marks"]["English"]
            maths = student["marks"]["Maths"]
            social = student["marks"]["Social"]

            if english < 35 or maths < 35 or social < 35:
                print(student["id"], "|", student["name"])
            else:
                continue

    elif choice == "9":

        print("\n")
        print("=" * 65)
        print("        Students Scored Below 60")
        print("=" * 65)

        for student in students:

            english = student["marks"]["English"]
            maths = student["marks"]["Maths"]
            social = student["marks"]["Social"]

            if english < 60 or maths < 60 or social < 60:

                print(
                    student["id"],
                    "|",
                    student["name"],
                    "| English:",
                    english,
                    "| Maths:",
                    maths,
                    "| Social:",
                    social
                )

            else:
                pass

    elif choice == "10":

        print("\n")
        print("=" * 65)
        print("        Students Scored 90+")
        print("=" * 65)

        for student in students:

            english = student["marks"]["English"]
            maths = student["marks"]["Maths"]
            social = student["marks"]["Social"]

            if english >= 90 or maths >= 90 or social >= 90:

                print(
                    student["id"],
                    "|",
                    student["name"],
                    "| English:",
                    english,
                    "| Maths:",
                    maths,
                    "| Social:",
                    social
                )

            else:
                pass

    elif choice == "11":

        print("\n")
        print("=" * 65)
        print("   Thank you for using Student Management System!")
        print("=" * 65)

        break

    else:

        print("\nInvalid Choice")
        print("Please Enter a number from 1 to 11.")
