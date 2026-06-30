height = int (input(f" What's your Height in cm?"))
age = input (f"Are you 18 or above? (yes/no):").lower()
if height>=160 and age == "yes":
    print(f" Welcome! you're Eligible")
elif height>= 160 and age == "no":
    print(f" You're tall enough but you're a child!")
else:
    print(f" Sorry! you're not eligible!!!")        