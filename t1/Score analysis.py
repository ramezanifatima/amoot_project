student_data = {
    'ali': {
        'math': 70,
        'english': 60,
        'science': 80
    },
    'reza': {
        'math': 90,
        'english': 45,
        'science': 50
    },
    'javad': {
        'math': 50,
        'english': 55,
        'science': 65
    },
}
avg = {}
student_failing =[]
for std in student_data:
    scores = student_data[std].values()
    sum = 0
    l = len(scores)
    for score in scores:
        sum += score
        if score<50:
            student_failing.append(std)
    avg.update({std: round(sum / l, 2)})

max_grades = max(avg,key=avg.get)
min_grades = min(avg,key=avg.get)

print(f'Highest average grade : {max_grades}({avg[max_grades]})\n  Lowest average grade : {min_grades}({avg[min_grades]})\n'
      f'Students failing : {student_failing}')