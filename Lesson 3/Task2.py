phone_number = input('Enter your phone number: ')
if len(phone_number) <= 10 and phone_number.isdigit():
    print('Thank you')
else:
    print('Error. Do not use letters when entering data.')