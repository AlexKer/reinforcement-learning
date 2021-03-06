import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset() # initial observation
    for t in range(100):
      env.render()
      print(observation)
      action = env.action_space.sample()
      # step returns observation, reward, done (episode), info
      observation, reward, done, info = env.step(action)
      if done:
        print("Episode finished after {} timesteps.".format(t+1))
        break
env.close()
