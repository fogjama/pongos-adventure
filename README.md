# Pongo's Adventure

Practice platformer game using Pygame.

## Details

Pongo is going on an adventure! He will explore different environments, encountering friends and foes alike. Along the way he will collect items that will let him use different abilities such as throwing fireballs, jumping extra high, and even eating his enemies.

## Technical Goals

In no particular order:
- [ ] Creating classes
- [ ] Inheriting from class
- [ ] Writing functions
- [ ] Refactoring code
- [ ] Creating decorators
- [ ] Using loops effectively

### Stages

#### Stage 1

- Simple forward-scrolling platformer with max 3 levels of platforms
- Limited enemies
    - Enemies have limited movement
    - Enemies of type *ground* (moves along the ground)
- Pongo can get rid of an enemy by jumping on it once
- Running into the side or bottom of an enemy reduces Pongo's health by 1
- When Pongo loses all of his health, he restarts the level

Optional Extras:
- Picking up a piece of food increases Pongo's health by 1
- Enemies of type *flying* (moves back and forth in the air)


### Future Development

- Enemies
    - *floating* (moves along both x and y planes in the air)
    - *jumping* (bounces along the ground)
    - *heavy* (moves along the ground, slower speed and higher attack)
    - *light* (moves along the ground, faster speed and lower attack)
- Item collection: 
    - Weapon - allows Pongo to attack left/right
    - Ranged Weapon - allows Pongo to attack from a distance
    - Power Up - item to double Pongo's attack power
    - Shrink - item to shrink Pongo to half size, evading attack but halves jump height
    - Grow - item to double Pongo's size, doubling jump height
- Score
    - Points given for enemy kills and item collection
    - Special items that just increase score
    - Points deducted for hits and deaths
- Lives
    - Limited number of lives
    - Health reduced to 0 removes a life
    - All lives removed = Game Over
- Story 
    - Story interludes between stages
    - Choices in dialogue affect stage generation
- Environment
    - Doorways
    - Portals


## Technical Structure

World design is based on 64x64 tiles

### Files


### Assets


## Installing and Running




