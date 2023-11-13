"""those ones with salary above R$ 500 will be increased by 10%,
while those who earn more than R$ 300 will be increased by 7%.
The other workers will have an increase of only 5%."""

#imports
from error import error

#main
while True:
    try:
        salary = float(input("Salary: "))
        break
    except:
        error()

print(f"The old salary: R${salary:.2f}")

if salary > 500:
    salary *= 1.1
elif salary > 300:
    salary *= 1.07
else:
    salary *= 1.05

print(f'The new salary: R${salary:.2f}')