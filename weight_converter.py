import math

weight = input("what is your weight?:")
unit = input('was that lbs or kgs?(L/K):')
if unit.upper() == 'L':
    weight_kg = int(weight) / 2.20462
    print("your weight in kg:", math.trunc(weight_kg))
elif unit.upper() == 'K':
    weight_lbs = int(weight) * 2.20462
    print(f'your weight in lbs: {math.trunc(weight_lbs)}')