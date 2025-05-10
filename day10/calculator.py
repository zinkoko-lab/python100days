#!/usr/bin/env python3
import os
import logo

# ターミナルの画面をクリアする関数を定義
# os.name が 'nt' の場合は Windows ⇒ 'cls' コマンド
# それ以外（macOS / Linux）の場合は 'clear' コマンドを使用
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print(logo.logo)

def number_input(what_number: int):
    """
    Prompt user for a number and return it as an integer.
    """
    while True:
        try:
            number = int(input(f"What is the {what_number} number?: "))
            break
        except ValueError:
            print("Your number is invalid. Please try again. ")
    return number

# 各四則演算を関数として定義
def add(num1: int, num2: int):
    return num1 + num2

def subtract(num1: int, num2: int):
    return num1 - num2

def multiply(num1: int, num2: int):
    return num1 * num2

def divide(num1: int, num2: int):
    return num1 / num2

operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def operate(num1: int, num2: int, operation: str):
    # 演算種別に応じて処理を実行
    try:
        return operations_dict[operation](num1, num2)
    # 0除算やオーバーフロー、その他の予期せぬエラーを処理
    except ZeroDivisionError:
        print("Division by zero detected. The result is considered infinity.")
        return "Infinity"
    except OverflowError:
        print("The number you entered is too large to be processed.")
        return "OverflowError"
    except Exception as e:
        print(f"Unexpected error: {e}. Please contact support if the problem persists.")
        return e

start_new_calculation = True
while start_new_calculation:
    first_number = number_input("first")

    use_last_result = True
    while use_last_result:
        # 利用可能な演算子の表示と選択
        print("+\n-\n*\n/")
        operations = ["+", "-", "*", "/"]
        while True:
            user_operation = input("Pick an operation: ").strip()
            if user_operation in operations:
                break
            else:
                print("Invalid operation. Please try again.")

        next_number = number_input("next")

        result = operate(num1=first_number, num2=next_number, operation=user_operation)
        print(f"{first_number} {user_operation} {next_number} = {result}")

        # 続けるか、新しい計算にするかの選択
        what_next = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if what_next == 'y':
            first_number = result
        elif what_next == 'n':
            use_last_result = False
        else:
            use_last_result = False
            start_new_calculation = False

print("Goodbye!")
