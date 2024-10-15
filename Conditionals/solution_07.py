# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

coffee=input("Which Size of Coffee Would you Like to Have \nSmall\nMedium \nLarge: ").upper()

extra_shot= input("Want Extra Shots??\n").lower()


if extra_shot=="yes":
    print(f"{coffee} Coffee With Extra Espresso")
else:
    print(f"{coffee} Coffee")
