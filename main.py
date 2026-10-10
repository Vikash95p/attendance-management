import json

from ai_model import inference_client


# --------------------------------
# LOAD ATTENDANCE DATA
# --------------------------------

with open("attendance.json", "r") as file:
    data = json.load(file)

students = data["students"]


# --------------------------------
# FIND STUDENT
# --------------------------------

def find_student(roll_no):

    for student in students:

        if student["roll_no"] == roll_no:
            return student

    return None


# --------------------------------
# TERMINAL INPUT
# --------------------------------

command = input("Enter command: ")

parts = command.split()


# --------------------------------
# CHECK ATTENDANCE
# --------------------------------

if len(parts) == 3 and parts[0] == "check":

    roll_no = parts[1]
    date = parts[2]

    student = find_student(roll_no)

    if student is None:

        print("Student not found.")

    elif date not in student["attendance"]:

        print("Date not found.")

    else:

        # Create request
        request = {
            "action": "check_attendance",
            "roll_no": roll_no,
            "date": date
        }

        print()
        print("Request sent to Inference Client:")

        print(json.dumps(request, indent=4))


        # Send request to inference client
        response = inference_client(request, data)


        print()
        print("Response from AI:")

        print(json.dumps(response, indent=4))


# --------------------------------
# PERCENTAGE
# --------------------------------

elif len(parts) == 2 and parts[0] == "percentage":

    roll_no = parts[1]

    student = find_student(roll_no)

    if student is None:

        print("Student not found.")

    else:

        percentage = (
            student["present_days"]
            / student["total_days"]
        ) * 100

        print()
        print("Student:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Attendance:", round(percentage, 2), "%")


# --------------------------------
# INVALID COMMAND
# --------------------------------

else:

    print("Invalid command.")

    print()
    print("Available commands:")

    print("percentage CS001")

    print("check CS001 2026-10-10")