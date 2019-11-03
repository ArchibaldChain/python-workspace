# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(
        os.getcwd(), 'python-workspace\\Workspace for Python\Reinforcement-learning'))
    print(os.getcwd())
except:
    pass

# %%
import numpy as np
import gym
import random
import time
import IPython.display as clear_output


# %%
env = gym.make("FrozenLake-v0")

# %%
action_space_size = env.action_space.n
state_space_size = env.observation_space.n

q_table = np.zeros((state_space_size, action_space_size))
print(q_table)


# %%
num_episodes = 1000
max_steps_per_episode = 100

learning_rate = 0.01            # Alpha
discount_rate = 0.99

exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.01

# %% [markdown]
# ###  Implement Reinforcement learning

# %%
rewards_all_episodes = []

# Q-learning
for episode in range(num_episodes):
    state = env.reset()

    done = False
    rewards_current_episode = 0  # The start rewards
    for step in range(max_steps_per_episode):

        # Exploration-exploitation trade-off
        exploration_rate_threshold = random.uniform(0, 1)
        if exploration_rate_threshold > exploration_rate:
            action = np.argmax(q_table[state, :])
        else:
            action = env.action_space.sample()

        new_state, reward, done, info = env.step(action)

        # UPdate Q-table for Q(s,a)
        q_table[state, action] = q_table[state, action] * (1-learning_rate) + learning_rate*(
            reward + discount_rate * np.max(q_table[new_state, :]))

        state = new_state
        rewards_current_episode += reward

        if done == True:
            break

        # Exploration rate decay
        exploration_rate = min_exploration_rate + \
            (max_exploration_rate - min_exploration_rate) * \
            np.exp(-exploration_decay_rate * episode)

        rewards_all_episodes.append(rewards_current_episode)

# Calculate and print the a erage reward per thousand episodes
rewards_per_thousand_episodes = np.split(
    np.array(rewards_all_episodes), num_episodes/1000)
count = 1000

print("*********Average reward per thousand episodes *******\n")
for r in rewards_per_thousand_episodes:
    print(count, ":", str(sum(r/1000)))
    count += 1000

print("\n\n**********************Q-table*******************\n")
print(q_table)


# %%
