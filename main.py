import random

import constant
from gamedata import Farmer, MainGenerals, SubGenerals, SuperWeapon, WeaponType
from gamestate import GameState, init_generals, update_round

constant.mountain_percent = random.uniform(0.05, 0.1)
constant.bog_percent = random.uniform(0.05, 0.25)
state = GameState()  # 每局游戏唯一的游戏状态类，所有的修改应该在此对象中进行
init_generals(state)
player0: int = 0
player1: int = 1
# 分别代表两个玩家，0是第一个玩家，1是第二个玩家，与gamestate里的相对应


def show_state(state: GameState):
    def print_color(color, end, message, background="0"):
        print("\033[" + color + ";" + background + "m" + message + "\033[0m", end=end)

    print("   ", end="")
    for i in range(25):
        print(str(format(i, "03d")), end="")
    print("")
    for i in range(constant.row):
        print(str(format(i, "03d")), end="")
        for j in range(constant.col):
            if state.board[i][j].generals != None:
                if state.board[i][j].generals.player == 0:
                    if isinstance(state.board[i][j].generals, MainGenerals):
                        print_color(
                            "0", "", str(format(state.board[i][j].army, "03d")), "41"
                        )
                    elif isinstance(state.board[i][j].generals, SubGenerals):
                        print_color(
                            "0", "", str(format(state.board[i][j].army, "03d")), "41"
                        )
                    elif isinstance(state.board[i][j].generals, Farmer):
                        print_color(
                            "0", "", str(format(state.board[i][j].army, "03d")), "41"
                        )

                elif state.board[i][j].generals.player == 1:
                    if isinstance(state.board[i][j].generals, MainGenerals):
                        print_color(
                            "0", "", str(format(state.board[i][j].army, "03d")), "44"
                        )
                    elif isinstance(state.board[i][j].generals, SubGenerals):
                        print_color(
                            "0", "", str(format(state.board[i][j].army, "03d")), "44"
                        )
                    elif isinstance(state.board[i][j].generals, Farmer):
                        print_color(
                            "0", "", str(format(state.board[i][j].army, "03d")), "44"
                        )

                elif state.board[i][j].generals.player == -1:
                    if isinstance(state.board[i][j].generals, MainGenerals):
                        print_color(
                            "0", "", str(format(state.board[i][j].army, "03d")), "46"
                        )
                    elif isinstance(state.board[i][j].generals, SubGenerals):
                        print_color(
                            "0", "", str(format(state.board[i][j].army, "03d")), "46"
                        )
                    elif isinstance(state.board[i][j].generals, Farmer):
                        print_color(
                            "0", "", str(format(state.board[i][j].army, "03d")), "46"
                        )
            else:
                if int(state.board[i][j].type) == 0:
                    print_color(
                        "0", "", str(format(state.board[i][j].army, "03d")), "47"
                    )
                elif int(state.board[i][j].type) == 1:
                    print_color(
                        "0", "", str(format(state.board[i][j].army, "03d")), "42"
                    )
                elif int(state.board[i][j].type) == 2:
                    print_color(
                        "0", "", str(format(state.board[i][j].army, "03d")), "43"
                    )
                else:
                    print(int(state.board[i][j].type), end=" ")
        print("")
    print("round:", state.round)
    print("coins:", state.coin)
    print("super weapons:", state.active_super_weapon)
    print("super weapon cds:", state.super_weapon_cd)
    print("generals:")
    for i in state.generals:
        print(i)


while 1:
    update_round(state)
    show_state(state)
    a = input()
    if a != "":
        if int(a) == 1:
            state.active_super_weapon.append(
                SuperWeapon(WeaponType(0), 0, 10, 10, [8, 8])
            )
            state.super_weapon_cd[0] = 10
