# Write your code here :-)

def collatz(number):
    if number %2 == 0:
        number = number//2
    else:
        number = (3*number) + 1
    print(number)
    return number

# Loop the program
a = 0
while a == 0:
    number = input("Enter an integer: ")
    number = int(number)
    while number != 1:
        number = collatz(number)
    print("We're restarting the loop")
