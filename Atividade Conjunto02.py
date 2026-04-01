Lilian = {"Arroz", "Feijão", "Miojo", "Macarrão", "Café", "Monster", "Batata Frita", "Batata palha"}
Lara = {"Arroz", "Brocolis", "Macarrão", "Café", "Frango", "Ovo", "Batata doce"}
Brenda = {"Miojo", "Café", "Bolacha Maizena"}
Maju = {"Arroz", "Feijão", "Caviar", "Macarrão", "Café", "Cenoura", "Batata", "Tomate"}
compras_Brenda = set(Brenda)
compras_Maju = set(Maju)
compras_Lara = set(Lara)
compras_Lilian = set(Lilian)
comum = Lilian.intersection(Lara, Brenda, Maju)
compras_tot = Lilian.union(Lara, Brenda, Maju)
print(f"Total das compras: {compras_tot}")
print (f"itens comuns: {comum}")