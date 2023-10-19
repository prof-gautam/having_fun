def HamEncoding(msg):
    m = len(msg)
    # Step 1: Calculate the number of parity bits needed.
    k = 0
    while 2 ** k < m + k + 1:
        k += 1
    
    # Print the number of parity bits
    print(f"k = {k}")

    # Create a list to hold the final encoded message
    encoded = [''] * (m + k)

    # Step 2: Set the parity bits at their positions
    j = 0  # index for msg
    for i in range(1, m + k + 1):
        if i & (i - 1) == 0:  # Check if i is a power of 2
            encoded[i - 1] = 'P'  # Placeholder for parity bits
        else:
            encoded[i - 1] = msg[j]
            j += 1

    # Step 3: Calculate the parity bits
    for i in range(k):
        pos = 2 ** i  # Parity bit position
        parity = 0
        for j in range(1, len(encoded) + 1):
            if j & pos:  # If bit is part of the parity
                if encoded[j - 1] == '1':
                    parity ^= 1  # XOR operation
        encoded[pos - 1] = str(parity)  # Set the parity bit

    return ''.join(encoded)

def HamDecoding(rcv, k):
    n = len(rcv)
    # Initialize a list for the binary representation of the error position
    error_bin = ['0'] * k

    # Check each parity bit
    for i in range(k):
        pos = 2 ** i  # Parity bit position
        parity = 0
        for j in range(1, n + 1):
            if j & pos:  # If bit is part of the parity
                if rcv[j - 1] == '1':
                    parity ^= 1  # XOR operation
        error_bin[k - i - 1] = str(parity)  # Save the error bit

    error_pos = int(''.join(error_bin), 2)  # Convert binary to integer
    if error_pos == 0:
        return 'No error'
    else:
        # Correct the error
        corrected = list(rcv)
        corrected[error_pos - 1] = '1' if rcv[error_pos - 1] == '0' else '0'
        return f"Error at Position {error_pos}, and correct data: {''.join(corrected)}"

# Test the functions




org_sig1 = input("Enter the bits for encoding (e.g., 1101): ")
encoded_sig1 = HamEncoding(org_sig1)
print(encoded_sig1)  # Should return: '1010101'

received_sig4 = input("Enter your received number: ")
print(HamDecoding(received_sig4, 4))  # Should return: 'Error at Position 7, and correct data: 10110010011'
