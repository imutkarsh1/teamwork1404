def get_numbers():
    numbers = []
    n = int(input("Enter the number of numbers: "))
    for _ in range(n):
        num = float(input("Enter a number: "))
        numbers.append(num)
    return numbers

def square_number(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2

def display_numbers(numbers):
    print("Squared numbers:")
    for num in numbers:
        print(num)

def main():
    numbers = get_numbers()
    square_number(numbers)
    display_numbers(numbers)

if __name__ == "__main__":
    main()