# Llegir la llista de candidats
num_candidates = int(input("Introdueix la quantitat de candidats: "))
candidates = []

for i in range(num_candidates):
    candidate_name = input(f"Introdueix el candidat {i + 1}: ")
    candidates.append(candidate_name)

# Preguntar quin candidat hi ha a cada posició
while True:
    position = int(input("Introdueix la posició (-1 per acabar): "))

    if position == -1:
        break

    if 1 <= position <= num_candidates:
        candidate_at_position = candidates[position - 1]
        print(candidate_at_position)
    else:
        print("Posició no vàlida. Torna-ho a provar.")
