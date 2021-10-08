####################################################################################
# Script written by Dan Gocan, for Programming and Algorithms 1 CMPU1026: 2021 class
# The script takes a value in Decimal, Binary or Hexadecimal and converts it to a
# value in any of the three systems. It contains a few checks, to try and prevent
# user from inputting invalid data. 

# Completed on 08 / 10 / 2021

# Website used to test values:
# https://www.rapidtables.com/convert/number/hex-to-binary.html

def conversion_master():

    # Dictionary to be used when converting from Hexadecimal
    hexadecimal_dict = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }

    bases = ["HEX", "DEC", "BIN"]
    from_base = ""
    to_base = ""
    initial_value = None

    # Asking the user to define the initial base. The script will only
    # accept values from the "bases" list. If wrong values are being 
    # introduced, it will loop
    while from_base not in bases: 
        from_base = input("Please input your initial base [DEC, BIN, HEX]").upper()

    # Asking the user to define the base they wish to convert to. 
    # The script will only accept values from the "bases" list
    while to_base not in bases:
        to_base = input("Please input your target base [DEC, BIN, HEX]").upper()

    # Stopping execution when trying to convert from and to the same base
    if (from_base == to_base):
        print("You are trying to convert from {} to {}. You're already there.".format(from_base, to_base))
        return

    # Loop to ask for an input from the user, asking for the initial value
    # that they wish to convert
    while not initial_value:

        # If converting from Decimal, we will take an integer as input
        # If user inputs anything else, the program will error
        if from_base == "DEC":
           initial_value = int(input(
               '''
               Please input a real, whole number. Anything else
               will generate an error \n
               '''
           ))

        # If converting from BIN or from HEX, we will take a string as input
        elif from_base == "BIN" or from_base == "HEX":
            initial_value = input(
                '''
                Please input a binary string [0's and 1's] or a
                hexadecimal string [0-9, A-F]. Any other values
                will generate an error \n
                ''')

            # Loop that goes over each element of the string and checks if it
            # is valid for the operation desired
            for element in initial_value:
                if from_base == "BIN" and element not in ["0", "1"]:
                    print("You have introduced an invalid character")
                    return

            for element in initial_value :
                if from_base == "HEX" and element not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
                    print("You have introduced an invalid character")
                    return

    # Here are all the functions that are doing the conversion from one
    # base to a different one. 


    # Function that converts Decimal to Binary
    def dec_to_bin(value):
        new_number = [] # a list to save the binary elements
        while value > 0.9:  
            if value % 2 < 0.5:
                new_number.append("0")
            elif value % 2 > 0.5:
                new_number.append("1")
            value = value // 2
        new_number.reverse()
        return "".join(new_number) # returns a list


    # Function that converts Decimal to Hexadecimal
    def dec_to_hex(value):
        new_number = []
        while value > 0.9:
            remainder = value % 16
            if remainder <= 9:
                new_number.append(str(remainder))
            # It was at this precise moment when I have realised that
            # there are no Switch-statements in Python
            elif remainder == 10:
                new_number.append("A")
            elif remainder == 11:
                new_number.append("B")
            elif remainder == 12:
                new_number.append("C")
            elif remainder == 13:
                new_number.append("D")
            elif remainder == 14:
                new_number.append("E")
            elif remainder == 15:
                new_number.append("F")
            value = value // 16
        new_number.reverse()
        return "".join(new_number) # returns a list

    # Function that converts Binary to Decimal
    def bin_to_dec(value):
        new_sum = 0
        power = len(value) - 1
        for element in range(0, power + 1):
            new_sum = new_sum + ((int(value[element]) * (2 ** power)))
            power = power - 1
        return new_sum

    # Function that converts Binary to Hexadecimal
    def bin_to_hex(value):
        # This will simply convert from Binary to Decimal and then to Hexadecimal.
        return dec_to_hex(bin_to_dec(value))


    # Function that converts Hexadecimal to Decimal
    def hex_to_dec(value):
        new_list = []
        new_sum = 0
        power = len(value) - 1

        # Converts Hexadecimal letters ("A", "B", etc.) in decimal characters
        for element in value:
            if element in hexadecimal_dict.keys():
                # Uses the dictionary defined at the beginning
                new_list.append(hexadecimal_dict[element])
            else:
                new_list.append(element)
        
        for element in range(0, power + 1):
            new_sum = new_sum + ((int(new_list[element]) * (16 ** power)))
            power = power - 1

        return new_sum

    # Function that converts Hexadecimal to Binary
    def hex_to_bin(value):
        return dec_to_bin(hex_to_dec(value))
            
    # Function that takes the input from the above values (from base, to base, input_value)
    # and applies the it the conversion functions, and then displays the result
    def conversion(from_base, to_base, value):

        if from_base == "DEC":
            if to_base == "BIN":
                print('''{} has been converted from base {} to base {} with a value of {}.
                '''.format(value, from_base, to_base, dec_to_bin(value)))

            elif to_base == "HEX":
                print('''{} has been converted from base {} to base {} with a value of {}.
                '''.format(value, from_base, to_base, dec_to_hex(value)))

        elif from_base == "BIN":
            if to_base == "DEC":
                print('''{} has been converted from base {} to base {} with a value of {}.
                '''.format(value, from_base, to_base, bin_to_dec(value)))

            elif to_base == "HEX":
                print('''{} has been converted from base {} to base {} with a value of {}.
                '''.format(value, from_base, to_base, bin_to_hex(value)))

        elif from_base == "HEX":
            if to_base == "DEC":
                print('''{} has been converted from base {} to base {} with a value of {}.
                '''.format(value, from_base, to_base, hex_to_dec(value)))

            elif to_base == "BIN":
                print('''{} has been converted from base {} to base {} with a value of {}.
                '''.format(value, from_base, to_base, hex_to_bin(value)))

    # Calls the nested conversion function
    conversion(from_base, to_base, initial_value)

# Calls the master function
conversion_master()
