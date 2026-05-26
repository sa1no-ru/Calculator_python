class Calculator:
    def __init__(self):
        self.history =[]
        self.operations={
            "+": self.add,
            "-":self.substract,
            "*": self.multiply,
            "/":self.divide,
            "**":self.power}
    def add(self,a,b):
        return a+b
    def substract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b ==0:
            return("Деление не возможно.")
        return a/b
    def power(self,a,b):
        return a**b
    def run(self):
        print("Калькулятор запущен. Доступные операции: +, -, *, /, **!!")
        print("Для выхода введите 'exit', для истории введите '/history'.")
        while True:
            try:
                user_input=input("Введите первое число (или exit):")
                if user_input.lower()==exit:
                    break
                if user_input =="/history":
                    self.show_history()
                    continue
                num1=float(user_input)
                op = input("Введите операцию(или .history):")
                if op ==self.history:
                    self.show_history()
                    continue
                if op not in self.operations:
                    print("Неизвестная операция.")
                    continue
                user_input2= input("Введите второе число:")
                if user_input2.lower()==exit:
                    break
                num2= float(user_input2)
                result= self.operations[op](num1,num2)
                self.history.append(f"{num1} {op} {num2} = {result}")
                print("Результат:", result)
            except ValueError:
                print("Ошибка:Введите число или команду!!!")
                continue
            except Exception as e:
                print("Неожиданная ошибка:", e)
    def show_history(self):
        if not self.history:
            print("История пуста")
        else:
            print("---История вычислений ---")
            for entry in self.history:
                print(entry)

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
