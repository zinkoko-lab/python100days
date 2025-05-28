from os import system, name
from coffee_data import MENU, resources

# 使用可能なコーヒーの種類を取得（espresso, latte, cappuccino）
types_of_coffee = list(MENU.keys())


def clear_screen():
    """
    ターミナル画面をクリアする関数。
    Windowsでは 'cls' を、それ以外のOSでは 'clear' を使用。
    """
    system("cls" if name == "nt" else "clear")


def return_coffee_data(name_of_coffee: str):
    """
    コーヒーの種類に対応するデータを返す。

    Args:
        name_of_coffee (str): コーヒーの種類（例：'latte'）

    Returns:
        dict: コーヒーの原材料とコスト情報
    """
    return MENU[name_of_coffee]


# a function to decide the resources are enough or not, is require.
def check_resources(coffee_data: dict):
    """
    コーヒーを作るのに必要な資源が足りているかを確認する。

    Args:
        coffee_data (dict): 作成するコーヒーの情報

    Returns:
        bool: 全ての材料が足りていればTrue、不足があればFalse
    """
    coffee_ingredients = coffee_data["ingredients"]
    for ingredient, amount in coffee_ingredients.items():
        if amount > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def insert_coin():
    """
    ユーザーに小銭の数を入力させ、投入された合計金額を計算して返す。

    Returns:
        float: 合計金額（ドル）
    """
    print("Please insert coins.")
    while True:
        try:
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            break
        except ValueError:
            print("Invalid input. Money refunded and try again from start.")
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total


def return_cost(coffee_data: dict):
    """
    コーヒーの価格を取得する。

    Args:
        coffee_data (dict): コーヒー情報

    Returns:
        float: 価格（ドル）
    """
    return coffee_data["cost"]


def update_resource(coffee_data: dict):
    """
    使用した材料を減らし、売上（Money）を更新する。

    Args:
        coffee_data (dict): 作成したコーヒーの情報
    """
    coffee_ingredients = coffee_data["ingredients"]
    for ingredient, amount in coffee_ingredients.items():
        resources[ingredient] -= amount
    if "money" not in list(resources.keys()):
        resources["money"] = coffee_data["cost"]
    else:
        resources["money"] += coffee_data["cost"]


def declare_amount_of_resources():
    """
    現在の資源の量を表示する。
    """
    for resource_name, amount in resources.items():
        if resource_name in ["water", "milk"]:
            print(f"{resource_name}: {amount}ml")
        elif resource_name == "coffee":
            print(f"{resource_name}: {amount}g")
        else:
            print(f"{resource_name}: ${amount}")


# メインプログラム開始
clear_screen()
while True:
    # ユーザーにコマンドを入力させる
    usr_input = (
        input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    )

    # コーヒーの注文処理
    if usr_input in types_of_coffee:
        usr_input_coffee_data = return_coffee_data(usr_input)
        if check_resources(usr_input_coffee_data):
            inserted_amount = insert_coin()
            coffee_cost = return_cost(usr_input_coffee_data)
            if inserted_amount >= coffee_cost:
                change = inserted_amount - coffee_cost
                update_resource(usr_input_coffee_data)
                print(f"Here is ${change} in change.")
                print(f"Here is your {usr_input} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded")

    # 資源レポートの表示
    elif usr_input == "report":
        declare_amount_of_resources()

    # コーヒーマシンの電源オフ
    elif usr_input == "off":
        clear_screen()
        break

    # 不正入力は画面クリアして無視
    else:
        clear_screen()
