# WAP to Validate User Given AGE
# Age must be in B/W 23 to 40

def validate_age(given_age):
    if((given_age>=23) and (given_age<=40)):
        print("Valid Age")
    else:
        raise ValueError("Invalid Age")
        #raise throw an Exception


age = int(input("Enter Age : "))
try:
    validate_age(age)
except ValueError as ve:
    print(ve)
else:
    print("Thanks For Validating Age")
finally:
    print("Thanks")

    












