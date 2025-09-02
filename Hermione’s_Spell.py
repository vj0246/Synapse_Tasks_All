runes=str(input("Please enter the string runes")).lower()
def transform_text(runes):
    checklist = {"l":0, "u":0, "m":0, "o":0, "s":0}
    min_chars = 0
    for i in runes.lower():
        if i in checklist.keys():
            checklist[i] = 1
        min_chars += 1
        if list(checklist.values()).count(0) == 0:
            return min_chars
    return -1
print(transform_text("adfshjkleruiowqmn"))