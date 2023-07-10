import random
from typing import List


class Environment:
    # 某些世界的模型，它在智能体外部，
    # 负责提供观察并给予奖励。
    # 而且环境会根据智能体的动作改变自己的状态
    def __init__(self):
        self.steps_left = 10  # 限定交互步数,状态就是一个计数器，记录智能体还能和环境交互的步数。

    def get_observation(self) -> List[float]:  # Python的类型注解
        # 能给智能体返回当前环境的观察。它通常被实现为有关环境内部状态的某些函数
        return [0.0, 0.0, 0.0]

    def get_actions(self) -> List[int]:
        # 允许智能体查询自己能执行的动作集
        return [0, 1]

    def is_done(self) -> bool:
        # 给予智能体片段结束的信号
        return self.steps_left == 0

    def action(self, action: int) -> float:
        # 核心； 处理智能体的动作以及返回该动作的奖励
        # 环境提供了一种检测片段何时结束的方法，通知智能体它无法再继续交互了
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()  # 不管智能体执行任何动作，它都给智能体返回随机奖励


class Agent:
    # 包含构造函数以及在环境中执行一步的方法
    def __init__(self):
        # 初始化计数器，该计数器用来保存片段中智能体累积的总奖励
        self.total_reward = 0.0

    def step(self, env: Environment):
        # 接受环境实例作为参数，并允许智能体执行下列操作：观察环境。基于观察决定动作。向环境提交动作。获取当前步骤的奖励
        current_obs = env.get_observation()
        actions = env.get_actions()
        reward = env.action(random.choice(actions))
        self.total_reward += reward


if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print("Total reward got: %.4f" % agent.total_reward)
