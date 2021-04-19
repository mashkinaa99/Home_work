phone_number = input('Enter your phone number (no more than 10 characters): ')
if len(phone_number) <= 10 and phone_number.isdigit():
    print('Thank you')
else:
    print('Error. Do not use letters when entering data.')