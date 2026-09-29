# ==========================================
#          MESS FEEDBACK SYSTEM
# ==========================================

feedbacks = []
complaints = []


# ==========================================
# LOAD FEEDBACK
# ==========================================

def load_feedback():
    try:
        with open("feedback.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 5:
                    feedbacks.append({
                        "name": data[0],
                        "meal": data[1],
                        "dish": data[2],
                        "rating": int(data[3]),
                        "comment": data[4]
                    })

    except FileNotFoundError:
        pass


# ==========================================
# SAVE FEEDBACK
# ==========================================

def save_feedback():
    with open("feedback.txt", "w") as file:
        for feedback in feedbacks:
            file.write(
                feedback["name"] + "|" +
                feedback["meal"] + "|" +
                feedback["dish"] + "|" +
                str(feedback["rating"]) + "|" +
                feedback["comment"] + "\n"
            )


# ==========================================
# LOAD COMPLAINTS
# ==========================================

def load_complaints():
    try:
        with open("complaints.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 3:
                    complaints.append({
                        "name": data[0],
                        "meal": data[1],
                        "complaint": data[2]
                    })

    except FileNotFoundError:
        pass


# ==========================================
# SAVE COMPLAINTS
# ==========================================

def save_complaints():
    with open("complaints.txt", "w") as file:
        for complaint in complaints:
            file.write(
                complaint["name"] + "|" +
                complaint["meal"] + "|" +
                complaint["complaint"] + "\n"
            )


# ==========================================
# GIVE FEEDBACK
# ==========================================

def give_feedback():

    print("\n----- GIVE FEEDBACK -----")

    student_name = input("Enter your name: ").strip()
    meal = input("Enter meal (Breakfast/Lunch/Snacks/Dinner): ").strip()
    dish = input("Enter dish name: ").strip()

    while True:
        try:
            rating = int(input("Give rating (1-5): "))

            if 1 <= rating <= 5:
                break

            print("Please enter a rating between 1 and 5.")

        except ValueError:
            print("Please enter a number from 1 to 5.")

    comment = input("Enter your comment: ").strip()

    feedback = {
        "name": student_name,
        "meal": meal,
        "dish": dish,
        "rating": rating,
        "comment": comment
    }

    feedbacks.append(feedback)

    save_feedback()

    print("\nFeedback submitted successfully!")
    print("Feedback has been saved permanently.")


# ==========================================
# VIEW FEEDBACK
# ==========================================

def view_feedback():

    print("\n----- ALL FEEDBACK -----")

    if not feedbacks:
        print("No feedback has been submitted yet.")
        return

    for i, feedback in enumerate(feedbacks, 1):

        print("\nFeedback", i)
        print("Name:", feedback["name"])
        print("Meal:", feedback["meal"])
        print("Dish:", feedback["dish"])
        print("Rating:", feedback["rating"], "/ 5")
        print("Comment:", feedback["comment"])


# ==========================================
# RATING SUMMARY
# ==========================================

def rating_summary():

    print("\n----- RATING SUMMARY -----")

    if not feedbacks:
        print("No ratings available.")
        return

    total_rating = 0

    for feedback in feedbacks:
        total_rating += feedback["rating"]

    average = total_rating / len(feedbacks)

    print("Total Feedback:", len(feedbacks))
    print("Average Rating:", round(average, 2), "/ 5")

    print("\nRating Distribution:")

    for rating in range(5, 0, -1):

        count = 0

        for feedback in feedbacks:
            if feedback["rating"] == rating:
                count += 1

        print(rating, "star:", count, "feedback(s)")


# ==========================================
# SUBMIT COMPLAINT
# ==========================================

def submit_complaint():

    print("\n----- SUBMIT COMPLAINT -----")

    student_name = input("Enter your name: ").strip()
    meal = input("Enter meal: ").strip()
    complaint_text = input("Enter your complaint: ").strip()

    complaint = {
        "name": student_name,
        "meal": meal,
        "complaint": complaint_text
    }

    complaints.append(complaint)

    save_complaints()

    print("\nComplaint submitted successfully!")
    print("Complaint has been saved permanently.")


# ==========================================
# VIEW COMPLAINTS
# ==========================================

def view_complaints():

    print("\n----- ALL COMPLAINTS -----")

    if not complaints:
        print("No complaints have been submitted.")
        return

    for i, complaint in enumerate(complaints, 1):

        print("\nComplaint", i)
        print("Name:", complaint["name"])
        print("Meal:", complaint["meal"])
        print("Complaint:", complaint["complaint"])


# ==========================================
# MAIN MENU
# ==========================================

def main():

    load_feedback()
    load_complaints()

    while True:

        print("\n================================")
        print("       MESS FEEDBACK SYSTEM")
        print("================================")

        print("1. Give Feedback")
        print("2. View Feedback")
        print("3. Rating Summary")
        print("4. Submit Complaint")
        print("5. View Complaints")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            give_feedback()

        elif choice == "2":
            view_feedback()

        elif choice == "3":
            rating_summary()

        elif choice == "4":
            submit_complaint()

        elif choice == "5":
            view_complaints()

        elif choice == "6":
            print("\nThank you for using Mess Feedback System!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")


# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":
    main()