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

![Overview of the simulation](https://github.com/hakosaj/PygameAI/blob/master/flappy/gena.JPG) Flappy bird and genetic algorithms
## Getting Started

Clone this and install requirements from requirements.txt.

Then navigate to folder and voilá!



## Using the software

### Flappy

For Flappy bird, the command is

`python main.py [algorithm] [loadfile]`

The [algorithm] options are
  - empty for normal flappy bird
  - `GA` for genetic algorithm
  - `Q` for Q-learning

To load a Q-learning Q-matrix training snapshot, use the "loadfile"-argument to specify the snapshot.

Simpler way is to use the specified files separately:
- `gaflappy.py` for GA
- `manual.py` for normal
- `qflappy.py` for Q learning


### Tetris

For Tetris, the command is either

`python tetris.py [control]`

The [control] options are
  - `manual` for a normal Tetris game
  - `auto` for playing the game with the heuristic agent with predetermined parameters


To run the parameter-finding GA, use

`python GA.py`

The aforementioned uses 

- Population size: 80
- Generations: 5
- Blocks per individual: 500

!!WARNING!!

This takes a LOT of time, there's still work to be done regarding the performance.

!!WARNING!!





## Status and steps until phase 1 is completed

### Flappy
  - Implement the Deep-Q CNN http://cs231n.stanford.edu/reports/2016/pdfs/111_Report.
  - Update Q-learning reward scheme etc. so that it actually converges
  - File selection based on argument
 
### Breakout
  - Fix the issues with ball+block collisions
  - Implement Deep-Q CNN á lá DeepMind

### Snake
  - Implement baseline game
  - Hamiltonian circuit-AI

  **After phase 1:**
  - Deep Neural Net-AI
  
### Tetris
  - Separate automated GA and manual game
  - Fix bugs: full screen freeze
  - Optimize performance, singlecore and multicore
  - Parameter convergence plots

  **After phase 1:**
  - Multiprocessing to make the GA faster?
  - This one does not do cliffhangers
  - No direct interfacing, get all data from the screen as a player would?


## Authors

* **Jussi Hakosalo** - *All of it* - [hakosaj](https://github.com/hakosaj)

## License

This project is licensed under the MIT License 
