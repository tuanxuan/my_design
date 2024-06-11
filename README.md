![image](https://github.com/tuanxuan/my_design/assets/145859078/109e54cb-48d0-40db-9dfd-63fc7d966435)



SPACE WAR

Overview
Space War is a 2D arcade-style game where players control a spaceship to battle against waves of enemy spaceships. The objective is to destroy all enemy ships while avoiding their bullets and surviving as long as possible. The game features a main menu, scrolling background, and explosion animations upon collisions.

Features

- Scrolling Background: A dynamic, continuously scrolling space background.

- Player Control: Move the spaceship with arrow keys and shoot bullets with the space bar.

- Enemies: Multiple waves of enemy spaceships that move and shoot bullets.


- Explosions: Animated explosions when spaceships are hit.

- Sound Effects: Various sound effects for background music, shooting, and explosions.

- Score System: Score increases when enemy spaceships are destroyed.

- Health Bar: Displays the remaining health of the player's spaceship.

Installation

1. Clone the repository:

git clone https://github.com/tuanxuan/my_design.git

2.Install dependencies:

Ensure you have pygame installed. If not, you can install it via pip:
    pip install pygame

3. Run the game

python main.py

How to Play

1.Start the Game:

- Launch the game and press Enter to start.

- Press Q to quit the game.

2.Controls:

- Move: Use the arrow keys (Left, Right, Up, Down) to move the spaceship.
- Shoot: Press the Space bar to shoot bullets.

3.Objective:

- Destroy all enemy spaceships.
- Avoid getting hit by enemy bullets.
- Survive as long as possible and achieve the highest score.

4.Game Over:

The game ends when the player's spaceship health drops to zero or all enemy spaceships are destroyed.

- If you lose, a "YOU LOSE!" message will appear.

- If you win, a "YOU WIN!" message will appear.

CODE OVERVIEW

Main Components

1.Constants: Definitions for window dimensions, colors, and asset directories.

2.Initialization: Setup for pygame, screen, clock, and game variables.

3.Functions:

- draw_bg(): Draws the scrolling background.
  
- draw_text(surf, text, size, x, y): Draws text on the screen.
  
- draw_score(surf, text, size, x, y): Draws the score on the screen.
  
- main_menu(): Displays the main menu and handles user input.
  
4.Classes:

- Father_Spaceship: Parent class for spaceships.

- My_spaceship: Player's spaceship with health and shooting capabilities.

- Spaceship_enemys: Enemy spaceships.

- Father_Bullets: Parent class for bullets.

- Bullets: Player's bullets.
  
- Enemy_Bullets: Enemy bullets. 

- Explosion: Explosion animation for collisions.
  
5. Main Loop: Handles game logic, including movement, shooting, collisions, and drawing.
   
ASSET LOADING

- Images: Background, player spaceship, enemy spaceships, bullets, and explosion frames.
- Sounds: Background music, shooting sound, and explosion sound effects.

Assets

Place your assets in the following directories:

* Images: assets/
- background.png
- main.png
- myspaceship1.png
- enemy1.png, enemy2.png, enemy3.png, enemy4.png, enemy5.png
- bullet.png
- enemy_bullet.png
- explosion1.png, explosion2.png, explosion3.png, explosion4.png, explosion5.png

* Sounds: sounds/

- menu.ogg
- getready.ogg
- laser.ogg
- explosion.ogg
- explosion2.ogg

  FUTURE IMPROVEMENTS
- Add power-ups and upgrades for the player's spaceship.
- Implement different levels with increasing difficulty.
- Add more enemy types with unique behaviors.
- Implement a high score system to save and display the highest scores.


