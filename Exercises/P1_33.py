class Calculator:
    operations = ['+', '-', '/', '*', '=', 'c']

    def run(self):
        print('Calculator is running, please input calculations.')
        self.solve()

    def solve(self):
        calc = 0
        op = ''
        inp = ''
        while (inp != '='):
            inp = self.userInput()
            if inp == '=':
                print(calc)

            elif (isinstance(inp, str)):
                op = inp

            elif op != '':
                calc = self.operate(calc, op, inp)

            else:
                calc = inp

    def userInput(self):
        inp = input()
        try:
            if (self.operations.index(inp) >= 0):
                if inp == 'c':
                    print(0)
                    self.solve()
                else:
                    return inp
        except ValueError:
            try:
                inp = float(inp)
                return inp
            except ValueError:
                print('Please input a number or operation.')
                self.userInput()

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
