import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for k,v in kwargs.items():
            for j in range(v):
                self.contents.append(k)

    def draw(self,ball):
        if ball >= len(self.contents):
            balls = self.contents.copy()
            self.contents.clear()
        else:
            balls = random.sample(self.contents, ball)
            for ball in balls:
                self.contents.remove(ball)
        return balls
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success=0
    for i in range(num_experiments):
        hatcp=copy.deepcopy(hat)
        drawn_ball=hatcp.draw(num_balls_drawn)
        exp=True
        for c,n in expected_balls.items():
            if drawn_ball.count(c)<n:
                exp=False
                break
        if exp:
            success+=1
    return(success/num_experiments)

