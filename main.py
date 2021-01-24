import random

a = [
"Niemcy",
"LGBT",
"Strajk kobiet",
"Opozycja",
"Hejt",
"Tusk"
]
b = [
" atakuje ",
" propaguję ideologię ",
" znieważa ",
" prowokuje ",
" liże "
]
c = [
"polaków",
"uczestników motel polska",
"papieża",
"patriotów",
"rząd"
]



print(a[random.randint(0, len(a)-1)]+b[random.randint(0, len(b)-1)]+c[random.randint(0, len(c)-1)])