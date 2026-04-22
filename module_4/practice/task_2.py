def vert_gor(lens, napravl, simbol):
    if napravl == 'V':
        print(lens*simbol)
    else:
        for el in range(lens):
            print(simbol)

vert_gor(
    lens= 10,
    napravl= 'V',
    simbol= '*'
)

vert_gor(
    lens= 10,
    napravl= 'H',
    simbol= '*'
)