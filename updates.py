from gamestate import GameState


# 本文件中的函数负责升级将军，解锁技能等，需要的金币从demo里的constant.py中调取，方便修改
def production_up(location: list[int, int], gamestate: GameState, player: int) -> bool:
    pass


def defence_up(location: list[int, int], gamestate: GameState, player: int) -> bool:
    pass


def movement_up(location: list[int, int], gamestate: GameState, player: int) -> bool:
    pass


"""
以上部分是将军升级的函数，接受location，gamestate，player参数，其中。location是一个list，location[0]为x坐标，location[1]为y坐标
gamestate为全局唯一的对象，而player传入player0或player1，这是为了防止恶意操纵他人的格子
在这三个函数里，首先需要通过location找到具体操作的格子，接下来判断该操作是否合法(是否操作了他人格子，钱是否够，格子上是否有将军)，
如果不合法则不扣除金币，不进行操作，返回Flase
如果合法则通过操作gamestate.board[location[0]][location[1]].generals对属性进行修改，并扣除相应的金币

"""


def tech_update(
    tech_type: int, gamestate: GameState, player: int
) -> bool:  # 规定0123分别代表文档中的对应序号科技
    pass


"""
你需要根据type判断升级什么科技，根据player判断升级谁的科技，并判断是否合法（是否还能升级？钱是否够），不合法返回false
你需要根据科技种类和当前等级扣除对应金币，并更改gamestate中的科技状态，若成功则返回True
"""
