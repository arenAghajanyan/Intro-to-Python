import pretty_print
def calculate_cube(x):
    return x**3
def calculate_square(x):
    return x**2

def main(a,b):
    pretty_print.simple_print(calculate_square(a))
    pretty_print.pro_print(calculate_cube(b))
main(2,4)
print(main(2,4))