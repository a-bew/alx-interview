#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
  # Initialize flags
  single_byte = True 
  two_bytes = False

  for byte in data:
    # Mask to check 8 least significant bits
    byte &= 0b11111111
    
    # Check for single byte character
    if single_byte: 
      if byte < 0b10000000:
        continue
      elif byte >= 0b11000000 and byte < 0b11100000:
        two_bytes = True
      else:
        return False
    
    # Check for multi-byte characters
    elif two_bytes:
      if byte >= 0b10000000 and byte < 0b11000000:
        two_bytes = False
      else:
        return False

  return not two_bytes
