from map import vill

class Memory:
    def __init__(self, time, contents, value=0):
        self.time = time
        self.contents = contents
        self.value = value

class Agent:
    def __init__(self, village, dailyplan, name="", position=[0,0], text=""):
        self.name = name
        self.position = position
        self.daily_log = []
        self.curr_log = []
        self.neartiles = self.get_neartiles(village)
        self.personality = self.get_personality(text)
        self.today = dailyplan
        self.distinetion = " "
        self.inhouse= True

    def get_neartiles(self, village):
        village = vill.get_village()
        x = self.position[0]
        y = self.position[1]
        z = village[x-2:x+3]
        for c, i in enumerate(z):
            z[c] = i[y-2:y+3]
        return z
    
    def get_personality(self, text):
        with open(text, "r") as f:
            data = f.read()
        return data

    def set_mylog(self, action, datetime):
        # logはMemory型
        log = Memory(datetime.print_en_time(), action)
        self.daily_log.append(log)
        log = Memory(datetime.print_hour_minute(), action)
        self.curr_log.append(log)
        self.curr_log.pop(0)
    
    def return_daily_log(self):
        log_txt = ""
        for i in self.daily_log:
            str = i.time
            log_txt += str
            log_txt += " "
            str = i.contents
            log_txt += str
            log_txt += "\n"
        # print(log_txt)
        return log_txt

    # def return_curr_log(self, n):
    #     # with open("./character/curr_log_template.txt", "r") as f:
    #     #     log_txt = f.read()

    #     count=0
    #     log_txt = ""
    #     for i in reversed(list(self.curr_log)):
    #         log_txt = log_txt + f"{i.time} {i.contents}"
    #         # print(n, ":", count)
    #         if count == n-1:
    #             break
    #         count += 1
    #         # log_txt = log_txt.replace(f"!<INPUT {count}>!", i.time)
    #         # count += 1
    #         # log_txt = log_txt.replace(f"!<INPUT {count}>!", i.contents)
    #         # count += 1
    #     # print(log_txt)
    #     return log_txt

    def delete_daily_log(self):
        self.mylog = []
    
    def init_curr_log(self, current):
        self.curr_log.append(Memory("6:10", "sleeping"))
        self.curr_log.append(Memory("6:20", "sleeping"))
        self.curr_log.append(Memory("6:30", "sleeping"))
        self.curr_log.append(Memory("6:40", "sleeping"))
        self.curr_log.append(Memory("6:50", "sleeping"))
