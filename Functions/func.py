def default_function(input_a: str) -> int:
    """
    This is the docstring of this function 
    """
    # Do stuff
    print(input_a)
    return len(input_a)



# Zip example
a = [0, 1, 2, 3, 4]
b = [1, 2, 3, 4, 5]

zipped_list = [i for i in zip(a, b)]
alternative = list(zip(a, b))

# lambda example
y = lambda a, b: a**2 + b 

# Map example
map(y, zip(a, b))