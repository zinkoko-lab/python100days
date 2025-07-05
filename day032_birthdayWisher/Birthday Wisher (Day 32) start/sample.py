import smtplib
from email.mime.text import MIMEText
from email.header import Header

# メール設定
sender_email = "your_email@example.com"
sender_password = "your_email_password"
receiver_email = "receiver_email@example.com"
subject = "Pythonからのメール送信テスト"

# 本文
message = "これはPythonスクリプトで送信されたテストメールです。"

# 署名
signature = """
---
Zin Ko Ko
Python Developer
"""

# メール本文 + 署名を結合
full_message = f"{message}\n{signature}"

# メールオブジェクトの作成
msg = MIMEText(full_message, "plain", "utf-8")
msg["Subject"] = Header(subject, "utf-8")
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    # SMTPサーバーに接続
    smtp_server = smtplib.SMTP_SSL("smtp.example.com", 465)  # 例: Gmailの場合
    smtp_server.login(sender_email, sender_password)

    # メールを送信
    smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
    print("メールを送信しました")

except Exception as e:
    print(f"エラーが発生しました: {e}")

finally:
    # 接続を閉じる
    if "smtp_server" in locals() and smtp_server:
        smtp_server.quit()
