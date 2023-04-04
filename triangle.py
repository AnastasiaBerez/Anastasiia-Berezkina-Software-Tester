class Triangle:
    def __init__(self):
        pass

    def perimeter(self, a, b, c):
        return a+b+c

    def area(self, a, b, c):
        return ((a+b+c)/2 * ((a+b+c)/2-a) * ((a+b+c)/2 - b) * ((a+b+c)/2 - c))**0.5

    def is_valid(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True


