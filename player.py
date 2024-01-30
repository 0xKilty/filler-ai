class Player:
    def __init__(self, id: int):
        self.id = id
        if id == 1:
            self.touching = [(5, 0), (6, 1)]
            self.owned = [(6, 0)]
        else:
            self.touching = [(0, 6), (1, 7)]
            self.owned = [(0, 7)]

    def get_score(self) -> int:
        pass