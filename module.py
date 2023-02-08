class Diak:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(' ')
        self.vezeteknev = v[0]
        self.keresztnev = v[1]
        self.magassag = int(v[2])
        self.suly = float(v[3].replace(',', '.'))
        self.nem = v[4]
        self.tti:float = self.suly / ((self.magassag/100) ** 2)