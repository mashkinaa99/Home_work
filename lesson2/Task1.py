name = 'Alena'
day = '15 april'
print(f'Good day {name}! {day} is a perfect day to learn some python.')

x = 'Good day {}! {} is a perfect day to learn some python.'
print(x.format(name, day))

print(f'Good day %s! %s is a perfect day to learn some python.' % (name, day))