class Individual:


    def __init__(self, behavior):
        self.behavior = behavior
        self.foodState = False
    

    def __repr__(self):
        return f'Individual with {self.behavior} behavior'


    def hasFood(self) -> bool:
        return self.foodState


    def setFoodState(self, state: bool):
        self.foodState = state