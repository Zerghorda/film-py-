import Film


def fileBeolvas():
    filmekLista =[]
    f = open("film.txt", "r", encoding="utf-8")
    f.readline()
    sorok = f.readlines()
    f.close()
    for i in range(len(sorok)):
        filmek = Film.Film(sorok[i])
        filmekLista.append(filmek)


    return filmekLista


def legrovidebb(cim):
    legrovidebb = ""
    for i in range(len(cim)):
        if cim[i] == "":
            legrovidebb = cim[i]
            if len(cim[i]) < len(legrovidebb):
                legrovidebb = cim[i]

    return print(f"A legrövidebb cim : {legrovidebb}")


def darab(perc):
    f = open("min110pFilmek.txt", "w", encoding="utf-8")
    db: int = 0
    for i in range(len(perc)):
        if i >= 110:
            db += 1
    f.write()
    f.close()
    return print(f"Ennyi minimum 110 perces film van : {db}")


