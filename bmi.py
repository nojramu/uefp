# BMI Checker

# BMI Constants
UNDER = 18.5
NORMAL = 24.9
OVER = 29.9

# Pangwe-welcome kay user
print("Mabuhay!, eto ang iyong BMI Checker")

# Tagatangap ng mga input mula sa user
name = input("Ano ang iyong pangalan? ")
weight = float(input("Ilagay ang iyong timbang sa kilo: "))
height = float(input("Ilagay ang iyong taas sa metro: "))

# Pagkalkula ng BMI at kategorya
if (weight > 0 and height > 0):
    bmi = weight / (height ** 2)
    if bmi < UNDER:
        category = "Underweight"
    elif bmi <= NORMAL:
        category = "Normal weight"
    elif bmi <= OVER:
        category = "Overweight"
    else:
        category = "Obese"

    print (f"Kamusta {name}, ang iyong BMI ay {bmi:.2f} at ikaw ay {category}.")
else:
    print("Ang timbang at taas mo ay dapat higit sa zero.")
