from datetime import date
a = date.today()
b = date.today().strftime("%A") # %A pelna nazwa  %a gdy z malej nazwa dnia tygodnia bedzie skrocona
print(a, b)
