# 🌐 UbuntuサーバーにWebサーバーを構築し、クライアントのブラウザからアクセスする手順

## 🎯 目的

- サーバー（例: `192.168.10.107`）にApacheまたはNginxをインストール
- クライアントPCのブラウザでWebページを閲覧できるようにする

---

## ✅ 前提条件

- サーバーとクライアントが同一LAN内にある
- サーバーで`sudo`権限があるユーザーで操作できる
- サーバーにSSHで接続できる（例: `ssh zin@192.168.10.107`）

---

```bash
🔧 手順①：Apacheのインストール（初心者向け）
1. サーバーにSSHログイン
ssh zin@192.168.10.107

2. Apacheをインストール

sudo apt update
sudo apt install apache2 -y

3. Apacheを起動し、自動起動を設定

sudo systemctl start apache2
sudo systemctl enable apache2

4. ファイアウォール（UFW）でHTTP通信を許可（UFW有効な場合）

sudo ufw allow 'Apache'
sudo ufw enable   # まだ有効化していない場合

5. クライアントPCのブラウザで確認

http://192.168.10.107/

→ Apacheのデフォルトページが表示されれば成功！

⸻

🔧 手順②：Nginxのインストール（軽量）

1. インストール

sudo apt update
sudo apt install nginx -y

2. 起動と自動起動設定

sudo systemctl start nginx
sudo systemctl enable nginx

3. ファイアウォール設定（UFW有効な場合）

sudo ufw allow 'Nginx HTTP'

4. クライアントのブラウザで確認

http://192.168.10.107/


⸻

✏️ Webページを編集するには

Apacheの場合

cd /var/www/html
sudo nano index.html

Nginxの場合

cd /var/www/html
sudo nano index.nginx-debian.html

変更後はサービスを再起動：

sudo systemctl restart apache2   # または nginx


⸻

🛠 トラブルシューティング

問題	対策
ブラウザで表示されない	ping 192.168.10.107 をクライアントから実行して確認
サーバーが起動していない	sudo systemctl status apache2 または nginx で確認
ファイアウォールでブロックされている	sudo ufw status を確認
ページを更新しても変化がない	HTMLを保存後にサーバー再起動が必要な場合あり


⸻

📌 備考
	•	DHCPでIPアドレスが変わると接続できなくなることがあるため、固定IP設定またはhostname.localでの接続も検討してください（Avahi/Bonjourが必要）。

例：

http://192.168.10.107/

または

http://zin-PC.local/


⸻

📝 まとめ
	•	ApacheかNginxを選び、簡単にUbuntuにWebサーバーを構築できる
	•	ローカルネットワーク上のブラウザからアクセスして確認可能
	•	ファイアウォールの設定を忘れないこと

---
