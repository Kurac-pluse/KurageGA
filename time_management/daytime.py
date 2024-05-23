class Daytime():
    def __init__(self):
        self.year = 2024
        self.month = 1
        self.day = 1
        self.hour = 0
        self.minute = 00
    
    def set_daytime(self,year,month,day,hour,minute):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
    
    def time_lapse(self):
        self.minute = self.minute + 1
        self.minute_over()
        self.hour_over()
        self.day_over()
        self.month_over()

    def print_jp_time(self):
        minute = self.minute
        if self.minute < 10:
            minute = str(self.minute).zfill(2)
        return f"{self.year}年{self.month}月{self.day}日 {self.hour}:{minute}"

    def print_en_time(self):
        minute = self.minute
        if self.minute < 10:
            minute = str(self.minute).zfill(2)
        
        if self.month == 1:
            month = "January"
        if self.month == 2:
            month = "February"
        if self.month == 3:
            month = "March"
        if self.month == 4:
            month = "April"
        if self.month == 5:
            month = "May"
        if self.month == 6:
            month = "June"
        if self.month == 7:
            month = "July"
        if self.month == 8:
            month = "August"
        if self.month == 9:
            month = "September"
        if self.month == 10:
            month = "October"
        if self.month == 11:
            month = "November"
        if self.month == 12:
            month = "December"
        return f"{month} {self.day}, {self.year} at {self.hour}:{minute}."
    
    def print_hour_minute(self):
        minute = self.minute
        if minute < 10:
            minute = str(self.minute).zfill(2)
        return f"{self.hour}:{minute}"

    def is_day_over(self):
        if self.hour == 0 and self.minute == 0:
            return True
        return False

    def minute_over(self):
        if self.minute == 60:
            self.minute = 0
            self.hour = self.hour + 1
    
    def hour_over(self):
        if self.hour == 24:
            self.hour = 0
            self.day = self.day + 1
    
    def day_over(self):
        if self.day == 31:
            self.day = 1
            self.month = self.month + 1

    def month_over(self):
        if self.month == 13:
            self.month = 1
            self.year = self.year + 1

if __name__ == "__main__":
    d = Daytime()
    d.set_daytime(2024,2,4,5,7)
    while(1):
        d.time_lapse()
        d.print_jp_time()
