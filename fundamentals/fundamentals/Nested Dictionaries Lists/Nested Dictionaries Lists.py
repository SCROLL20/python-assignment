likes = {"color":"blue","fruit":"apple","pet":"dog"}
dojo = {
    'locations':['San jose','seattle','dallas','chicago','tusla','dc','burbank'],
    'instructors':['Michael','Amy','Eduardo','Josh','Garham','Patrick','Minh','Devon']
}
for key in dojo:
    print(f"{len(dojo[key])}{key}")
    for value in dojo[key]:
        print(value)