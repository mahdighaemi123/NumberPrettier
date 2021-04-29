from persiantools import characters, digits

import math

_max_digit = 12
_split_digit = True
_simplefy = False

numbers = {
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
}

number_formats = {
    '-',
    '.',
    ','
}

number_formats = [
    {'number':1_000_000_000,'name':'B'},
    {'number':1_000_000,'name':'M'},
    {'number':1_000,'name':'T'},
]

number_formats.sort(key=lambda number_format:number_format['number'],reverse=True)


def normalize_float(data_value):

    new_value = None

    data_value = normalize_str(data_value)
    new_value = float(data_value)


    return new_value


def normalize_int(data_value):

    new_value = None
    new_value = int(normalize_float(data_value))

    return new_value


def normalize_str(data_value):

    new_value = None

    new_value = str(data_value)
    new_value = digits.fa_to_en(new_value)
    new_value = characters.ar_to_fa(new_value)

    return new_value
    

def normalize_bool(data_value,default=False):

    new_value = None

    try:
        new_value = str(data_value)
    except Exception as ex:
        print('str Exception',data_value,ex)
        new_value = str(default)

    return new_value.upper() == 'True'.upper()


def parse_float_as_str(input_number):
    input_number = normalize_str(input_number)

    input_number = normalize_float(input_number)
    input_number = format(input_number, f'.12f') 

    return input_number

def parse_int_as_str(input_number):
    input_number = normalize_str(input_number)

    input_number = normalize_float(input_number)
    input_number = format(input_number, f'.0f') 

    return input_number

def parse_int_str_as_str(input_number):
    input_number = normalize_str(input_number)
    input_number = input_number.split('.')[0]
    return input_number


def remove_zero_from_end(input_number):
    input_number = normalize_str(input_number)
    result = ''
    find_first_number = False

    for character in input_number[::-1]:
        if find_first_number or character != '0':
            result += character
            find_first_number = True

    result = result[::-1]
    return result


def chrs_splitter(input_str,chrs):
    input_str = normalize_str(input_str)
    chrs = set(chrs)
    result = ['']

    for character in input_str:
        if character in chrs:
            result.append('')

        else:
            result[len(result)-1] += character

    return result

    
def number_prettier(input_number,max_digit=_max_digit,split_digit=_split_digit,simplefy=_simplefy):

    str_number = normalize_str(input_number)
    str_number_spilited = chrs_splitter(str_number,['_',' '])

    number = str_number_spilited[0]
    number = normalize_float(number)
    number = parse_float_as_str(number) 

    if len(str_number_spilited) >1:
        input_number = number +' '+ "".join(str_number_spilited[1:])
    else:
        input_number = number + "".join(str_number_spilited[1:])

    str_number = normalize_str(input_number)
    str_number_spilited = chrs_splitter(str_number,['.',' '])

    main_number = str_number_spilited[0]
    number_format_name = ''


    if len(str_number_spilited) > 1:
        division_number = str_number_spilited[1]
    else:
        division_number = '0'


    if len(str_number_spilited) > 2:
        others = ''.join(str_number_spilited[2:])
    else:
        others = ''

    all_number = normalize_float(f'{main_number}.{division_number}')
    main_number = normalize_float(main_number)

    negative = all_number < 0

    negative_symbol = '-'

    if negative:
        main_number = main_number *  -1

    main_number = abs(main_number)

    if simplefy:

        for number_format in number_formats:
            if  main_number >= number_format['number']:
                number_format_name = number_format['name']

                new_number = main_number // number_format['number']

                division_number = f"{(main_number - (new_number * number_format['number']) )}"
                main_number = new_number // 1

                break

    if split_digit:

        spilted_main = ''
        for index,left_chr in enumerate(parse_int_as_str(main_number)[::-1]):
        
            spilted_main = left_chr + spilted_main

            if (index+1) % 3 == 0 and (index+1) < len(parse_int_as_str(main_number)):
                spilted_main = ',' + spilted_main

        main_number = spilted_main


    result = ''

    if negative:
        result += negative_symbol

    result += f'{parse_int_str_as_str(main_number)}'

    if normalize_float(division_number) != 0:
        result += f'.{remove_zero_from_end(parse_int_str_as_str(division_number)[0:max_digit])}'

    if number_format_name != '':
        result += f' {number_format_name}'
    
    if others != '' :
        result += f' {others}'

    return result


def is_number(input_number):
    input_number = str(input_number)

    for chacacter in input_number:

        if chacacter not in numbers and chacacter not in number_formats:
            return False

    return True