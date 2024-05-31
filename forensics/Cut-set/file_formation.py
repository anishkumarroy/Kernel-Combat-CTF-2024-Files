def hex_to_png(hex_data, output_filename):
    # Convert hexadecimal string to bytes
    byte_data = bytes.fromhex(hex_data)

    # Write the bytes to a PNG file
    with open(output_filename, 'wb') as file:
        file.write(byte_data)

    print("PNG file", output_filename, "created successfully.")

# Function to read hex data from a file
def read_hex_from_file(input_filename):
    # Read hexadecimal data from the file
    with open(input_filename, 'r') as file:
        hex_data = file.read().strip()

    return hex_data

# Example usage
input_filename = 'output_file.txt'  # Replace 'hex_data.txt' with the path to your file
output_filename = 'output_image.png'  # Output PNG file name

# Read hexadecimal data from the file
hex_data = read_hex_from_file(input_filename)

# Convert hexadecimal data to PNG file
hex_to_png(hex_data, output_filename)
