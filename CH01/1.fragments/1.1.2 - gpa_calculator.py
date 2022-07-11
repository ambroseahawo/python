"""Example illustration of while loop"""

print('Welcome to the GPA calculator.')
print('Please enter all your letter grades, one per line')
print('Enter a blank line to designate the end')

# map from letter grades to point value
points = { 'A+' :4.0, 'A' :4.0, 'A-' :3.67, 'B+' :3.33, 'B' :3.0,
             'B-' :2.67,'C+' :2.33, 'C-' :2.0, 'C' :1.67, 'D+' :1.33,
              'D' :1.0, 'F' :0.0 }

NUM_COURSES = 1
TOTAL_POINTS = 0
DONE = False

while not DONE:
    print(f"Course {0}:".format(NUM_COURSES))
    grade = input()
    if grade == '':
        DONE = True
        NUM_COURSES -= 1
    elif grade not in points:
        print(f"Unknown grade '{0}' being ignored".format(grade))
    else:
        NUM_COURSES += 1
        TOTAL_POINTS += points[grade]

if NUM_COURSES > 0:
    print(f"Calculating GPA for {0} courses entered.".format(NUM_COURSES))
    print(f"Your GPA is {0:.3}".format(TOTAL_POINTS/NUM_COURSES))

# Illustrate immutability
# Mutable objects are type list, dict and set
