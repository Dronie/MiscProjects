import numpy as np

class MontyHall():

    def __init__(self):
        self.results = []
        self.doors = []
        self.winning_door = None
        self.choice = None


    def init_doors(self, n):
        self.doors = np.zeros(n)
        self.winning_door = np.random.randint(0,n)
        self.doors[self.winning_door] = 1
        print("Doors:", self.doors)

    def open_doors(self, choice):
        for i in range(0, len(self.doors)):
            if i != self.choice and i != self.winning_door:
                self.doors[i] = 2
            
        print("Open Doors:", self.doors)

    def stick_or_stay(self, s, doors):
        if s == 1 and self.doors[self.choice] != 1:
            print("Lose!")
            self.results.append(0)
        elif s == 1 and self.doors[self.choice] == 1:
            print("Win!")
            self.results.append(1)
        elif s != 1 and self.doors[self.choice] != 1:
            print("Lose!")
            self.results.append(0)
        elif s != 1 and self.doors[self.choice] == 1:
            print("Win!")
            self.results.append(1)
    
    def reset(self):
        self.doors = []
        self.winning_door = None
        self.choice = None 

    def play(self, n, games):
        for i in range(0, games):
            self.init_doors(n)
            self.choice = np.random.randint(0,n)
            print("Choice is:", self.choice+1)
            self.open_doors(self.choice)
            self.stick_or_stay(0, self.doors)
            self.reset()
        print(self.results)
        tally = 0
        for i in self.results:
            if i == 1:
                tally += 1
        print(100 * (tally / len(self.results)), "% win rate")

if __name__ == "__main__":
    game = MontyHall()
    game.play(3, 10)
