# Ildiko Fallahpour
# Complete

# This program accepts five numeric grades from the user, calculates an average
# then turns it into a letter grade.

# The main function accepts five scores, validates them, and calculates their average, finally: calls the
# determine_grade function.

def main():
    total =0
    MAX_SCORES = 5
    for i in range (MAX_SCORES):
         score = float(input('Enter score #'+str( i+1)+ ': '))
         while score < 0 or score > 100:
               score = float(input('Error: Enter number between 1 and 100.  Enter score #'+ str(i+1)+ ': '))
         total += score
         
    average = total/MAX_SCORES
    determine_grade(average)

# The determine_grade validates the average of the grades,turns it into a letter grade and prints the value of
# the average and the corresponding letter grade.

def determine_grade(average):

    if average >= 90:
        print('Your average is:' ,average, 'which is an A')
    elif 80 <= average < 90:
        print('Your average is:' ,average, 'which is a B')
    elif 70 <= average < 80:
        print('Your average is:' ,average, 'which is a C')
    elif 60 <= average < 70:
        print('Your average is:' ,average, 'which is a D')
    else:
        print('Your average is:' ,average, 'which is an F')
main()
