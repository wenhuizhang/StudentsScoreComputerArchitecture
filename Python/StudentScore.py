lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "attendence": [88.0, 40.0, 94.0],
    "papers": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "attendence": [82.0, 83.0, 91.0],
    "papers": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "attendence": [0.0, 75.0, 78.0],
    "papers": [100.0, 100.0]
}



# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)
    
    
def get_average(student):

    Homework = average(student["homework"])
    Attendences = average(student["attendence"])
    Papers = average(student["papers"])
    
    '''
    change your assign weight here
    '''

    return Homework * 0.4 + Attendences * 0.0 + Papers * 0.6


def get_letter_grade(score):
    if score >= 80: 
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
        
#get_letter_grade(get_average(lloyd))        
    

def get_class_average(students):
    results = []
    for student in students:
        get_average(student)
        results.append(get_average(student))
    '''
    print average(results)
    '''
    return average(results)  
    
'''
student list here
'''
    
students = [lloyd, alice, tyler]    
get_class_average(students)   



print get_class_average(students)    
print get_letter_grade( get_class_average(students)   ) 
