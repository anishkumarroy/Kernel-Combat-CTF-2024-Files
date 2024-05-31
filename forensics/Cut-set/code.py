def reverse_chunks(text, chunk_size=8):
    # Split the text into chunks of size chunk_size
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    reversed_chunks = []

    # Reverse each chunk and add it to the list of reversed chunks
    for chunk in chunks:
        reversed_chunks.append(chunk[::-1])

    # Join the reversed chunks and return the result
    return ''.join(reversed_chunks)

def reverse_pairs(text, chunk_size=2):
    # Split the text into chunks of size chunk_size
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    reversed_chunks = []

    # Reverse each chunk and add it to the list of reversed chunks
    for chunk in chunks:
        reversed_chunks.append(chunk[::-1])

    # Join the reversed chunks and return the result
    return ''.join(reversed_chunks)

# Read text from the file
filename = 'hex_data'  # Replace 'your_file.txt' with the path to your file
with open(filename, 'r') as file:
    text = file.read().strip()

# Reverse every 8 characters in the text
reversed_text = reverse_chunks(text)

# Reverse every pair of digits in the reversed text
reversed_pairs = reverse_pairs(reversed_text)

# Write the output to the final text file
output_filename = 'output_file.txt'  # Replace 'output_file.txt' with the desired output file name
with open(output_filename, 'w') as file:
    file.write(reversed_pairs)

print("Output written to", output_filename)
