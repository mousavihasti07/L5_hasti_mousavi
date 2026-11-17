numbers = [4, 9, 15, 23, 42, 56, 71]
user_number = int(input('enter your number:'))

for i in numbers:
    if user_number in numbers:
        print('number found.')
        break
    else:
        print('number not found.')
        break



