import numpy as np
import Gridworld_v1
np.set_printoptions(threshold=np.inf)

print("hello world")

gamma = 0.9   #折扣因子，越接近0越近视
rows = 5      #记得行数和列数这里要同步改
columns = 5
# gridworld = GridWorld_v1.GridWorld_v1(rows=rows, columns=columns, forbiddenAreaNums=4, targetNums=2, seed = random.randint(1,1000))
# gridworld = GridWorld_v1.GridWorld_v1(desc = [".#",".T"])             #赵老师4-1的例子
# gridworld = GridWorld_v1.GridWorld_v1(desc = ["##.T","...#","...."])  #随便弄的例子
gridworld = Gridworld_v1.GridWorld_v1(forbiddenAreaScore=-10, score=1,desc = [".....",".##..","..#..",".#T#.",".#..."])
gridworld.show()

value = np.zeros(rows*columns)       #初始化可以任意，也可以全0
qtable = np.zeros((rows*columns,5))  #初始化，这里主要是初始化维数，里面的内容会被覆盖所以无所谓
policy = np.argmax(qtable,axis=1)    #初始策略
gridworld.showPolicy(policy)
