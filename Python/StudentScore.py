lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}



# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)
    
    
def get_average(student):

    Homework = average(student["homework"])
    Quizzes = average(student["quizzes"])
    Tests = average(student["tests"])

    return Homework * 0.1 + Quizzes * 0.3 + Tests * 0.6


def get_letter_grade(score):
    if score >= 90: 
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
        
get_letter_grade(get_average(lloyd))        
    

def get_class_average(students):
    results = []
    for student in students:
        get_average(student)
        results.append(get_average(student))
    '''
    print average(results)
    '''
    return average(results)  
    
    
    
students = [lloyd, alice, tyler]    
get_class_average(students)   



print get_class_average(students)    
print get_letter_grade( get_class_average(students)   ) 
