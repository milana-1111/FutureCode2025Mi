A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = A | B
D = A.union(B)
print(C)
print(D)

materials = {"кирпич", "дерево", "стекло"}
player_items = {"дерево", "гвозди"}
c = materials - player_items
print(c)

artefacts = {"меч", "щит", "кольцо", "амулет"}
player_artefacts =  {"меч", "амулет"}
f = artefacts  <= player_artefacts
print(f)

inventory = {"яблоко", "ключ", "карта"}
if 'ключ' in inventory:
    print("ключ в инвентаре")
if 'факел' not in inventory:
    inventory.add('факел')
    print(inventory)
