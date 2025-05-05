def bitwise_operations_on_string(input_str):
    print("Char  ASCII  AND 127  OR 127  XOR 127")    
    for char in input_str:
        ascii_val = ord(char)
        and_val = ascii_val & 127
        or_val = ascii_val | 127
        xor_val = ascii_val ^ 12
    print(char, "\t",ascii_val , "\t", and_val , "\t", or_val , "\t", xor_val)

input_string = "HelloWorld"
bitwise_operations_on_string(input_string)