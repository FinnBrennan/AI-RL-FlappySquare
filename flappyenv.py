# The Environment Interface
# Implements the standard agent-environment contract.

from game.gamestate import Gamestate
from game import gamelogic as gl


class Flappyenv:

    def __init__(self):
        self.state = Gamestate()

    def get_observation(self):
        nearest_tower = next(
            t
            for t in self.state.towers
            if t[0].x_pos + gl.TOWER_WIDTH > self.state.square.x_pos
        )

        return [
            self.state.square.y_pos,
            self.state.square.vertical_vel,
            nearest_tower[0].x_pos,
            nearest_tower[0].top_height,
            nearest_tower[0].y_pos,
            nearest_tower[0].x_pos - self.state.square.x_pos,
        ]

    def reset(self):
        """
        Return the environment to its initial state and return the
        initial observation. Calling reset() at any time must fully
        re-initialise the game with no residual state from a prior episode.
        """
        self.state = Gamestate()
        self.state.towers.append([gl.Tower_object(), False])
        self.state.frame_count = 1
        observation = self.get_observation()
        return observation

    def step(self, action: int):
        """
        Advance the simulation by exactly ONE frame.
        action: 0 = do nothing, 1 = flap.
        Returns (observation, reward, done):
        observation -- the new state the agent observes (see Part C)
        reward      -- the scalar reward for this transition (see Part D)
        done        -- True if the episode has ended (collision or
                          out-of-bounds), else False.
        """

        done = False

        if self.state.frame_count % gl.TOWER_SPAWN_INTERVAL == 0:
            self.state.towers.append([gl.Tower_object(), False])

        for tower in self.state.towers:
            tower[0].move_tower()

        if self.state.towers[0][0].x_pos <= -gl.TOWER_WIDTH:
            self.state.towers.remove(self.state.towers[0])

        if action == 1:
            self.state.square.apply_jump()
        self.state.square.apply_gravity()

        self.state.score = gl.score_counter(
            self.state.square, self.state.towers, self.state.score
        )

        if (
            any(gl.collides(self.state.square, t[0]) for t in self.state.towers)
            or 0 > self.state.square.y_pos
            or self.state.square.y_pos > gl.SCREEN_HEIGHT
        ):
            done = True

        self.state.frame_count += 1
        observation = self.get_observation()
        reward = 1  # (idk yet temporary)
        return (observation, reward, done)
