workshop1 = {"Ana", "Bruna", "Cleusa", "Dafne", "Helena"}
workshop2 = {"Alice", "Brenda", "Caio", "Douglas", "Heitor"}
participantes_a = set(workshop1)
participantes_b = set(workshop2)
print(f"Particiantes do primeiro evento: {participantes_a}")
print(f"Particiantes do segundo evento: {participantes_b}")
todos_participantes = participantes_a.union(participantes_b)
print(f"Total de participantes: {todos_participantes}")
print(len(todos_participantes))
ambos_workshop = participantes_a.intersection(participantes_b)
print(f"Participantes em dois workshop: {ambos_workshop}\n")
so_a = participantes_a.difference(participantes_b)
print(f"Apenas particiantes do Workshop 1: {so_a}")