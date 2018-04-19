def input_positive_integer():
    while True:
        try:
            int_input = int(input("Input a number: "))
            if int_input > 0:
                return int_input
                break
            else:
                print("Please input a positive integer!")
        except ValueError:
            print("Please input a positive integer!")
