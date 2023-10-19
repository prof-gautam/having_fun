import datetime

def xor_binary(a, b):
    """
    Perform XOR (exclusive OR) operation on two binary numbers a and b.
    
    Args:
        a (str): Binary number as a string.
        b (str): Binary number as a string.

    Returns:
        str: Result of the XOR operation as a binary string.
    """
    # Ensure the binary numbers have the same length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ""
    for i in range(max_len):
        result += '1' if a[i] != b[i] else '0'
    
    return result

def encoding(msg, poly):
    """Perform CRC encoding for given message using the provided polynomial."""
    mod_msg = msg + "0"*(len(poly)-1)
    remainder = remainder_finder(mod_msg, poly)
    
    if len(remainder)<5:
        zeros_needed = 5 - len(remainder)

        remainder = '0' * zeros_needed + remainder
    encoded_output = msg + remainder
    return encoded_output

def remainder_finder(dividend, divisor):

    if int(divisor, 2) == 0:
        raise ZeroDivisionError("Division by zero (divisor is zero)")

    quotient = ""
    remainder = dividend[:len(divisor)]

    for i in range(len(divisor), len(dividend)):
        quotient_bit = remainder[0]
        if quotient_bit == '1':
            remainder = xor_binary(remainder, divisor)
        else:
            remainder = xor_binary(remainder, '0' * len(divisor))

        remainder = remainder[1:] + dividend[i]

        quotient += quotient_bit

    quotient_bit = remainder[0]
    if quotient_bit == '1':
        remainder = xor_binary(remainder, divisor)
    else:
        remainder = xor_binary(remainder, '0' * len(divisor))

    remainder = remainder[1:]

    return remainder

def decoding(rcv, poly):
    
    remainder = remainder_finder(rcv,poly)
    if int(remainder) == 0:
        return "No error Found"
    else:
        return "Error"

user_bit = input("Enter a binary number to be encoded: ")
POLY = "100101" #always fix for 4 bit number

#prints encoded message
print(f"Encoded message is : {encoding(user_bit, POLY)}")

encoded_number = input("Enter the number you received: ")


print(decoding(encoded_number, POLY))


