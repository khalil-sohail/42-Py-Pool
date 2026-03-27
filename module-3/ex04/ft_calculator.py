class calculator:
    """calculator"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = 0
        for a, b in zip(V1, V2):
            res += a * b
        print(f"Dot product is: {res}")
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = [float(a) + float(b) for a, b in zip(V1, V2)]
        print(f"Add Vector is: {res}")
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = [float(a) - float(b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
