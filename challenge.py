#Lynijah Russell
#Challenge! 
# Program that shows Fibonacci numbers up to 100th term. 
count = 0
numOfTerms=100
number1, number2 = 0, 1
print("Fibonacci sequence:")
while (count < numOfTerms):
    print(number1)
    counting = number1 + number2
    number1 = number2
    number2 = counting
    count += 1