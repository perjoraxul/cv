student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

final = 0
for n in range(0, len(student_scores)):
  if n > 0 :
    score1 = student_scores[n-1]
    score2 = student_scores[n]
    if score1 > score2 and score1 > final : 
      final = score1
      
    elif score2 > final : 
      final = score2 
      
print(f"The highest score in the class is: {final}")