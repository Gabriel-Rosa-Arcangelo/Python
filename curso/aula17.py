first_value = input('First value? ')
second_value = input('Second_value? ')

if first_value > second_value:
    print(f'{first_value=} is bigger than {second_value=}')
elif first_value < second_value:
    print(f'{second_value=} is bigger than {first_value=}')
else:
    print(f'{second_value=} and {first_value=} are same')
