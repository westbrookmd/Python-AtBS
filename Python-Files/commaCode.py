
spam = ['apples', 'bananas', 'tofu', 'cats']

a=0

while a == 0:
    for i in range(len(spam)):
        print(spam[i], end = ", ")

    spam= input()
