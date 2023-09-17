import random as r

name_list = ["Ramtin", "Annika", "Saeed", "Alex",
             "Mohammed", "Zainab", "Tove", "Ismail", "Marcial"]

print(name_list[r.randint(1, len(name_list))])

chess_row = ["a", "b", "c", "d", "e", "f", "g", "h"]
chess_col = [1, 2, 3, 4, 5, 6, 7, 8]
chess_board = [[(x, y) for x in chess_row] for y in chess_col]
print(chess_board)
