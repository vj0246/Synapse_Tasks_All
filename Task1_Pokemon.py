import itertools

k=int(input("Please enter value of k from 1 to 10:"))
Pokedex = { 
"Pikachu": ("Electric",), 
"Charizard": ("Fire", "Flying"),
"Lapras": ("Water", "Ice"), 
"Machamp": ("Fighting",), 
"Mewtwo": ("Psychic", "Fighting"), 
"Hoopa": ("Psychic", "Ghost", "Dark"), 
"Lugia": ("Psychic", "Flying", "Water"),  
"Squirtle": ("Water",), 
"Gengar": ("Ghost", "Poison"), 
"Onix": ("Rock", "Ground") 
}

possible_combinations=()
max_len=0
items = list(["Pikachu","Charizard","Lapras","Machamp","Mewtwo","Hoopa","Lugia","Squirtle","Gengar","Onix"])
combinations = list(itertools.combinations(items,k))

for i in combinations:
    tpl=tuple()
    for j in i:
        tpl=tpl+tuple(Pokedex[j])
    st=set(tpl)
    tpl=tuple(st)
    lenn=len(tpl)
    if lenn>max_len:
        max_len=lenn
        max_features=tpl
        pokemon_list=i
print(max_len)
print(max_features)
print(pokemon_list)
