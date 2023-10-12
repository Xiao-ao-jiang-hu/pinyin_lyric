from gamedata import SkillType
from gamestate import GameState


# 本文件定义了将军战法
def skill_activate(player: int, gamestate: GameState, skillType: SkillType) -> bool:
    coin = GameState[player]

    if skillType == SkillType.SURPRISE_ATTACK:
        pass
    elif skillType == SkillType.ROUT:
        pass
    elif skillType == SkillType.COMMAND:
        pass
    elif skillType == SkillType.DEFENCE:
        pass
    else:
        pass

    pass


"""
需要根据skilltype这个enum类型(定义在gamedata中)判断要使用那个技能
根据player以及将军的技能冷却,金钱数目来判断操作是否合法
如果必要可以在gamedata中添加属性(不可以删除）
如果不合法返回false,不进行任何操作
对于增益or减益,需要更改skillsactivated属性,而对于瞬移,可以调用movement文件中的general_move(location,gamestate,player,destination)->bool:
对于击破,判断合法性后直接操作gamestate即可
操作成功后需要扣除相应的金币并返回true
"""
