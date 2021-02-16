#Create a variable called 'name' that holds a string
name = input("enter a name")
print('Name, {}'.format(name))

#Create a variable called 'country' that holds a string
country = input("enter a country")
print('Country, {}'.format(country))

#Create a variable called 'age' that holds an integer
age = input("enter an age")
print('Age, {}'.format(age))

#Create a variable called 'hourly_wage' that holds an integer
hourly_wage = input("enter an hourly wage")
print('Hourly wage, {}'.format(hourly_wage))

#Calculate the daily wage for the user
daily_wage = (8*hourly_wage)

#Create a variable called 'satisfied' that holds a boolean
satisfied = True

#Print out "Hello <name>!"
print("Hello"+name)

#Print out what country the user entered
print(country)

#Print out the user's age
print(age)

#With an f-string, print out the daily wage that was calculated
print(f"this is {name}")

#With an f-string, print out whether the users were satisfied
print(f"User is {satisfied}")