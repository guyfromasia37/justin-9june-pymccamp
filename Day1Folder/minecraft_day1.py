# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


def teleport():
    agent.teleport_to_player()
player.on_chat("tp", teleport)

def turnleft():
    agent.turn(LEFT)
player.on_chat("tl", turnleft)

def turnright():
    agent.turn(RIGHT)
    
player.on_chat("tr", turnright)




################## On Chat Commands Section #####################
