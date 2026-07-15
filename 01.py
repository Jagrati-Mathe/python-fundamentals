# Variables & types
name = "Amit"
age = 28
salary = 55000.50
is_employed = True

print(type(name), type(age), type(salary), type(is_employed))

# Type conversion
age_str = str(age)
salary_int = int(salary)  # what happens to the decimal?
print(age_str, salary_int)

# String operations
full_greeting = "Hello, " + name + "!"
print(full_greeting)
print(f"Hello, {name}! You are {age} years old.")  # f-strings — use these, not +