# Modifying Global Scope

# # おすすめしないコード
# 関数の中(local scope)から Global Scope にあるものを更新したりするのは
# バグの原因になるのでおすすめしない
# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# increase_enemies() # enemies inside function: 2
# print(f"enemies outside function: {enemies}") # enemies outside function: 2

# おすすめするコード
current_enemies = 1

def increase_enemies(enemy: int):
    enemy += 1
    return enemy

print(f"Before increase enemies, current_enemies = {current_enemies}")
updated_enemies = increase_enemies(current_enemies)
print(f"After increase enemies, updated_enemies = {updated_enemies}")
