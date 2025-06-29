from cryptography.fernet import Fernet

# 1. 鍵の生成
# 鍵は非常に重要です！安全に保管し、他人と共有しないでください。
# この鍵がないと、暗号化されたデータを復号できません。
key = Fernet.generate_key()
print(f"生成された鍵: {key.decode()}")  # byte型なのでdecode()して表示

# 2. Fernetオブジェクトの作成
# 生成した鍵を使ってFernetオブジェクトを作成します。
f = Fernet(key)

# 3. データの暗号化
# 暗号化したいデータをバイト型に変換する必要があります。（文字列の場合は.encode()を使う）
original_message = b"This is a secret message."
encrypted_message = f.encrypt(original_message)
print(f"暗号化されたメッセージ: {encrypted_message}")

# 4. データの復号
# 暗号化されたメッセージを復号します。
# 復号されたデータはバイト型なので、.decode()して文字列に戻します。
decrypted_message = f.decrypt(encrypted_message)
print(f"復号されたメッセージ: {decrypted_message.decode()}")

# 補足: 別のFernetオブジェクトで復号化
# 同じ鍵を使っていても、Fernetオブジェクトは新しく作成できます。
# これは、鍵さえあれば復号化できることを示しています。
f_new = Fernet(key)
decrypted_message_new = f_new.decrypt(encrypted_message)
print(f"新しいオブジェクトで復号: {decrypted_message_new.decode()}")

from tkinter import simpledialog

master_password = simpledialog.askstring(
    "Master Password", "Enter Master Password:", show="*"
)
