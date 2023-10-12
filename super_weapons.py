from gamestate import GameState


# 本文件定义了超级武器
def bomb(gamestate: GameState, location: list[int, int], player: int) -> bool:
    pass


def strengthen(gamestate: GameState, location: list[int, int], player: int) -> bool:
    pass


def tp(
    gamestate: GameState, start: list[int, int], to: list[int, int], player: int
) -> bool:
    pass


def timestop(gamestate: GameState, location: list[int, int], player: int) -> bool:
    pass


"""
location类型为list
这部分需要完成四个超级武器的逻辑,接受gamestate参数
首先需要根据player,科技是否解锁,金钱数判断操作是否合法,不合法返回false
若为合法操作,则需要在gamestate中更新对应的状态
对于bomb,你需要更新location周围的兵力和将军(消灭他们)
对于强化,你需要只需要更新gamestate即可
对于tp,你需要判断操作是否合法,并将军队更新
对于时间停止,只需要在gamestate中更新即可
! ! !建议参考demo的写法
"""
