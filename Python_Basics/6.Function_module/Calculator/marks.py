import Grading

math = int(input("Enter your math marks: "))
science = int(input("Enter your science marks: "))
english = int(input("Enter your english marks: "))
total = math + science + english

Perc = total/300*100

print(f"Grade of a marks {Grading.grade(perc)}")