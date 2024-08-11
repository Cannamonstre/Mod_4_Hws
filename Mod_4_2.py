def outer_function():
    def inner_function():
        print("Hi! I'm inner_function and I'm in the scope of outer_function!")
    inner_function()


try:
    inner_function()
except NameError:
    print("There's NameError appears")

# outer_function()
