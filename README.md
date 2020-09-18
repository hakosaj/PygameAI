# Intelligent agents for basic games


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

The `algorithm` options are
  - empty for normal flappy bird
  - `GA` for genetic algorithm
  - `Q` for Q-learning

To load a Q-learning Q-matrix training snapshot, use the "loadfile"-argument to specify the snapshot.

Simpler way is to use the specified files separately:
- `gaflappy.py` for GA
- `manual.py` for normal
- `qflappy.py` for Q learning


### Tetris

The Tetris operates with a 4-parameter vector that govern the agent's behaviour. The program itself can be ran in several different ways. There are two modes for this, visual or nonvisual mode. The nonvisual mode is used for parallerising the genetic algorithm when finding parameters.

Whenever the heuristic agent is playing the game, constant `multi` from `constants.py` dictates whether or not the actual heuristic parallerises the finding of a following move. The default version is doing it.

For Tetris, the command is either

`python tetris.py [control]`

The `[control]` options are
  - `manual` for a normal Tetris game
  - `auto` for playing the game with the heuristic agent with predetermined parameters


To run the parameter-finding GA, use

`python GA.py`

To utilise a faster, nonvisual parallel implementation of the parameter finding algorithm, change

`visual` from `constants.py` to `False`,

and use the command

`python MCGA.py`



The aforementioned uses 

- Population size: 80
- Generations: 5
- Blocks per individual: 500

!!WARNING!!

This takes a LOT of time, there's still work to be done regarding the performance.

!!WARNING!!


My Tetris algorithm is modelled after [Yiyuan Lee](https://codemyroad.wordpress.com/2013/04/14/tetris-ai-the-near-perfect-player/)






## Status and steps: currently at phase 1

### Flappy
  - Implement the Deep-Q CNN http://cs231n.stanford.edu/reports/2016/pdfs/111_Report.
  - File selection based on argument
  
  **After phase 1:**
  - Update Q-learning reward scheme so it converges better
  - Some sorta ANN (perceptron with 4 inputs and 2 outputs?)
 
### Breakout
  - Fix the issues with ball+block collisions
  - Implement Deep-Q CNN á lá DeepMind

### Snake
  - Implement baseline game
  - Hamiltonian circuit-AI

  **After phase 1:**
  - Deep Neural Net-AI
  
### Tetris
  - Fix bugs: full screen freeze
  - Optimize singlecore perf: some done, keep track of actives to avoid lambda call every time?
  - Folder structure


  **After phase 1:**
  - This one does not do cliffhangers
  - No direct interfacing, get all data from the screen as a player would?
  - Parameter convergence plots


## Authors

* **Jussi Hakosalo [hakosaj](https://github.com/hakosaj)** - *All of it* 



## License

This project is licensed under the MIT License 
