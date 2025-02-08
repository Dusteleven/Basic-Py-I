# Write your solution here

def who_won(game_board: list):
    c1=0
    c2=0
    for rows in game_board:
        for e in rows:
            if e ==1:
                c1+=1
            elif e==2:
                c2+=1
    if c1 > c2:
        return 1
    elif c2 > c1:
        return 2
    else: return 0


if __name__ == "__main__":
    go = [[0, 1, 0, 2, 2, 1, 0], [2, 1, 2, 0, 2, 1, 2], [1, 2, 2, 0, 0, 2, 1], [1, 2, 1, 2, 2, 0, 1], [1, 0, 1, 0, 2, 0, 1], [0, 2, 0, 0, 1, 1, 0], [2, 2, 0, 0, 1, 0, 2]]
    print(who_won(go)) 