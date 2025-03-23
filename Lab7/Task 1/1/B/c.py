# read input values

correct_answer = int(input())
student_answer = int(input())

# check if the student's answer is correct 
if(correct_answer !=1 and student_answer !=1) or (correct_answer == student_answer):
    print("YES")
else:
    print("NO")