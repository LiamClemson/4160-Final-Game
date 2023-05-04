# PART 1: INTRODUCTION

### NAME
Paleo Fisher

### INSTRUCTIONS
- Download all files in the GitHub repo to local folder.
- Run main.py file.
- Game controls accessbile in-game on main menu.


# PART 2: GAME DESIGN

### MECHANICS / TECHNOLOGY
There is one central while-loop, the Game Loop, that displays the essential gameplay screen. Additionally, the Game Loop calls other functions within the file that run their own loops to display different in-game "screens". For example, the Game Loop will call a Main Menu function, Pause function, Game Pause function, etc. to show the player different displays without affecting the primary Game Loop. This allos gameplay to start and stop without impacting the players performance or score.

### STORY
The story of the game is that you're a fisherman trying to catch as many fish as possible. The gimmick is that you're fishing hundreds of millions of years in the past! The player begins at the start of the Paleozoic Era, beginning with the Cambrian Period, and progresses through the Era, ending with the Permian Period.

The protagonist is the fisherman. They just want to spend a relaxing day on the water and get a couple of fish in the boat. The only problem is something is wrong with spacetime... but that won't stop them from fishing the day away.

The antagonists are the great beasts that roamed the oceans in ancient history. They are big and mean and ready to ruin the fisherman's peaceful day.

### PLAYER EMOTIONS
I want the players to be fascinated and intrigued by the information they learn. It's not everyday that you're learning about the periods of the Paleozoic Era and their relative fauna.
Challenge-wise the game requires multi-tasking. The player must catch as many fish as possible while navigating moving obstacles.
The player will see real-time updates in their score and movements. Additionally, at the end of the game they will see any achievements they've gotten and their final score.

# PART 3: GAME DESIGN CHANGES
The original game concept consisted of the majority of the mechanics implemented in the final product, with a few additional features. 
The plot remained the same during production as well as the fundamental goal and gameplay.
Although, the original vision of the game included the player having had an upgradeable weapon and turn-based combat. Unfortunately, this became too complex to implement in the given timeframe.
I also tried to implement an on-going highscore tracker by reading and writing to a local file but I failed to start working on this feature early enough so it does not properly write to the file.
Any changes to my original vision were primarily based in timing. Yes, the features I had to let go of may have been complex but I know they are possible with enough time and dedication.

# PART 4: GAME DEVELOPMENT AND DOCUMENTATION

### CLASSES
- Fisherman: player class that tracks and updates player data, movements/positioning, and, player image
- Enemy: enemy class that tracks and updates enemy data, movements/positioning, and enemy image
- FishArea: fishing area class that tracks and updates fishing area positioning, and rippling images
- Creature: animal class that stores information relevant to a catchable-animal such as dimensions, classificaiton, and description
- Period: period class that stores information relevant to a time period (description)
- Powerup: powerup class that stores stat bonus information as well as tracking and updating positioning and images, also handles impact on player
- BuoyObstacle: obstacle class that tracks and stores positioning and image data, also handles impact on player

### HELPER METHODS
- compact_text(): converts a long string into a paragraph form by automatically creating newlines at a given string length
- reset_presitge_text(): resets a set of text that reference animals discovered relative to a certain period
- beastiary(): updates counters and a list that store information relative to the number of genus discovered/caught and their totals
- updatePeriod(): handles variable adjustments for game display and stats when transitioning from one period to another

### MAJOR METHODS
- main_menu(): handles displaying the main menu, including an "how to play" screen toggle option
- paused(): handles screen display when player decides to pause the game ("P")
- information_screen(): handles screen display when an animal is caught or the game is transitioning from one period to another
- end_game(): handles screen display at the completion of the game and allows the player the option to start again
- count_down(): handles the screen display when counting down from 3 to begin each period

### MAJOR BUGS
- There may be an issue with the barrel power-up sound effect playing in bursts rather than a single time
- If a fish is caught exactly as a period changes, after clicking through the new period screen the player may be immediately prompted with a caught fish screen
- The highscores display at the completion of the game may not properly update
- There may be issues inputting your initials at the completion of the game to go with your score
- Some sprites (specifically the buoy) may blit on screen for a split moment when reverting back to the main menu screen after completing at least one run-through
- Not technically a bug, but the oar power-up has no sound effect

### COLLABORATION
I worked alone. My environment was VSCode.

# PART 5: GROUP MEMBER ROLES, TASKS, AND PERFORMANCE

I worked alone.

### TIMELINE

