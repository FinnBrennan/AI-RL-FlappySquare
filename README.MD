# FlappySquare AI RL 

The goal for this project is to create a simple user friendly game. (I chose to build a game very similar to the classic Flappy Bird game). Then to refactor it into a agent friendly environment before teaching an agent how to play the game. 

## Phase 1: User Friendly Game

Flappy Square: A simple flappy-bird style python game. Built using the pygame library.

- Player sprite with physics (gravity + jump -> updates sprite's y-velocity)
- Frame-rate controlled spawning of tower obstacles. (Spawns both top and bottom with random gap placements). Towers move across the screen from right to left before being removed and respawned. 
- Live score and persistent high score tracking within sessions. 
- Game over (+screen) and reset for users. 

At this point (current) the game is a user friendly / human-playable simple game.

**Controls:** `Space` / `↑` to flap · `S` to reset.

## Phase 2: Refactor as an agentic environment.

This second phase involves refactoring the player-focused game to a environment which an agent can be trained to play within.





## Learnings: 

### Phase 1

I wanted to challenge my ability to pick up an unfamiliar library (pygame) and work through applying the library to a project by working out the design and debugging problems myself from its documentation, rather than following a tutorial. Using my existing python knowledge alongside the docs, I worked out the game loop, collision handling and state management; resulting in a complete, user-friendly flappy-bird style game. I definitely struggled at some points, but it was a great problem solving excercise to have to figure out how various pygame functions worked through trial and error, reading the documentation, and experimentation.  

I chose flappy bird as inspiration due to its relative simplicity: 1 player sprite,  recycled scrolling obstacles, and the simplicity of only 1 input. This also means it is a very good candidate for my first try at reinforcement learning in phases 2+. 
