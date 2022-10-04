name = input("What s your name ? ")
age = input("How old are you ? ")
try:
    age_prochain = int(age)+1
except:
    print("You must put a good value for the age!")
else:
    print("My name is " + name + " and i am " + age + " years old.")
    print("Next year, you will have " + "age_prochain" + "years old!")
