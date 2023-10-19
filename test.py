def binary_string_xor(s1, s2):
    return ''.join(['0' if bit1 == bit2 else '1' for bit1, bit2 in zip(s1, s2)])

def binary_string_mod(dividend, divisor):
    while len(divisor) <= len(dividend):
        if dividend[0] == '1':
            dividend = binary_string_xor(dividend[:len(divisor)], divisor) + dividend[len(divisor):]
        dividend = dividend[1:]
    return dividend

def encoding(msg, poly):
    extended_msg = msg + '0' * (len(poly) - 1)
    remainder = binary_string_mod(extended_msg, poly)
    encoded_msg = msg + remainder.zfill(len(poly) - 1)
    return encoded_msg

def decoding(rcv, poly):
    remainder = binary_string_mod(rcv, poly)
    if int(remainder) == 0:
        return 'No error'
    else:
        return 'Error'

# Polynomial remains constant
poly = '100101' # x^5 + x^2 + 1

# User inputs for original and received messages
org_string = input("Enter the original binary data: ")
encoded_message = encoding(org_string, poly)
print(f"Encoded message: {encoded_message}")

received_string = input("Enter the received binary data: ")
decoding_result = decoding(received_string, poly)
print(f"Decoding result: {decoding_result}")
