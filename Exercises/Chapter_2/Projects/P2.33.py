class Polynomial:
    def __init__(self, a=1, b='x', c=1):
        self._a = a
        self._b = b
        self._c = c

    def derivative(self):
        self._a = self._c * self._a
        self._c -= 1

        if self._c == 0:
            return '1'
        else:
            return str(self._a) + self._b + '^' + str(self._c)

if __name__ == '__main__':
    expr = Polynomial()
    assert(expr.derivative() == '1')
    expr = Polynomial(a=2, c=4)
    assert(expr.derivative() == '8x^3')
    assert(expr.derivative() == '24x^2')
    assert(expr.derivative() == '48x^1')
    assert(expr.derivative() == '1')
    expr = Polynomial(2, 'a', -1)
    assert(expr.derivative() == '-2a^-2')
    assert(expr.derivative() == '4a^-3')
