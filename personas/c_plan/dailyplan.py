from LLM.llm import *

class Dailyplan:
    def __init__(self, wake_up, sleep, breakfast, lunch, dinner):
        self.dplan = []
        self.dplan.append(wake_up)
        self.dplan.append(sleep)
        self.dplan.append(breakfast)
        self.dplan.append(lunch)
        self.dplan.append(dinner)
        self.dplan.append("common human behavior")

    def change_plan(self, agent):
        prompt = agent.return_daily_log()
        # print("||---------------------------||")
        # print(prompt)
        # print("^^---------------------------^^")
        q = "Please briefly tell me what you are focusing on today and what you need to work on based on yesterday's action log."
        llm_response = Llama_request(prompt, q)
        print("||---------------------------||")
        print(llm_response)
        print("^^---------------------------^^")
        self.dplan.pop(5)
        self.dplan.append(llm_response)
        agent.today = self.dailyplan_to_string()

    def dailyplan_to_string(self):
        with open("./personas/c_plan/dailyplan_template.txt", "r") as f:
            my_todays_plan = f.read()
        for count, i in enumerate(self.dplan): 
            my_todays_plan = my_todays_plan.replace(f"!<INPUT {count}>!", i)
        return my_todays_plan

if __name__ == "__main__":
    my = Dailyplan("8:00", "23:00", "9:00", "12:00", "19:00")
    print(my.dailyplan_to_string())
