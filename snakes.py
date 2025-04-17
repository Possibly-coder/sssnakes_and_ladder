import random
PLAYERS = 3

current_position_of_players = {1:0, 2:0, 3:0}
class Player:
    def __init__(self, name, length):
        self.name = f"player_{name}"
        self.pos = 0
        self.grid_length = length
        self.pos_history = []
        self.dice_history = []
        self.grid_size = length*length
        self.winner = "Nope"
        self.two_dimension_coordinates = []


    def move(self, dice_val):
        new_position = int(self.pos)+dice_val
        if new_position > self.grid_size:
            self.pos_history.append(self.pos)
            co_ordinates = get_coordinates(self.pos, self.grid_length)
            self.two_dimension_coordinates.append(co_ordinates)
            return self.pos
        self.pos = new_position
        co_ordinates = get_coordinates(self.pos, self.grid_length)
        self.two_dimension_coordinates.append(co_ordinates)
        self.pos_history.append(new_position)
        return new_position

    def pos_reset(self):
        self.pos = 0

def get_coordinates(pos, grid_length):
    if pos == 1:
        return (0,0)
    row = (pos-1)%grid_length
    col = (pos-1)//grid_length
    if col%2 == 1:
        row = grid_length-row-1
    return (row, col)
def check_for_collision_and_return_the_previous_player(player: Player, pos):
    for player, curr_pos in current_position_of_players.items():
        if pos == curr_pos:
            return True, player
    return False, 0

def game_loop():
    grid_length = int(input("Whats the grid size?"))
    grid_size = grid_length*grid_length

    players = {Player(i, grid_length) for i in range(PLAYERS)}
    winner = False
    while not winner:
        for player in players:
            input(f"{player.name} press enter to roll the dice")
            dice_val = random.randint(1,6)
            print(f"The Dice has returned : {dice_val}")
            player.dice_history.append(dice_val)
            # if player.pos + dice_val > player.grid_size:
            #     continue
            new_position = player.move(dice_val)
            print(f"{player.name}'s new position is {new_position} \n \n")
            if new_position == grid_size:
                winner = True
                co_ordinates = get_coordinates(grid_size, grid_length)
                player.winner ="WINNER"
                print(f"Player {player.name} is the winner \n \n \n \n ")
                break

            #we check the collision below
            for check_player in players:
                if check_player.pos == new_position and check_player != player:
                    check_player.pos_reset()


    for player in players:
        print(f"Dice History of {player.name}: ", player.dice_history)
        print(f"Position History of {player.name}: ", player.pos_history)
        print(f"the co-ordinate history for {player.name} is :", player.two_dimension_coordinates)
        print(f"is {player.name} a winner ??", player.winner, "\n\n")



if __name__ == "__main__":
    print("Lets start the game")
    game_loop()