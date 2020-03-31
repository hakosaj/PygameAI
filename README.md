# Intelligent agents for basic games
HOX! WORK IN PROGRESS, SERIOUSLY


Just a fun run, creating some basic (retro) games and intelligent agents to play them. Will be creating all of the AI-side from scratch.

Pygame is used in creating the game environment. Tensorflow, PyTorch and SKLearn not allowed!

Going to do these games... (tentative):
  - Flappy bird
  - Minesweeper
  - Breakout
  - Snake
  - Tetris

...using these kinds of agents (tentative):
  - Genetic algorithm
  - ANN with backpropagation
  - Q-learning
  - NEAT
  - CNN with only using the screen as input

![Overview of the simulation](https://github.com/hakosaj/PygameAI/blob/master/gena.JPG) Flappy bird and genetic algorithms
## Getting Started

Clone this and install requirements from requirements.txt.

Then navigate to folder and voilá!



## Using the software

For Flappy bird, the command is

`python main.py [algorithm] [loadfile]`

The algorithm options are
  - empty for normal flappy bird
  - "GA" for genetic algorithm
  - "Q" for Q-learning

To load a Q-learning Q-matrix training snapshot, use the "loadfile"-argument to specify the snapshot.




## Next steps
  - Implement the basic structure of a Q-learning agent for FlappyBird
  - Design and implement a base version of Breakout

## Authors

* **Jussi Hakosalo** - *All of it* - [hakosaj](https://github.com/hakosaj)

## License

This project is licensed under the MIT License 
