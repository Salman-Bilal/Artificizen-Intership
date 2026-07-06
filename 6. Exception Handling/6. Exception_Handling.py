"""
Question: 6: Write a try/except block that gracefully handles at least three different exception types (ValueError, ZeroDivisionError, FileNotFoundError).

"""

def safe_divide_from_file(filename: str):
    try:
        
        with open(filename, "r", encoding="utf-8") as file:
            file_data = file.read().strip()
        
        numerator = int(file_data)
        
        user_input = input(f" File loaded '{filename}' ({numerator}). Enter a number to divide by: ")
        denominator = int(user_input)
        
        result = numerator / denominator
        print(f" Success! {numerator} / {denominator} = {result}")

    except FileNotFoundError:
        print(f" Error: System could not find the file '{filename}'. Please verify the filename.")

    except ValueError:
        print(" Error: Invalid value! The file content or your input must be a clean integer.")

    except ZeroDivisionError:
        print(" Error: Mathematical impossibility! You cannot divide a number by zero.")

    except Exception as generic_error:
        print(f" An unexpected system error occurred: {generic_error}")


safe_divide_from_file("missing_file.txt")
safe_divide_from_file("invalid_number.txt")
safe_divide_from_file("good_number.txt")
