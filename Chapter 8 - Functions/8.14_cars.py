


def make_car(make, model, **kwargs):
    """Print car info"""
    kwargs['make'] = make
    kwargs['model'] = model
    return kwargs

car = make_car('ford', 'flex', v6=True, FlexFuel=False)
car_1 = make_car('car', 'flex', v6=True, FlexFuel=False, trim='LIM')

print(car)
print(f'\n{car_1}')
