def convert_file_to_uppercase(input_path: str, output_path: str):
    try:
        with open(input_path, "r") as file:
            content = file.read().upper()

        with open(output_path, "w") as new_file:
            new_file.write(content)

        print(f"File written to: {output_path}")
    except FileNotFoundError:
        print(f"Error: {input_path} not found.")
    except IOError as e:
        print(f"I/O error: {e}")

convert_file_to_uppercase("example.txt", "new_file.txt")