#Christian Smith, 1/21/2023, TUID: 915789291, This program is for lab1 and is creating a student profile by requesting
#the information from the user and this information then gets placed into a .txt file named "students.txt", to use this 
#program simply run it with the correct python requirements installed and enter on the commandline what it prompts you to enter.

#first attempt at the lab.

def create_student_profile():
    # Prompt user for student information
    full_name = input("Enter the student's full name (first and last): ")
    
    #here we check if the entered TUID is valid or not
    while True:
        tuid = input("Enter the student's TUID (9 digits): ")
        if len(tuid) == 9 and tuid.isdigit():
            break
        print("Error: TUID must be 9 digits long. Please try again.")

    email = input("Enter the student's email address: ")
    phone = input("Enter the student's phone number: ")
    major = input("Enter the student's major: ")
    graduation = input("Enter the student's expected graduation date: ")
    undergraduate = input("Is the student an undergraduate (yes/no): ")

    # Write student information to a text file and organize it properly
    with open("students.txt", "a") as file:
        file.write("Name: " + full_name + "\n")
        file.write("TUID: " + tuid + "\n")
        file.write("Email: " + email + "\n")
        file.write("Phone: " + phone + "\n")
        file.write("Major: " + major + "\n")
        file.write("Graduation: " + graduation + "\n")
        file.write("Undergraduate: " + undergraduate + "\n")

# Loop to allow for multiple students
while True:
    create_student_profile() #we call the creating student method again if yes is entered allowing us to enter multiple students
    again = input("Do you want to add another student? (yes/no): ")
    if again.lower() != "yes":
        print("You entered 'no' or you didn't enter 'yes' properly") #tell them why the program stopped
        break
