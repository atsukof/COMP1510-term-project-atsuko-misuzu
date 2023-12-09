[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ECKgeadS)
# COMP-1510-202330-Term Project Make Me A Game

## 0. Student Information
### Name:

Atsuko Uemura

Misuzu Taniguchi

### Student number:

A01373940

A01367008

### GitHub username:

atsukof

Miryeong1235


## 1. Introduction
About a decade ago, we were students at Kyoto University, immersed in the stunning beauty of Kyoto.
Our love for this city runs deep, and we would like players to experience its charm and visit its streets.
So, we made a game to show how great Kyoto is and teach about Kyoto and Japan using a map of this amazing city.

## 2. How the game progresses
### 2-1. Rules

- To win the game, the ultimate goal is to reach Kinkakuji (Golden Pavilion) and defeat the monk in a match.
- To engage in a battle with the monk, a character must reach level 3.
- Reaching level 3 requires accumulating Kyoto Experience Points (KEP) of 6.
- If a character's HP drops below 0, it's game over.

### 2-2. Characters

- Characters possess a name, current location, HP, Kyoto Experience Points (KEP), and Level.
- HP starts at 5, and KEP starts at 0.

### 2-3. Map

- Characters move across a 10 x 10 map.
- Initially, characters are at Kyoto Station.
- Players choose a direction (north, south, east, west) for their character to move.

### 2-4. Special Location

- Certain points on the map are designated as Special Locations.
- At these locations, characters can enjoy delicious local food.
- Consuming food raises HP by 1.

### 2-5. Quizzes

- Upon each character movement, there is a chance for a quiz related to Japan or Kyoto to be presented.
- Correct answers to quizzes increase KEP by 1.
- Incorrect answers result in a decrease of HP by 1.

### 2-6. Battle with the monk

- Once the character reaches level 3 and arrives at Kinkakuji (Golden Pavilion), the monk challenges them to a match.
- Winning the battle against the monk leads to game completion.
- Losing the battle against the monk results in a decrease of 2 HP.
- Characters can move to a different location and challenge the monk again at Kinkakuji, allowing multiple attempts.


## 3. Requirements

| Element                          | Functions/Description                                                                    |
|----------------------------------|------------------------------------------------------------------------------------------|
| Scenario                         | `instruction` - Describes game progression.                                              |
| 10x10 grid environment           | `make_board`, `show_status_and_map`                                                      |
| Character                        | `make_character`                                                                         |
| Character attributes             | Name, Hit Points, Kyoto Experience Points, Level                                         |
| Character movement               | `get_user_choice`, `validate_direction`, `move_user`                                     |
| Encounter obstacles              | `check_quiz`                                                                             |
| Overcome obstacles               | `play_quiz`                                                                              |
| Game completion                  | Character achieves final goal or level 3                                                 |
| Simple leveling scheme           | Starts at level 1, can reach level 3                                                     |
| Leveling elements                | Level name, Level up, Reaching new levels, Reaching level 3                              |
| Character level-up action        | Fight with the final boss if Level 3 is achieved and at Kinkakuji                        |
| Character runs out of mojo       | Game ends if character is not alive                                                      |
| Immutable data structures        | `make_board`                                                                             |
| Mutable data structures          | `make_character`                                                                         |
| Exceptions and handling          | `fight_with_monk`                                                                        |
| List/dictionary comprehensions   | `make_board` (board_dict)                                                                |
| If-statements                    | Various functions throughout the game                                                    |
| Loops (for/while)                | Various functions throughout the game                                                    |
| Membership operator              | `fight_with_monk`, `make_board`                                                          |
| Range function                   | `make_board`, `show_status_and_map`                                                      |
| Itertools                        | `fight_with_monk`                                                                        |
| Random module                    | `play_quiz`, `fight_with_monk`                                                           |
| Formatting strings               | `make_character`, `fight_with_monk`, `get_user_choice`, `check_level`, `is_food_station` |

