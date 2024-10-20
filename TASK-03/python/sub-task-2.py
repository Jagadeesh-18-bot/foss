# Defines the files
input_file = 'input.txt'
output_file = 'output.txt'

# Reads the information from input.txt
with open(input_file, 'r') as infile:
    content = infile.read()

# Writes the content to output.txt
with open(output_file, 'w') as outfile:
    outfile.write(content)

print(f"Content successfully copied from {input_file} to {output_file}.")

