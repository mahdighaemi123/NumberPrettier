import number_prettier_tool


print(
    number_prettier_tool.number_prettier(
        input_number='1234567890123456789',
        simplefy = True,
        split_digit = True,
        max_digit = 12,
    )
) # -> 1,234,567,890.123456768 B

print(
    number_prettier_tool.number_prettier(
        input_number='1234567890123456789',
        simplefy = True,
        split_digit = True,
        max_digit = 2,
    )
) # -> 1,234,567,890.12 B

print(
    number_prettier_tool.number_prettier(
        input_number='1234567890123456789',
        simplefy = False,
        split_digit = True,
        max_digit = 2,
    )
) # -> 1,234,567,890,123,456,768

print(
    number_prettier_tool.number_prettier(
        input_number='1234567890123456789',
        simplefy = True,
        split_digit = False,
        max_digit = 2,
    )
) # -> 1234567890.12 B