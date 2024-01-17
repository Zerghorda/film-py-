class Film:

    def __init__(self, sor: str):
        daraboltSor = sor.strip().split(";")
        self.cim = daraboltSor[0]
        self.rendezo = daraboltSor[1]
        self.foszereplo = daraboltSor[2]
        self.ev = int(daraboltSor[3])
        self.perc = int(daraboltSor[4])

    def __str__(self):
        return f"cím:{self.cim},rendező:{self.rendezo},főszereplő:{self.foszereplo},év:{self.ev},perc:{self.perc}"
