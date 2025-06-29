from random import randint, choice, shuffle
from characters import letters, numbers, symbols
import sys, os
import tkinter as tk
from tkinter import messagebox, simpledialog
import pyperclip
import json
from pathlib import Path
from cryptography.fernet import Fernet
import base64
import hashlib  # hashlibをインポート

# --- グローバル変数としてFernetオブジェクトと鍵を保持 ---
fernet_obj = None
encryption_key = None
MASTER_PASSWORD_FILE = "master_password.key"
FERNET_KEY_FILE = "fernet.key"


# ---------------------------- GET FILE PATH(logo_image) ------------------------------- #
# PyInstaller環境でもファイルを取得できるパスを返す
def get_resource_path(relative_path):
    try:
        # PyInstallerで実行されている場合
        base_path = sys._MEIPASS
    except AttributeError:
        # 開発環境の場合
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# ---------------------------- PATH FOR USER DATA ------------------------------- #
def get_user_data_path(filename="data.json"):
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller app化後の環境
        user_dir = (
            Path.home() / "Documents" / "MyPasswordManagerData"
        )  # ユーザー固有のディレクトリに変更
    else:
        # 開発環境
        user_dir = Path.cwd()

    user_dir.mkdir(parents=True, exist_ok=True)
    return user_dir / filename


json_data_path = get_user_data_path()
master_password_path = get_user_data_path(MASTER_PASSWORD_FILE)
fernet_key_path = get_user_data_path(FERNET_KEY_FILE)

print(f"Using data path: {json_data_path}")
print(f"Master password path: {master_password_path}")
print(f"Fernet key path: {fernet_key_path}")


# ---------------------------- MASTER PASSWORD HANDLING ------------------------------- #
def hash_password(password):
    """パスワードをSHA256でハッシュ化する"""
    # パスワードをバイト列にエンコードし、ハッシュ化
    return hashlib.sha256(password.encode()).hexdigest()


def setup_master_password():
    """初回起動時にマスターパスワードを設定し、ハッシュ化して保存する"""
    if master_password_path.exists():
        return True  # すでに設定済みなら何もしない

    while True:
        password = simpledialog.askstring(
            "Set Master Password", "Enter your new master password:"
        )
        if password:
            confirm_password = simpledialog.askstring(
                "Confirm Master Password", "Re-enter your master password:"
            )
            if password == confirm_password:
                hashed_password = hash_password(password)  # パスワードをハッシュ化

                with open(master_password_path, "w") as f:
                    f.write(hashed_password)  # ハッシュ化されたパスワードを保存
                os.chmod(master_password_path, 0o600)  # オーナーだけ読み書き可能

                generate_and_save_fernet_key()  # Fernet鍵も同時に生成

                messagebox.showinfo("Success", "Master password has been set.")
                return True
            else:
                messagebox.showerror("Error", "Passwords do not match.")
        else:
            messagebox.showerror("Error", "Master password is required.")
            sys.exit()  # 入力がなければ終了


def verify_master_password():
    """マスターパスワードを検証する"""
    if not master_password_path.exists():
        return setup_master_password()  # まだ設定されていなければ設定プロセスを開始

    with open(master_password_path, "r") as f:
        stored_hashed_password = f.read().strip()  # 保存されているハッシュ値を取得

    while True:
        entered_password = simpledialog.askstring(
            "Master Password", "Enter your master password:", show="*"
        )
        if entered_password:  # 入力があった場合
            entered_hashed_password = hash_password(
                entered_password
            )  # 入力されたパスワードをハッシュ化
            if (
                entered_hashed_password == stored_hashed_password
            ):  # ハッシュ値を比較して認証
                messagebox.showinfo("Success", "Master password verified.")
                return True
            else:
                messagebox.showerror(
                    "Authentication Failed", "Incorrect master password."
                )
        elif entered_password is None:  # キャンセルされた場合
            messagebox.showerror(
                "Authentication Failed",
                "Master password input was canceled. Exiting application.",
            )
            sys.exit()
        else:  # 空の入力があった場合
            messagebox.showerror(
                "Authentication Failed", "Master password cannot be empty."
            )


# ---------------------------- FERNET KEY HANDLING ------------------------------- #
def generate_and_save_fernet_key():
    """Fernet鍵を生成し、ファイルに保存する"""
    global encryption_key
    key = Fernet.generate_key()
    with open(fernet_key_path, "wb") as key_file:
        key_file.write(key)
    os.chmod(fernet_key_path, 0o600)  # オーナーだけ読み書き可能
    encryption_key = key
    print(f"Fernet key generated and saved: {fernet_key_path}")


def load_fernet_key():
    """ファイルからFernet鍵を読み込む"""
    global encryption_key, fernet_obj
    if not fernet_key_path.exists():
        # 鍵ファイルが存在しない場合は、マスターパスワード設定時に鍵も生成されるため、ここで生成しない
        # マスターパスワードが設定済みなら、何らかの理由で鍵ファイルがないのでエラーとする
        if master_password_path.exists():
            messagebox.showerror("Error", "Fernet key file not found.")
            sys.exit()
        else:
            # マスターパスワードも鍵もなければ、マスターパスワード設定関数で両方生成される
            return False

    with open(fernet_key_path, "rb") as key_file:
        encryption_key = key_file.read()
    fernet_obj = Fernet(encryption_key)
    print(f"Fernet key loaded: {fernet_key_path}")
    return True


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passwd_gen():
    num_letters = randint(8, 10)
    num_nums = randint(2, 4)
    num_symbols = randint(2, 4)

    password = [choice(letters) for _ in range(num_letters)]
    password += [choice(numbers) for _ in range(num_nums)]
    password += [choice(symbols) for _ in range(num_symbols)]

    shuffle(password)
    password = "".join(password)
    passwd_entry.delete(0, tk.END)  # Clear existing password
    passwd_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD (Encrypted) ------------------------------- #
def save():
    website = web_entry.get().lower()
    id_val = email_entry.get()
    passwd = passwd_entry.get()

    if not fernet_obj:
        messagebox.showerror("Error", "Encryption key not loaded.")
        return

    # パスワードを暗号化
    try:
        encrypted_passwd = fernet_obj.encrypt(
            passwd.encode()
        ).decode()  # Encode to bytes, encrypt, then decode to string
    except Exception as e:
        messagebox.showerror("Encryption Error", f"Failed to encrypt password: {e}")
        return

    new_data = {
        website: {"email": id_val, "password": encrypted_passwd}
    }  # Save encrypted password

    if len(website) < 1 or len(passwd) < 1:
        messagebox.showwarning(message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            message=f"Do you want to save the following details?\nWebsite: {website}\nEmail/Username: {id_val}\nPassword: {'*' * len(passwd)}\n(Password will be encrypted)",
        )
        if is_ok:
            try:
                with open(file=json_data_path, mode="r") as f:
                    # Reading old data
                    data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                # If file doesn't exist or is empty, create new and write new_data
                with open(file=json_data_path, mode="w") as f:
                    json.dump(new_data, f, indent=4)
                # Read/write only for owner
                os.chmod(json_data_path, 0o600)
            else:
                if website in data:
                    is_ok = messagebox.askokcancel(
                        message=f"Details for {website} already exist.\nDo you want to overwrite the existing data?"
                    )
                    if not is_ok:  # Abort if not overwriting
                        return
                # Updating old data with new data
                data.update(new_data)
                # If successfully read, write updated data
                with open(file=json_data_path, mode="w") as f:
                    json.dump(data, f, indent=4)
            finally:
                web_entry.delete(0, tk.END)
                passwd_entry.delete(0, tk.END)


# ---------------------------- FIND PASSWORD (Decrypted) ------------------------------- #
def find_passwd():
    website = web_entry.get().lower()

    if not fernet_obj:
        messagebox.showerror("Error", "Encryption key not loaded.")
        return

    if len(website) > 0:
        try:
            with open(file=json_data_path, mode="r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showwarning(message="No Data File Found.")
        else:
            try:
                email = data[website]["email"]
                encrypted_password = data[website]["password"]
                # Decrypt the encrypted password
                decrypted_password = fernet_obj.decrypt(
                    encrypted_password.encode()
                ).decode()  # Encode to bytes, decrypt, then decode to string
                pyperclip.copy(
                    decrypted_password
                )  # Copy decrypted password to clipboard
            except KeyError:
                messagebox.showwarning(message=f"No details for {website} found.")
            except Exception as e:
                messagebox.showerror(
                    "Decryption Error",
                    f"Failed to decrypt password. Key might be incorrect or data corrupted.\nError: {e}",
                )
            else:
                messagebox.showinfo(
                    title=website,
                    message=f"Email/Username: {email}\nPassword: {decrypted_password}\n\nPassword copied to clipboard.",
                )


# ---------------------------- UI SETUP ------------------------------- #
def setup_ui():
    global window, web_entry, email_entry, passwd_entry

    window = tk.Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)

    canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
    image_data_path = get_resource_path("logo.png")
    logo_image = tk.PhotoImage(file=image_data_path)
    canvas.create_image(100, 100, image=logo_image)
    canvas.grid(row=0, column=0, columnspan=3)

    # labels
    website_label = tk.Label(text="Website:", width=11, anchor="e")
    website_label.grid(row=1, column=0, padx=1)

    name_label = tk.Label(text="Email/Username:", width=11, anchor="e")
    name_label.grid(row=2, column=0, padx=1)

    passwd_label = tk.Label(text="Password:", width=11, anchor="e")
    passwd_label.grid(row=3, column=0, padx=1)

    # entry
    web_entry = tk.Entry(width=21)
    web_entry.focus()
    web_entry.grid(row=1, column=1, sticky="w")

    email_entry = tk.Entry(width=39)
    email_entry.insert(0, "example@abcmail.com")
    email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

    passwd_entry = tk.Entry(width=21)
    passwd_entry.grid(row=3, column=1, sticky="w")

    # buttons
    pwd_gen_btn = tk.Button(
        text="Generate Password",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=passwd_gen,
    )
    pwd_gen_btn.grid(row=3, column=2)

    add_btn = tk.Button(
        text="Add",
        width=36,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=save,
    )
    add_btn.grid(row=4, column=1, columnspan=2)

    search_btn = tk.Button(
        text="Search",
        width="13",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=find_passwd,
    )
    search_btn.grid(row=1, column=2)

    window.mainloop()


# ---------------------------- APPLICATION START ------------------------------- #
if __name__ == "__main__":
    # マスターパスワードの検証または設定
    if verify_master_password():
        # Fernet鍵のロード
        if load_fernet_key():
            setup_ui()
        else:
            # ここに到達するのは、マスターパスワードは設定されているがFernet鍵がない場合
            # これは通常発生しないはずだが、念のためエラー処理
            messagebox.showerror(
                "Error",
                "Failed to load Fernet key. Exiting application.",
            )
            sys.exit()
    else:
        # マスターパスワードの認証に失敗した場合、verify_master_password()内でsys.exit()が呼ばれる
        pass
