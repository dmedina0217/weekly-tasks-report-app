# from datetime import datetime
from datetime import datetime, timedelta

class weeklycalendar:

    todays_date = datetime.now()
    isworkday = False
    weekend_message = list()
    todays_date_pretty = todays_date.ctime()
    day_of_week = todays_date.isoweekday()
    days_of_work_week_with_date = []

    def __init__(self):
        #check if current day is a workday
        if self.todays_date.isoweekday() <=  5:
            self.isworkday = True
            self.days_of_work_week_with_date = self.getdaysofweek_withdate()
        else:
            self.weekend_message.append("Today is not a workday!")
            self.weekend_message.append(self.todays_date_pretty)
     
    def print_weekend_message(self):
        print()
        for m in self.weekend_message:
            print(m)
    
    def getdaysofweek_withdate(self):
        listresponse = self.getweeklistdate(self.get_monday_date())
        return listresponse

    def get_monday_date(self):
        if self.day_of_week == 1:
            return self.todays_date
        elif self.day_of_week > 1:
            date_to_return = datetime.today()
            count = self.day_of_week
            while count != 1:
                date_to_return = date_to_return - timedelta(days=1)
                count-=1
            else:
                return date_to_return

    def getweeklistdate(self,monday_date):
        count = 0
        response_list = []
        work_days = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY"]
        while count < 5:
            new_date = monday_date + timedelta(days=count)
            month = new_date.month
            day = new_date.day
            year = new_date.year
            work_day_from_list = work_days[count]
            response_day = f"{work_day_from_list} {month}/{day}/{year}"
            response_list.append(response_day)
            count+=1
        return response_list
        # while count <= loopcount:

# test = weeklycalendar()

# test.getdaysofweek_withdate()

       
        
            
