calculation_to_units = 24 * 60 * 60
name_of_unit = 'seconds'

#print(f'20 days are {20 * calculation_to_units}  {name_of_unit}')


def days_to_units(num_of_days):
    return (f'{num_of_days} days are {num_of_days * calculation_to_units}  {name_of_unit}')

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
         cal_value = days_to_units(user_input_number)
         print(cal_value)
        elif user_input_number == 0:
            print ('please enter number greater then zero')
    else:
        print('not a valid number, please try again')

user_input = ''
while user_input != 'exit':
    user_input = input('enter a number of days\n')
    validate_and_execute()

#   print(custom_message)


# def scope_check():
#    local_var = 'my local var'
#    print(name_of_unit)
#    print(local_var)

# scope_check()

# days_to_units(65, 'testing')