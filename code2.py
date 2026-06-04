birth_year = input('Birth_year: ')
print(type(birth_year))
age = 2026 - int(birth_year)
print(type(age))
print(age)
weight_lbs = input('weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
course = 'Python for "beginners"'
print(course)
another_course = '''
Hi!
This is my first interaction with you!
Goodbye.
'''
print(another_course)
one_more_course = "I'm coding"
final_course = one_more_course[2:-2]
print(final_course)
first_name = 'Liam'
last_name = 'Smith'
message = first_name + ' [' + last_name + '] is a coder'
print(message)
message_2 = f'{first_name} [{last_name}] is a coder'
print(message_2)
text_to_be_counted = "I speak English"
print(len(text_to_be_counted))