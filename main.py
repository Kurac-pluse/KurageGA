from character.agents import Agent
from LLM.llm import *
from personas.c_plan.dailyplan import *
from personas.a_perceive.perceive import *
from personas.b_retrieve.retrieve import *
#from personas.c_plan import plan
#from personas.d_reflect import reflect
#from personas.e_execute import execute
from map import vill
from time_management.daytime import Daytime
import time

datetime = Daytime()
datetime.set_daytime(2024,1,1,7,0)
village = vill.get_village()
plan1 = Dailyplan(wake_up="8:00", sleep="22:00", breakfast="9:00", lunch="12:00", dinner="18:00")
plan2 = Dailyplan(wake_up="9:00", sleep="23:30", breakfast="9:15", lunch="13:00", dinner="18:00")
agent1 = Agent(village,plan1.dailyplan_to_string(),name="agent1",
               position=[2,2],text="./personality/agent1.txt")
agent2 = Agent(village,plan2.dailyplan_to_string(),name="agent2",
               position=[30,2],text="./personality/agent2.txt")
agent1.init_curr_log(datetime)
agent2.init_curr_log(datetime)

for i in range(10):
    while(datetime.is_day_over() == False):
        # 現在時間の出力
        print(datetime.print_jp_time())
        # agentsが周囲の環境を認識する
        around1 = get_perceive(agent1)
        around2 = get_perceive(agent2)
        
        # agentsが環境からイベントを取得&実行
        events1 = get_retrieve(agent1, around1, agent2, datetime, destination="")
        print("person1:",events1)
        events2 = get_retrieve(agent2, around2, agent1, datetime, destination="")
        print("person2:",events2)
        print()

        # agentsが計画した場所へ移動する
        # print("person1:", point11, "->", point12)
        # print("person2:", point21, "->", point22)
        
        # 10分進める
        for i in range(10):
            datetime.time_lapse()
    print("-----------------------------------------------------------------------")
    # 今日の行動logから明日の計画を立てる
    plan1.change_plan(agent1)
    plan2.change_plan(agent2)
    # 今日の行動logを削除
    agent1.delete_daily_log()
    agent2.delete_daily_log()
    # 10分進める
    for i in range(10):
        datetime.time_lapse()
