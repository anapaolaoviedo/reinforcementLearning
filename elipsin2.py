from enum import Enum
import random
import numpy as np
from gridworld.grid import Grid


def reset(initialX, initialY):
    global x, y
    x = initialX
    y = initialY
    return (x, y)

def in_target(newx, newy):
    return newx == targetX and newy == targetY

def in_bound(newx, newy):
    return (newx >= 0 and newx < maxx and
            newy >= 0 and newy < maxy)

def get_reward(newx, newy):
    if not in_bound(newx, newy):
        return -0.1
    if in_target(newx, newy):
        return 1.0
    else:
        return -0.01

def step(action):
    global x, y
    xx, yy = ACTIONS[action]

    next_x = x + xx
    next_y = y + yy

    reward = get_reward(next_x, next_y)
    done = False  # Inicializamos 'done' aquí

    if in_bound(next_x, next_y):
        x, y = next_x, next_y
        if in_target(next_x, next_y):
            done = True
        
    return (x, y), reward, done


initialX = 0
initialY = 2
targetX = 3
targetY = 1
maxx = 4
maxy = 3
x = 0
y = 0

Dir = Enum("Dir", ["UP", "DOWN", "LEFT", "RIGHT"])
actions = [Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT]

grid = Grid(maxx, maxy, 90, 90, title='Gridworld', margin=1, framerate=2)

# Inicialización del diccionario q
q = {}
for i in range(maxx):
    for j in range(maxy):
        q[(i, j)] = {action: 0 for action in actions}

ACTIONS = {
    Dir.UP: (0, -1),
    Dir.DOWN: (0, 1),
    Dir.LEFT: (-1, 0),
    Dir.RIGHT: (1, 0)
}


def tick():
    global x, y
    oldx, oldy = x, y

    current_probs = q[(x, y)]
    value = random.random()

    if value < current_probs[Dir.UP]:
        if y > 0:
            y -= 1
    elif value < current_probs[Dir.UP] + current_probs[Dir.DOWN]:
        if y < maxy - 1:
            y += 1
    elif value < current_probs[Dir.UP] + current_probs[Dir.DOWN] + current_probs[Dir.LEFT]:
        if x > 0:
            x -= 1
    else:
        if x < maxx - 1:
            x += 1

    grid[oldx, oldy] = ''
    grid[x, y] = ':)'
    if (x, y) == (0, 0) or (x, y) == (3, 1):
        reset(initialX, initialY)


grid.set_timer_action(tick)

grid.run()

episodes = 20000
learning_rate_a = 0.9  # alpha/learning rate
discount_factor_g = 0.9  # gamma/discount factor.
epsilon = 1  # 1 = 100% Random walk
epsilon_decay_rate = 0.0001
rewards_per_episode = np.zeros(episodes)

for i in range(episodes):
    state = reset(initialX, initialY)
    terminated = False
    max_q_val = 0

    while not terminated:
        if np.random.uniform(0, 1) <= epsilon:
            action = random.choice(actions)
        else:
            for a in actions:
                q_val = q[state][a]
                if q_val >= max_q_val:
                    action = a
                    max_q_val = q_val

        new_state, reward, terminated = step(action)

        q[state][action] = q[state][action] + learning_rate_a * (
                reward + discount_factor_g * np.max([v for k, v in q[new_state].items()]) - q[state][action]
            )

        state = new_state

    epsilon = max(epsilon - epsilon_decay_rate, 0)

    if epsilon == 0:
        learning_rate_a = 0.0001

    if reward == 1:
        rewards_per_episode[i] = 1

    if i % 1000 == 0:
        print("Episode:", i)
        # Evaluación del sistema después de cada conjunto de 1000 episodios
        total_moves = 0
        eval_episodes = 1000  # Número de episodios para evaluación
        for _ in range(eval_episodes):
            state = reset(initialX, initialY)
            moves = 0
            terminated = False
            while not terminated:
                action = max(q[state], key=q[state].get)  # Seleccionar la acción con el mayor valor Q
                state, _, terminated = step(action)
                moves += 1
            total_moves += moves
        average_moves = total_moves / eval_episodes
        print("Average moves:", average_moves)

print("done")
print(rewards_per_episode)
