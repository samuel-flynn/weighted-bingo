class BingoItem:

    name : str
    weight : int

    def __init__(self, p_name, p_weight) -> None:
        self.name = p_name
        self.weight = p_weight

    def __str__(self) -> str:
        return self.name
