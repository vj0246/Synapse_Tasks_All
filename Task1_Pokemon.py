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
def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)

n_combinations=int(factorial(10)/(factorial(10-k)*factorial(k)))

possible_combinations=()
max_len=0
items = list(["Pikachu","Charizard","Lapras","Machamp","Mewtwo","Hoopa","Lugia","Squirtle","Gengar","Onix"])
combo=[]
combinations = list(itertools.combinations(items,k))

#print(combinations[0][1])
for i in combinations:
    tpl=tuple()
    for j in i:
        tpl=tpl+tuple(Pokedex[j])
        print(tpl)
    st=set(tpl)
    tpl=tuple(st)
    lenn=len(tpl)
    if lenn>max_len:
        max_len=lenn
        sett=tpl
print(max_len)
