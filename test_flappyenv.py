import random
from flappyenv import Flappyenv

env = Flappyenv(True)
for episode in range(5):
    obs = env.reset()
    done = False
    step = 0
    while not done:
        # action = random.choice([0, 1])
        action = 0
        obs, reward, done = env.step(action)
        step += 1
        print(f"step: {step}")
    print(f"Episode {episode}: score = {env.state.score}")
