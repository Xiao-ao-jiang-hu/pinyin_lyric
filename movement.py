from computation import compute_attack, compute_defence
from gamedata import CellType, Direction
from gamestate import GameState

# TODO 设置全局常量
MAX_LENGTH = 25

# 本文件用于实现将军和军队的移动逻辑


def outrange(location: list[int, int]) -> bool:  # 判断越界
    return (
        location[0] < 0
        or location[0] >= MAX_LENGTH
        or location[1] < 0
        or location[1] >= MAX_LENGTH
    )


def calculate_new_pos(
    location: list[int, int], direction: Direction
) -> tuple[int, int]:  # 计算目标位置
    if direction == Direction.UP:
        newX = location[0] - 1
        newY = location[1]
    if direction == Direction.DOWN:
        newX = location[0] + 1
        newY = location[1]
    if direction == Direction.LEFT:
        newX = location[0]
        newY = location[1] - 1
    if direction == Direction.RIGHT:
        newX = location[0]
        newY = location[1] + 1
    if outrange([newX, newY]):
        return (-1, -1)
    return (newX, newY)


def army_move(
    location: list[int, int],
    gamestate: GameState,
    player: int,
    direction: Direction,
    num: int,
) -> bool:  # 军队移动
    x, y = location[0], location[1]
    if outrange(location):  # 越界
        return False
    if player != 0 and player != 1:  # 玩家参数非法
        return False
    if gamestate.board[x][y].player != player:  # 操作格子非法
        return False

    if num <= 0:  # 移动数目非法
        return False
    if num >= gamestate.board[x][y].army - 1:  # 超过最多移动兵力
        num = gamestate.board[x][y].army - 1

    newX, newY = calculate_new_pos(location, direction)
    if newX < 0:  # 越界
        return False
    if (
        gamestate.board[newX][newY].type == CellType.MOUNTAIN
        and gamestate.tech_level[player][1] == 0
    ):  # 不能爬山
        return False

    if gamestate.board[newX][newY].player == player:  # 目的地格子己方所有
        gamestate.board[newX][newY].army += num
        gamestate.board[x][y].army -= num

    elif gamestate.board[newX][newY].player == -1:  # 目的地格子无主
        gamestate.board[newX][newY].army += num
        gamestate.board[newX][newY].player = player
        gamestate.board[x][y].army -= num

    elif gamestate.board[newX][newY].player == 1 - player:  # 攻击敌方格子
        attack = compute_attack(gamestate.board[x][y], gamestate)
        defence = compute_defence(gamestate.board[newX][newY], gamestate)
        vs = num * attack - gamestate.board[newX][newY].army * defence
        if vs > 0:  # 攻下
            gamestate.board[newX][newY].player = player
            gamestate.board[newX][newY].army = vs // attack
            gamestate.board[x][y].army -= num
        elif vs <= 0:  # 防住
            gamestate.board[newX][newY].army = -vs // defence
            gamestate.board[x][y].army -= num

    return True


def general_move(
    location: list[int, int],
    gamestate: GameState,
    player: int,
    destination: list[int, int],
) -> bool:  # 将军移动（参数须保证合法）
    x, y = location[0], location[1]
    newX, newY = destination[0], destination[1]
    gamestate.board[newX][newY].generals = gamestate.board[x][y].generals
    gamestate.board[x][y].generals = None
    return True


def check_general_movement(
    location: list[int, int],
    gamestate: GameState,
    player: int,
    destination: list[int, int],
) -> bool:  # 检查将军移动合法性
    x, y = location[0], location[1]
    if outrange(location):  # 越界
        return False
    if player != 0 and player != 1:  # 玩家非法
        return False
    if (
        gamestate.board[x][y].player != player or gamestate.board[x][y].generals == None
    ):  # 起始格子非法
        return False

    newX, newY = destination[0], destination[1]
    if outrange([newX, newY]):  # 越界
        return False
    if (
        gamestate.board[newX][newY].type == CellType.MOUNTAIN
        and gamestate.tech_level[player][1] == 0
    ):  # 不能爬山
        return False
    if (
        gamestate.board[newX][newY].player != player
        or gamestate.board[newX][newY].generals != None
    ):  # 目的地格子非法
        return False

    # 行动力不足
    if abs(newX - x) + abs(newY - y) > gamestate.board[x][y].generals.mobility_level:
        return False

    return True


"""
这两个函数分别处理军队移动和将军移动。
！！！这一部分一定要理解游戏规则，可以看和demo版本代码逻辑是否相同

军队移动接受操作的位置（list类型），当前游戏状态，操作的玩家（int类型），移动的方向（建议参考demo），移动军队数目
gamestate.board[location[0]][location[1]]可访问到被操作的棋盘
首先，需要判断操作是否合法（例如不能操作别人的地盘），是否尝试移动到棋盘外面，山脉上等，若有不合法操作，返回false，不进行任何操作
其次，根据方向执行军队移动的逻辑，注意：需要分成三种情况（移动到自己地盘，移动到中立地盘，移动到对手地盘）（可以通过demo代码重构）
你需要计算剩余的军队数，此时需要知道本格的attack和defence，这可以通过调用computation.py里的函数得到
最终需要根据计算结果正确更新cell.player属性，cell.army属性

将军移动接受操作的位置（list类型），当前游戏状态，操作的玩家（int类型），移动的终点（与demo不同！）
(check...函数中)首先，需要判断操作是否合法，与军队移动不同的是，移动的终点需要根据将军的行动力（行动力是4，代表起点到终点最短距离应该不大于4）判断是否合法
你需要正确更改cell.generals属性即可

"""
