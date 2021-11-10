calculation_to_units = 24 * 60 * 60
name_of_unit = 'seconds'

print(f'20 days are {20 * calculation_to_units}  {name_of_unit}')


def days_to_units(num_of_days):
    print(f'{num_of_days} days are {num_of_days * calculation_to_units}  {name_of_unit}')

days_to_units(65)
days_to_units(35)
days_to_units(50)