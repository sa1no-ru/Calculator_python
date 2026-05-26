"""
Простой интерактивный калькулятор на Python с историей вычислений.
"""


class Calculator:
    """Класс калькулятора с поддержкой базовых математических операций."""

    def __init__(self):
        """Инициализация калькулятора с пустой историей."""
        self.history = []
        self.operations = {
            "+": self.add,
            "-": self.substract,
            "*": self.multiply,
            "/": self.divide,
            "**": self.power
        }

    def add(self, a, b):
        """Сложение двух чисел."""
        return a + b

    def substract(self, a, b):
        """Вычитание второго числа из первого."""
        return a - b

    def multiply(self, a, b):
        """Умножение двух чисел."""
        return a * b

    def divide(self, a, b):
        """Деление первого числа на второе с защитой от деления на ноль."""
        if b == 0:
            return "❌ Деление на ноль невозможно!"
        return a / b

    def power(self, a, b):
        """Возведение числа в степень."""
        return a ** b

    def run(self):
        """Запуск интерактивного режима калькулятора."""
        print("\n" + "=" * 50)
        print("🧮 КАЛЬКУЛЯТОР ЗАПУЩЕН")
        print("=" * 50)
        print("📋 Доступные операции: +, -, *, /, **")
        print("💾 Для просмотра истории введите: /history")
        print("❌ Для выхода введите: exit")
        print("=" * 50 + "\n")

        while True:
            try:
                user_input = input("📱 Введите первое число (или команду): ").strip()

                # Проверка команды выхода
                if user_input.lower() == "exit":
                    print("\n✅ Спасибо за использование калькулятора!\n")
                    break

                # Проверка команды истории
                if user_input.lower() == "/history":
                    self.show_history()
                    continue

                # Преобразование в число
                num1 = float(user_input)

                # Ввод операции
                op = input("➕➖✖️➗ Введите операцию: ").strip()

                # Проверка команды истории
                if op.lower() == "/history":
                    self.show_history()
                    continue

                # Проверка корректности операции
                if op not in self.operations:
                    print("⚠️  Неизвестная операция! Используйте: +, -, *, /, **\n")
                    continue

                # Ввод второго числа
                user_input2 = input("📱 Введите второе число: ").strip()

                # Проверка команды выхода
                if user_input2.lower() == "exit":
                    print("\n✅ Спасибо за использование калькулятора!\n")
                    break

                num2 = float(user_input2)

                # Выполнение операции
                result = self.operations[op](num1, num2)

                # Добавление в историю
                self.history.append(f"{num1} {op} {num2} = {result}")

                # Вывод результата
                print(f"\n✅ Результат: {result}\n")

            except ValueError:
                print("⚠️  Ошибка: Введите корректное число!\n")
                continue
            except Exception as e:
                print(f"❌ Неожиданная ошибка: {e}\n")

    def show_history(self):
        """Вывод истории всех вычислений."""
        if not self.history:
            print("\n📭 История пуста\n")
        else:
            print("\n" + "=" * 50)
            print("📜 ИСТОРИЯ ВЫЧИСЛЕНИЙ")
            print("=" * 50)
            for i, entry in enumerate(self.history, 1):
                print(f"{i}. {entry}")
            print("=" * 50 + "\n")


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
