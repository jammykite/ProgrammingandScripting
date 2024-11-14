def temperature_classify():

    user_input_temperature = float(input("Please enter the current temperature in degreee celsius : "))

    if user_input_temperature <10:
        return 'Cold'
    elif user_input_temperature <25:
        return 'Warm'
    else:
        return 'Hot'

if __name__ == '__main__':
    temp_class = temperature_classify()
    print(f'It is currently {temp_class.lower()}')
