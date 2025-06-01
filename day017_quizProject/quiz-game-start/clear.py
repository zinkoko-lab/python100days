from os import system, name


def clear_screen():
    """
    ターミナル画面をクリアする関数。
    Windowsでは 'cls' を、それ以外のOSでは 'clear' を使用。
    """
    system("cls" if name == "nt" else "clear")
