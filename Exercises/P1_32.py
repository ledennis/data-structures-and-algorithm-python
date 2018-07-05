class Calculator:
    operations = ['+', '-', '/', '*', '=']

    def run(self):
        print('Calculator is running, please input calculations.')
        self.solve()

    def solve(self):
        firstInput = self.numInput()
        secondInput = self.opInput()
        thirdInput = self.numInput()
        calc = self.operate(firstInput, secondInput, thirdInput)
        op = self.opInput()
        while (op != '='):
            print(calc)
            num = self.numInput()
            calc = self.operate(calc, op, num)
            op = self.opInput()
        print(calc)

    def numInput(self):
        inp = input()
        try:
            inp = float(inp)
            return inp
        except ValueError:
            print('Please input a number.')
            self.numInput()

    def opInput(self):
        inp = input()
        try:
            if (self.operations.index(inp) >= 0):
                return inp
        except ValueError:
            print('Please input only an operation.')
            self.opInput()

    def operate(self, num1, op, num2):
        if (op == '+'):
            return num1 + num2
        elif (op == '-'):
            return num1 - num2
        elif (op == '*'):
            return num1 * num2
        elif (op == '/'):
            return num1 / num2
        else:
            raise ValueError('Error handling was done poorly.')


calc = Calculator()
calc.run()
