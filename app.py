import sys

def calculate(expression):
    try:
        # Evaluate the expression using eval()
	# We dont have to change anything because eval is the calculator...
        result = eval(expression)
        return result
    except Exception as e:
        raise ValueError("Invalid expression")

def main():
    if len(sys.argv) != 2:
        print("All arithmetic is supported\n Usage: python app.py <expression>")
        return

    # Get the expression from the command-line argument
    expression = sys.argv[1]
    try:
        # Calculate and print the result
        result = calculate(expression)
        print( result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
