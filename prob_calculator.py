import copy
import random


class Hat:

    def __init__(self, **contents) -> None:
        #print(contents)
        self.contents = []
        for key, value in contents.items():
            i = 0
            while i < value:
                self.contents.append(key)
                i += 1
        #print(self.contents)

    def draw(self, drawn):
        if drawn > len(self.contents):
            return self.contents
        
        self.ballsDrawn = []
        sample = random.sample(self.contents, drawn)
        #print("sample:", self.ballsDrawn)
        
        #Get sample from contents
        for s in sample:
            self.ballsDrawn.append(s)
            self.contents.remove(s)

        return self.ballsDrawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expectedBallsMatched = 0
    startExperiment = 0

    while startExperiment < num_experiments:
        newHat = copy.deepcopy(hat)
        data = newHat.draw(num_balls_drawn)

        #Make dict from data list
        dataDict = {}
        for d in data:
            dataDict[d] = dataDict.get(d, 0) + 1

        #Matching the balls
        countMatch = 0
        for key, value in expected_balls.items():
            try:
                if dataDict.get(key) >= value:
                    countMatch += 1
            except TypeError:
                break 
        if countMatch == len(expected_balls):
            expectedBallsMatched += 1
            
        startExperiment += 1

    #print(expectedBallsMatched)

    return expectedBallsMatched/num_experiments
    

#random.seed(95)
#hat = Hat(blue=3,red=2,green=6)
#print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))