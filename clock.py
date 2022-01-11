
class Clock:
    def __init__(self, day = 0, month = 0, year = 0, hour = 0, min = 0, sec = 0):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__hour = hour
        self.__min = min
        self.__sec = sec

    def inc_sec(self):
        self.__sec += 1
        if self.__sec == 60:
            self.inc_min()
            self.__sec = 0
    
    def inc_min(self):
        self.__min += 1
        if self.__min == 60: 
            self.inc_hour()
            self.__min = 0
    
    def inc_hour(self):
        self.__hour += 1
        if self.__hour == 24:
            self.inc_day()
            self.__hour = 0
    
    def leapyear(self): 
        if self.__year % 4 == 0 and self.__year % 100 != 0 or self.__year % 400 == 0: 
            return 0
        else: 
            return 1
    
    def inc_day(self):
        self.__day += 1
        if self.__month == 1 and self.__day == 32 or self.__month == 3 and self.__day == 32 \
            or self.__month == 5 and self.__day == 32 or self.__month == 7 and self.__day == 32 \
            or self.__month == 8 and self.__day == 32 or self.__month == 10 and self.__day == 32 \
            or self.__month == 12 and self.__day == 32:
            self.__day = 1
            self.inc_month()
        elif self.__month == 4 and self.__day == 31 or self.__month == 6 and self.__day == 31 \
            or self.__month == 9 and self.__day == 31 or self.__month == 11 and self.__day == 31: 
            self.__day = 1
            self.inc_month()
        elif self.__month == 2 and self.leapyear() == 1 and self.__day >= 29: 
            self.__day = 1 
            self.inc_month()
        elif self.__month == 2 and self.leapyear() == 0 and self.__day == 30: 
            self.__day = 1
            self.inc_month()

    
    def inc_month(self):
        self.__month +=1
        if self.__month == 13: 
            self.inc_year()
            self.__month = 1
    
    def inc_year(self): 
        self.__year +=1
    
    def clock_as_string(self):
        return f'{self.__day:0>2}:{self.__month:0>2}:{self.__year:0>4}:{self.__hour:0>2}:{self.__min:0>2}:{self.__sec:0>2}'
    
    def set_clock(self, day, month, year, hour, min, sec):
        Clock(day, month, year, hour, min, sec)



