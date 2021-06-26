def format_address(address_string):
    # Declare variables

    # Separate the address string into parts

    # Traverse through the address parts
    numberA = ""
    addressSpace = ""
    for i in address_string:
        if (i.isnumeric()):
            numberA = numberA + i
        else:
            break

        street = int(numberA)
        t = len(numberA)
        addressSpace = address_string[t + 1:]
        # Determine if the address part is the
        # house number or part of the street name

    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(street, addressSpace)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
