# Desafio 1
sorteios = ['sorteio1', 'sorteio2', 'sorteio3']
participantes = ['joel', 'jessica', 'maria', 'cris', 'Larissa', 'rafael', 'marcus', 'john']
pprint({sorteio: random.choice(participantes) for sorteio in sorteios})


# Desafio 2
grupos = ['grupo 1', 'grupo 2', 'grupo 3']
pprint({grupo: [random.randint(1, 101) for i in range(5)] for grupo in grupos})
