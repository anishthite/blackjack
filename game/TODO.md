#TODO
* create function to put the data into csv
* create human wrapper function
* create bot wrapper function
* finish implementing score in close()?
* document all code
* fix the dealerwins and playerwins functions


#GAMEFLOW:

1. create session
2. execute rounds of games
    a. init
        - create the metadata to store in csv
        - draw the opening cards for the dealer and the player
    b. loop:
        init- generate csventry from metadata
        display- give the dealer hand and player hand (list of cards) to the agent
        action- get response
        - if hit: add one more to player hand, check for bust (go to close),  complete csventry with the play results
        - if stand: cover dealer, return outcome
        - close: complete csventry with the play results
