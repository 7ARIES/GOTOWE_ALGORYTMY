slownik = [{"szt": 500, "towar": "towar_A"}, {"szt": 400, "towar": "towar_B"}]

lista_kluczy = []
lista_values = []

for k in slownik:
    lista_kluczy.append(f'szt: {list(k.items())[0][1]}')
    lista_values.append(f'towar: {list(k.items())[1][1]}')

print(lista_kluczy)
print(lista_values)
# metoda 2 prosta podaje jedynie wartości
szt = [e.get("szt") for e in slownik]
# I to samo dla towar:
towar = [e.get("towar") for e in slownik]

print(szt)
print(towar)

print(slownik[1]['towar'])  # wyszukiwanie elemtów w słowniku
