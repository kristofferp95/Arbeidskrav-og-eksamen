weight = float(input(f'Enter your weight in kg (for.x 82.5): '))
height = float(input(f'Enter your height in meters (for.x 1.78): '))

bmi = weight / (height * height)

print(f'Your BMI is {bmi:.1f}')