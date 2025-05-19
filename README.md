Game development of a 2 player game using only python and pygame🐍

Tools used:
Vscode
github copilot

Pygame game devlog1️⃣: the initaial commit had a basic setup for a platformer type of game, the players could move in the ground floor but limited to the right or left direction, the code included the game loop within a class and instances were created after

What i learned from this log✅: 1)basic fundamentals of pygame and player movenment, 
                                2)utilization of classes and basic oop concepts

pygame game devlog2️⃣: I refectored the game dimentions to be smaller(100, 100) >> (50,50), and i removed the ground object and gave the players more movement, this enables the players to move in all 4 axis

What i learned from this log✅: 1) better understanding of pygame's costomization feutures

pygame game devlog3️⃣: added player bounderies for the players and deleted the extra pygame file

What i learned from this log✅:1) better understanding of pygame's coordinate system, and better project file management

pygame game devlog4️⃣: added projectiles for both players, this was done by creating a projectile class that has 3 methods, creating an instance of the projectile class on both the players, and creating an update for the projectile making it move and removing the projectile when it reach the boundry, and drawing it on the display

What i learned from this log✅: 1) How to utilize class functions from other classes, how to create moving game objects using delta time and the velocity, and better code structure and readability

pygame game devlog5️⃣: enhanced the shooting by making the axis of shooting to go all axis, depending on the players last direction

What i learned from this log✅: 1) how to better code structure, the code i initially wrote took the player movement detection in later stages of the code which gave me problems and errors, the solution was to take the players movement using the keys pressed and update the direction of the projectile with the players movement instead of trying to find player movenment in the game loop and changing the direction there.

