height = float(input("Enter you height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight/(height/100)**2
bmi = round (bmi, 2)

if bmi <= 18.4:
    print(f"Your bmi is {bmi}. You are underwight.")
elif bmi <= 24.9:
     print(f"Your bmi is {bmi}. You are healthy.")
elif bmi <= 29.9:
      print(f"Your bmi is {bmi}. You are overweight.")
elif bmi <= 34.9:
      print(f"Your bmi is {bmi}. You are severly overweight.")
elif bmi <= 39.9:
     print(f"Your bmi is {bmi}. You are obese.") 
else:
      print(f"Your bmi is {bmi}. You are severly obese.")
