calculation_to_units = 24 * 60 * 60
name_of_unit = 'seconds'

#print(f'20 days are {20 * calculation_to_units}  {name_of_unit}')


def days_to_units(num_of_days, custom_message):
    print(f'{num_of_days} days are {num_of_days * calculation_to_units}  {name_of_unit}')


user_input = input('enter a number of days\n')
print(user_input)
#   print(custom_message)


# def scope_check():
#    local_var = 'my local var'
#    print(name_of_unit)
#    print(local_var)

# scope_check()

# days_to_units(65, 'testing')
