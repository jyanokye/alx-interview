#!/usr/bin/python3
""" Validation of UTF8  """


def validUTF8(data):
    """
    Determines if a given byte sequence represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    # Bit masks for the first and second bits of a byte
    FIRST_BIT_MASK = 1 << 7
    SECOND_BIT_MASK = 1 << 6

    for byte in data:
        byte_mask = 1 << 7

        if num_bytes == 0:
            # Counts the number of bytes needed to represent the current character
            while byte_mask & byte:
                num_bytes += 1
                byte_mask = byte_mask >> 1
            
            if num_bytes == 0:
                continue

            # Invalid number of bytes
            if num_bytes == 0 or num_bytes > 4:
                return False

        else:
            # Check if the current byte has the correct form
            if not (byte & FIRST_BIT_MASK and not (byte & SECOND_BIT_MASK)):
                return False

        num_bytes -= 1

    # Check if there are any left bytes that have not been processed
    if num_bytes == 0:
        return True
    else:
        return False
