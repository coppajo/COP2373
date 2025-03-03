import re

def phone_number_val(phone):
    # format is ###-###-####
    pattern = r'\d{3}-\d{3}-\d{4}$'

    # looking for match and then returning the match value
    valid = re.match(pattern, phone)

    return valid


def social_security_val(social):
    # format is ###-##-####
    pattern = r'\d{3}-\d{2}-\d{4}$'

    # looking for match and then returning the match value
    valid = re.match(pattern, social)

    return valid

def zip_code_val(zip):
    # ZIP format: #####
    # ZIP+4 format: #####-####
    pattern = r'\d{5}(-\d{4})?$'

    # looking for match and then returning the match value
    valid = re.match(pattern, zip)

    return valid

def main():
    # user inputs values to be validated
    phone_num = input('Phone number: ')
    social_num = input('Social security number: ')
    zip_code = input('Zip code: ')

    # run the functions to check the formats for each
    phone_valid = phone_number_val(phone_num)
    social_valid = social_security_val(social_num)
    zip_valid = zip_code_val(zip_code)

    if phone_valid is None:
        print('Phone number is invalid.')
    else:
        print('Phone number is valid.')

    if social_valid is None:
        print('Social security number is invalid.')
    else:
        print('Social security number is valid')

    if zip_valid is None:
        print('Zip code is invalid.')
    else:
        print('Zip code is valid.')


main()