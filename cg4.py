total =0
MAX_SCORES = 5
for i in range (MAX_SCORES):
     score = float(input("Enter score #", i+1, ": "))
     while score < 0 or score > 100:
           score = float(input("Error: Enter number between 1 and 100.  Enter score #", i+1, ": "))
     total += score
average = total/MAX_SCORE
print(average)
