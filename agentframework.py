import random

class Agent:
    
    def __init__(self, environment, agents, y, x):
        self.environment = environment
        self.agents = agents        
        self.store = 0

        if (x == None):
            self._x = self.get_x()
        else:
            self._x = x
        
        if (y == None):
            self._y = self.get_y()
        else:
            self._y = x

    def __set_x(self):
        return random.randint(0,99)

    def __set_y(self):
        return random.randint(0,99)
    
    def get_x(self):
        return self.__set_x()

    def get_y(self):
        return self.__set_y()

    # calculate distance between two agents
    def distance_between(self,agent):
        return (((self._x - agent._x)**2) +
        ((self._y - agent._y)**2))**0.5

    def move(self):
        
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
    def share_with_neighbours(self,neighbourhood):
        for agent in self.agents:
           dist = self.distance_between(agent)
           if dist <= neighbourhood:
            #    print("self store " + str(self.store))
            #    print("agent store " + str(agent.store))
               sum = self.store + agent.store
               ave = sum/2
               self.store = ave
               agent.store = ave
            #   check whether the function is working
               print("sharing " + str(dist) + " " + str(ave))
            
        
    
