# SSH公開鍵認証によるサーバー接続手順まとめ

## 🔰 概要

このドキュメントでは、SSHの**公開鍵認証**を用いて、パスワードなしで安全にサーバーへ接続する手順をまとめています。将来の再設定時に備えて記録しています。

---

## 📁 手順

```bash
1. 秘密鍵と公開鍵のペアを作成（クライアント側）
ssh-keygen -t ed25519 -C "your_email@example.com"

	•	保存先は ~/.ssh/my_ubuntu など自由に設定可能。
	•	パスフレーズは任意（空でもOK）。

作成されるファイル：
	•	秘密鍵：~/.ssh/my_ubuntu
	•	公開鍵：~/.ssh/my_ubuntu.pub

⸻

2. 公開鍵をサーバーにコピー

scp ~/.ssh/my_ubuntu.pub zin@192.168.10.107:/home/zin/.ssh/


⸻

3. サーバー側：authorized_keys に追記

cat ~/my_ubuntu.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

※authorized_keys がなければ新規作成してもOK

⸻

4. サーバー側：sshd_config 設定の確認

ファイル：/etc/ssh/sshd_config

以下のように設定されていることを確認：

PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
PasswordAuthentication no  # ※公開鍵のみで接続するなら

変更後は SSH を再起動：

sudo systemctl restart ssh


⸻

5. クライアント側：SSHで接続

ssh -i ~/.ssh/my_ubuntu zin@192.168.10.107

もしくは、.ssh/config に設定して簡略化：

vim ~/.ssh/config

Host zin-server
    HostName 192.168.10.107
    User zin
    IdentityFile ~/.ssh/my_ubuntu

接続は以下のように簡単に：

ssh zin-server


⸻

🛠 トラブルシューティング

❗ Permission denied (publickey)
	•	秘密鍵の指定漏れや、公開鍵の不一致が主な原因。

❗ known_hosts のエラー
	•	ホストキーが変わった場合：

ssh-keygen -R [IP or Hostname]

❗ デバッグで接続の様子を見る

ssh -i ~/.ssh/my_ubuntu -v zin@192.168.10.107


⸻

📝 備考
	•	~/.ssh/authorized_keys には、複数の公開鍵を追加できます（GitHubや他の端末など）。
	•	パーミッションが厳密に管理されているため、以下を守ること：

chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys


⸻

✅ 最終確認チェックリスト
	•	秘密鍵と公開鍵はセットで作成したか
	•	公開鍵がサーバーの authorized_keys に正しく登録されたか
	•	sshd_config の設定を見直したか
	•	サーバーのSSHが再起動されたか
	•	ssh コマンドで -i で正しい鍵を指定しているか

⸻
