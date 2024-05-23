def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Hello, Whats your name?: ")
    print("Hello," + student_name + " How goes it. ")

    # Prompt the user for their scores in Math, Science, and English
    math_score = input("Whats your current, Math scores may I ask?: ")
    print("WOW, " + math_score)
    science_score = input("Science?: ")
    print("Okay, Okay " ,  math_score , science_score)
    english_score = input("And finally English?: ")
    print(f"I see you out here! ", math_score , science_score , english_score ," doing numbers! ")
 

    # Store the scores in the respective variables: math_score, science_score, english_score
    # math_score = int(input())
    # science_score = int(input())
    # english_score = int(input())

    # Calculate the average grade
    
    # average_grade = int((math_score, science_score, english_score )/ 3)
    print("test print average grade", average_grade)
    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()
    calculate_average_grade()

    # Print the student's name and their average grade
    print(f"", student_name, calculate_average_grade)