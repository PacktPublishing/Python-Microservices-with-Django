
"""
This program is created for division functionality.
"""

def div(input_01,input_02):
    try:
        print("\nfirst value: " + str(input_01) + " and second value: " + str(input_02))
        output = 0
        # Comparing the values.
        if input_02 < input_01:
            output = input_01/input_02
            print("output value", output)
        else:
            print("second value should be smaller then first value")
    # It will execute if an error occurred in the try section.
    except TypeError:
        print("Both values type should be integer or float")
    return output
