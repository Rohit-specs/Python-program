filename = "example.txt"

try:
    with open(filename, 'x') as file:
        file.write("This file was created using 'x' mode\n")
        file.write("it will create error\n")
    print(f"File '{filename}' created successfully.")
except FileExistsError:
    print(f"Error: File '{filename}' already exists!")