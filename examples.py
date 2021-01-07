# comment

"""
Multiline
Comment
"""

name = 'Jackson'
age = 34
is_old = False
sei_1019 = True

print(name)

name = 'Lev'

print(name)

# Methods for a String

sentence = "Today is Nicole's birthday"
nicole_birthday = sentence.split(' ')
print(nicole_birthday)

new_sentence = (' ').join(nicole_birthday)
# OR: new_sentence = (' ').join(nicole_birthday)

print(new_sentence)

# Find index
print(new_sentence.index('N'))

# Upper case everything
name.upper()

# Lower case everything
name.lower()

# Replace character
day_sentence = sentence.replace('birthday', 'Day')
print(day_sentence)

# In keyword
is_day = 'Day' in day_sentence

print(is_day)

last_letter = day_sentence[-1]
nicole_range = day_sentence[9:15]
print(nicole_range)

# length
print(len(nicole_range))

# logical operators
equal_to = 5 == 5
not_equal = 5 != 5

false_variable = not True
true_variable = not False

print(9 < 30)

print(5 < 6 < 7)

print(5 < 4 or 6 > 30)

print(5 < 6 and 1 > 0)

print('Rome' == 'rome' or 'Pete' == 'Pete') # TRUE
print('Rome' == 'rome' and 'Pete' == 'Pete') # FALSE

print('' or 'Rome') # Will return 'Rome' because it is the truthy value
print(0 or 5) # Will return 5 because it is the truthy value

# SHORTCUTS
# str[index] choose one letter at index
# str[-index] choose letter at index counting backwards from the end.
# str[start:end] get a range of letters from a start to end.
# str[start:end:step] get a range of letters taking step sized steps between.
# str[:end] omit the start index and grab letters from zero up to end.
# str[start:] omit the end index and grab letters from start up to the end of the string.
# str[::-1] reverses a string by going backwards with a step of -1 from start to end.