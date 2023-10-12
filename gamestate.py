# 本文件定义了游戏状态类，以及负责初始化将军，更新回合的函数
import random
from dataclasses import dataclass, field

from constant import *
from gamedata import (
    Cell,
    Farmer,
    Generals,
    MainGenerals,
    SubGenerals,
    SuperWeapon,
    init_coin,
)


@dataclass
class GameState:
    round: int = 0  # 当前游戏回合数
    generals: list[Generals] = field(default_factory=list)  # 游戏中的将军列表，用于通信
    coin: list[int] = field(
        default_factory=lambda: [init_coin() for p in range(2)]
    )  # 每个玩家的金币数量列表，分别对应玩家1，玩家2
    active_super_weapon: list[SuperWeapon] = field(default_factory=list)
    super_weapon_unlocked: list[bool] = field(
        default_factory=lambda: [False, False]
    )  # 超级武器是否解锁的列表，解锁了是true，分别对应玩家1，玩家2

    super_weapon_cd: list[int] = field(
        default_factory=lambda: [-1, -1]
    )  # 超级武器的冷却回合数列表，分别对应玩家1，玩家2

    tech_level: list[list[int]] = field(
        default_factory=lambda: [[0, 0, 0, 0], [0, 0, 0, 0]]
    )
    # 科技等级列表，第一层对应玩家一，玩家二，第二层分别对应行动力，攀岩，免疫沼泽，超级武器

    board: list[list[Cell]] = field(
        default_factory=lambda: [[Cell() for j in range(col)] for i in range(row)]
    )  # 游戏棋盘的二维列表，每个元素是一个Cell对象


def init_generals(gamestate: GameState):
    # init random position
    positions = []
    for i in range(row):
        for j in range(col):
            positions.append([i, j])
    random.shuffle(positions)

    # generate main generals
    for player in range(2):
        gen = MainGenerals(player=player)
        pos = positions.pop()
        gen.position[0] = pos[0]
        gen.position[1] = pos[1]
        gamestate.generals.append(gen)
        gamestate.board[pos[0]][pos[1]].generals = gen

    # generate sub generals
    for player in range(2):
        gen = SubGenerals(player=player)
        pos = positions.pop()
        gen.position[0] = pos[0]
        gen.position[1] = pos[1]
        gamestate.generals.append(gen)
        gamestate.board[pos[0]][pos[1]].generals = gen
    # generate farmer
    for i in range(8):
        gen = Farmer(player=random.randint(0, 1), produce_level=1)
        pos = positions.pop()
        gen.position[0] = pos[0]
        gen.position[1] = pos[1]
        gamestate.generals.append(gen)
        gamestate.board[pos[0]][pos[1]].generals = gen


def update_round(gamestate: GameState):
    for i in range(row):
        for j in range(col):
            if isinstance(gamestate.board[i][j].generals, MainGenerals):
                gamestate.board[i][j].army += 1
            elif isinstance(gamestate.board[i][j].generals, SubGenerals):
                gamestate.board[i][j].army += 1
            elif isinstance(gamestate.board[i][j].generals, Farmer):
                if gamestate.board[i][j].generals.player != -1:
                    if gamestate.board[i][j].generals.produce_level == 1:
                        gamestate.coin[gamestate.board[i][j].generals.player] += 1
                    elif gamestate.board[i][j].generals.produce_level == 2:
                        gamestate.coin[gamestate.board[i][j].generals.player] += 2
                    elif gamestate.board[i][j].generals.produce_level == 3:
                        gamestate.coin[gamestate.board[i][j].generals.player] += 5


# 每一回合结束后均需要调用，需要根据游戏状况正确更新棋盘（将军的生产，沼泽对兵力的削减）
