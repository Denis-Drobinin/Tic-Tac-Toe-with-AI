import random


def menu():
    while True:
        print("Input command:")
        command = input()
        command_list = command.split()
        global players
        global player_x
        global player_o
        if command == "exit":
            break
        elif len(command_list) != 3:
            print("Bad parameters!")
        elif competitors.count(command_list[1]) > 0 and competitors.count(command_list[2]) > 0:
            players = {"player_X": {"Level": command_list[1], "Mark": "X", "Id": 1},
                       "player_O": {"Level": command_list[2], "Mark": "O", "Id": 1}}
            player_x = command_list[1]
            player_o = command_list[2]
            print(f"""---------
| {field[0]} {field[1]} {field[2]} |
| {field[3]} {field[4]} {field[5]} |
| {field[6]} {field[7]} {field[8]} |
---------""")
            return player_x, player_o, players
        else:
            print("Bad parameters!")
        return menu()


def human(mark, opponent_mark, id):
    global field_list
    move_x = 0
    move_y = 0
    while True:
        print("Enter the coordinates:")
        coordinates = str(input())
        if not coordinates.replace(" ", "1").isdigit():
            print("You should enter numbers!")
        elif any(int(x) > 3 or int(x) < 1 for x in coordinates.split()):
            print("Coordinates should be from 1 to 3!")
        else:
            break
    if coordinates[0] == "1":
        move_x = 0
    elif coordinates[0] == "2":
        move_x = 1
    elif coordinates[0] == "3":
        move_x = 2
    if coordinates[2] == "1":
        move_y = 0
    elif coordinates[2] == "2":
        move_y = -3
    elif coordinates[2] == "3":
        move_y = -6
    while True:
        if field_list[6 + move_x + move_y] != "_":
            print("This cell is occupied! Choose another one!")
            return human(mark, opponent_mark, id)
        else:
            field_list[6 + move_x + move_y] = mark
            break
    result = "".join(field_list).replace("_", " ")
    print(f"""---------
| {result[0]} {result[1]} {result[2]} |
| {result[3]} {result[4]} {result[5]} |
| {result[6]} {result[7]} {result[8]} |
---------""")
    return field_list


def ai_easy(mark, opponent_mark, id):
    global field_list
    move_x = 0
    move_y = 0
    coordinates = f'{random.choice(["1", "2", "3"])} {random.choice(["1", "2", "3"])}'
    if coordinates[0] == "1":
        move_x = 0
    elif coordinates[0] == "2":
        move_x = 1
    elif coordinates[0] == "3":
        move_x = 2
    if coordinates[2] == "1":
        move_y = 0
    elif coordinates[2] == "2":
        move_y = -3
    elif coordinates[2] == "3":
        move_y = -6
    while True:
        if field_list[6 + move_x + move_y] != "_":
            return ai_easy(mark, opponent_mark, id)
        else:
            field_list[6 + move_x + move_y] = mark
            break
    result = "".join(field_list).replace("_", " ")
    print('Making move level "easy"')
    print(f"""---------
| {result[0]} {result[1]} {result[2]} |
| {result[3]} {result[4]} {result[5]} |
| {result[6]} {result[7]} {result[8]} |
---------""")
    return field_list


def ai_medium(mark, opponent_mark, id):
    move_x = 0
    move_y = 0
    i = 0
    random_method = True
    global field_list
    for x in combinations:
        if x.count(mark) == 2 and x.count("_") == 1:
            field_list[combination_index[i * 3 + x.index("_")]] = mark
            random_method = False
            break
        elif x.count(opponent_mark) == 2 and x.count("_") == 1:
            field_list[combination_index[i * 3 + x.index("_")]] = mark
            random_method = False
            break
        i += 1
    if random_method:
        coordinates = f'{random.choice(["1", "2", "3"])} {random.choice(["1", "2", "3"])}'
        if coordinates[0] == "1":
            move_x = 0
        elif coordinates[0] == "2":
            move_x = 1
        elif coordinates[0] == "3":
            move_x = 2
        if coordinates[2] == "1":
            move_y = 0
        elif coordinates[2] == "2":
            move_y = -3
        elif coordinates[2] == "3":
            move_y = -6
        while True:
            if field_list[6 + move_x + move_y] != "_":
                return ai_medium(mark, opponent_mark, id)
            else:
                field_list[6 + move_x + move_y] = mark
                break
    result = "".join(field_list).replace("_", " ")
    print('Making move level "medium"')
    print(f"""---------
| {result[0]} {result[1]} {result[2]} |
| {result[3]} {result[4]} {result[5]} |
| {result[6]} {result[7]} {result[8]} |
---------""")
    return field_list


def check_result(field_list, mark):
    global combinations
    global status
    status = None
    if field_list.count("_") == 0:
        status = "Draw"
    combinations = [[field_list[0], field_list[1], field_list[2]],
                [field_list[3], field_list[4], field_list[5]],
                [field_list[6], field_list[7], field_list[8]],
                [field_list[0], field_list[3], field_list[6]],
                [field_list[1], field_list[4], field_list[7]],
                [field_list[2], field_list[5], field_list[8]],
                [field_list[6], field_list[4], field_list[2]],
                [field_list[0], field_list[4], field_list[8]]]
    for x in combinations:
        if x.count(mark) == 3:
            status = "Win"
            break
    return status


def empty_fields(field_list):
    empty_field_list = []
    i = 0
    for x in field_list:
        if x == "_":
            empty_field_list.append(i)
        i +=1
    return empty_field_list


def minimax(estimated_field, mark, opponent_mark, id):
    global fc
    moves = {}
    fc += 1
    best_score = -1000 * id
    best_move = None
    empty_field_list = empty_fields(estimated_field)
    check_result(estimated_field, opponent_mark)
    if status == "Win":
        score = 10 * -id
        return status, score
    elif status == "Draw":
        score = 0
        return status, score
    else:
        for x in empty_field_list:
            estimated_field[x] = mark
            if mark == "X":
                move, score = minimax(estimated_field, "O", "X", -id)
            else:
                move, score = minimax(estimated_field, "X", "O", -id)
            estimated_field[x] = "_"
            moves[x] = score
    if id > 0:
        for key, value in moves.items():
            if int(value) > best_score:
                best_score = int(value)
                best_move = key
    else:
        for key, value in moves.items():
            if int(value) < best_score:
                best_score = value
                best_move = key
    return best_move, best_score


def ai_hard(mark, opponent_mark, id):
    global field_list
    scores = []
    move_x = 0
    move_y = 0
    moves = empty_fields(field_list)
    estimated_field = field_list.copy()
    best_move, best_score = minimax(estimated_field, mark, opponent_mark, 1)
    field_list[best_move] = mark
    result = "".join(field_list).replace("_", " ")
    print('Making move level "hard"')
    print(f"""---------
| {result[0]} {result[1]} {result[2]} |
| {result[3]} {result[4]} {result[5]} |
| {result[6]} {result[7]} {result[8]} |
---------""")
    return field_list


def player_x_choice(players):
    return {"user": human, "easy": ai_easy, "medium": ai_medium, "hard": ai_hard}.get(players["player_X"]["Level"])


def player_o_choice(players):
    return {"user": human, "easy": ai_easy, "medium": ai_medium, "hard": ai_hard}.get(players["player_O"]["Level"])


status = None
players = None
player_x = None
player_o = None
field = str("           ")
field_list = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
combinations = [[field_list[0], field_list[1], field_list[2]],
            [field_list[3], field_list[4], field_list[5]],
            [field_list[6], field_list[7], field_list[8]],
            [field_list[0], field_list[3], field_list[6]],
            [field_list[1], field_list[4], field_list[7]],
            [field_list[2], field_list[5], field_list[8]],
            [field_list[6], field_list[4], field_list[2]],
            [field_list[0], field_list[4], field_list[8]]]
combination_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 3, 6, 1, 4, 7, 2, 5, 8, 6, 4, 2, 0, 4, 8]
competitors = ["user", "easy", "medium", "hard"]
fc = 0

menu()

while True:
    player_x_choice(players)("X", "O", 1)
    check_result(field_list, "X")
    if status == "Win":
        print("X wins")
        break
    elif status == "Draw":
        print("Draw")
        break
    player_o_choice(players)("O", "X", -1)
    check_result(field_list, "O")
    if status == "Win":
        print("O wins")
        break
    elif status == "Draw":
        print("Draw")
        break
