def multiply_digits(number):
    result = 1
    while number > 0:
        digit = number % 10
        result *= digit
        number //= 10
    return result


def main():

    user_input = input("Введіть ціле число: ")

    try:
        number = int(user_input)
    except ValueError:
        print("Введене значення не є цілим числом.")
        return

    number = abs(number)

    while number > 9:
        number = multiply_digits(number)

    print(f"Результат: {number}")


if __name__ == "__main__":
    main()
