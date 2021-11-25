height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / (float(height)*float(height))

#BMI should be a rounded number
print(int(bmi))