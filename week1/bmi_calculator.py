height = input("Enter your hieght in m ")
weight = input(" Enter your weight in kg ")
#formular kg/m2
new_height = float(height)
new_weight = int(weight)
Bmi = new_weight / new_height **2
result = int(Bmi)
print(result)

