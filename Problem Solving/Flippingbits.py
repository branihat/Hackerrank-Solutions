def flippingBits(n):
    # Calculate the maximum 32-bit unsigned integer (2^32 - 1)
    max_uint32 = 2**32 - 1

    # Flip all the bits using XOR with the maximum unsigned integer
    result = n ^ max_uint32

    return result

if __name__ == '__main__':
    q = int(input().strip())  # Read the number of queries

    for _ in range(q):
        n = int(input().strip())  # Read the integer to process
        result = flippingBits(n)
        print(result)
