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
import IPython.display as display


# %% [markdown]
# ### Creating the environment
# We will using the environment *FrozenLake-v0*

# %%
env = gym.make("FrozenLake-v0")

# %% [markdown]
# ### Creating the Q-table
# We are going to construct our Q-table, and initialize all the Q-values.
# number of rows in the table = size of state space in the environemnt
#
# number of columns is equivalent size of action space

# %%
action_space_size = env.action_space.n
state_space_size = env.observation_space.n

q_table = np.zeros((state_space_size, action_space_size))
print(q_table)

# %% [markdown]
# ### Initializing Q-learning parameters
# Now we initalize all the paramenters.
# `num_episodes` defines the total number of episodes.
# `learning_rate` is represented with the symbol $\alpha$.
# `discount_rate` is represented with the symbol $\gama$.
# `exploration_rate` is represented with the symbol $\epsilon$.

# %%
num_episodes = 10000
# we define a maximum number of steps that our agent is allowed to take within a single episode
max_steps_per_episode = 100

# Alpha the weighted for sum of old value and learned value in Q
learning_rate = 0.01
discount_rate = 0.99

exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.001

# %% [markdown]
# ###  Implement Reinforcement learning

# %%
rewards_all_episodes = []

# Q-learning
for episode in range(num_episodes):
    state = env.reset()
    print("episodes:", episode)

    done = False
    rewards_current_episode = 0  # The start rewards
    for step in range(max_steps_per_episode):

        # Exploration-exploitation trade-off
        exploration_rate_threshold = random.uniform(0, 1)
        # this will determine whether our agent will explore or expoit
        if exploration_rate_threshold > exploration_rate:
            action = np.argmax(q_table[state, :])
        else:
            action = env.action_space.sample()

        new_state, reward, done, info = env.step(action)

        # UPdate Q-table for Q(s,a)
        q_table[state, action] = q_table[state, action] * (1-learning_rate) + learning_rate*(
            reward + discount_rate * np.max(q_table[new_state, :]))

        # Transition to the next state
        state = new_state
        rewards_current_episode += reward

        if done == True:
            break

    # Exploration rate decay
    exploration_rate = min_exploration_rate + \
        (max_exploration_rate - min_exploration_rate) * \
        np.exp(-exploration_decay_rate * episode)

    rewards_all_episodes.append(rewards_current_episode)

# %%
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

# %% [markdown]
# ### Watch the agent play the game

# %%
for episode in range(3):
    # initialize new episode params
    state = env.reset()
    done = False
    print("*******EPISODE ", episode + 1, "**********\n\n\n\n\n")
    time.sleep(1)
    for step in range(max_steps_per_episode):
        display.clear_output(wait=True)
        env.render()  # render the current state of the environment to display
        time.sleep(0.3)
        # Show the current state of environment on screen
        # Choose action with highest Q-value for current state
        # Take new action
        action = np.argmax(q_table[state, :])
        new_state, reward, done, info = env.step(action)

        state = new_state

        if done:
            display.clear_output(wait=True)
            env.render()
            if reward == 1:
                # Agent reached the goak and won episode
                print("**** You reached the goal****")
                time.sleep(3)
                display.clear_output(wait=True)
            else:
                # Agent stepped in a hole and lost episode
                print("***** You fell into a hole****")
                time.sleep(3)
                display.clear_output(wait=True)
            break
env.close
