from classes import systeminformation,weeklycalendar,report,print_statements,tasks
import os.path

class weeklyreport:
    filename = ""
    sys_info = systeminformation.system_information()
    weekly_calender = weeklycalendar.weeklycalendar()
    list_of_tasks = []
    write_report = report.report()
    print_statements_for_app = print_statements.print_statements()
    default_user_directory = ""
    completed_reports_directory_path = ""
    app_start = False
    user_name = str()
    default_username_from_file = str()
    developer="Daniel Medina"
    title="Weekly Tasks"
    description="Print out tasks for work days MONDAY - FRIDAY"
    output_filename = ""
    output_filename_path = ""

    def set_default_username_file(self):
        if not self.sys_info.os_name == "windows":
            self.default_username_from_file = self.default_user_directory + "/defaultuser.txt"
        else:
            self.default_username_from_file = self.default_user_directory + "\defaultuser.txt"

    def check_defaultuser(self):
        return self.defaultuser_directory_exists()

    def ask_for_username(self):
        self.user_name = self.input_check("Enter First and Last name: ").title()

    def create_default_user_file(self):        
        with open(self.default_username_from_file,"w") as file:
            file.write(self.user_name)

    def get_username_from_defaultuser(self):
        with open(self.default_username_from_file) as f:
            for b in f:
                self.user_name = b

    def weekend_message(self):
        mList = []
        mList.append("Today is not a workday")
        mList.append(self.weekly_calender.todays_date_pretty)
        self.print_statements_for_app.print_ending(mList)

    def loopthroughwork_days(self):
        for d in self.weekly_calender.days_of_work_week_with_date:
            new_task = tasks.tasks()
            print()
            print("type exit to exit current day")
            print()
            print(f"{d} Task")
            task_name_input = self.input_check("Task Name: ")
            new_task.task_day = d
            new_task.tasks = []
            while task_name_input.lower() != "exit":
                task_description_input = self.input_check(f"Description: ")
                new_task.addtask(task_name_input,task_description_input)
                print()
                print(f"Current Tasks for: {d}")
                for n in new_task.tasks:
                    print(n["Task_Name"])
                print()
                task_name_input = self.input_check("Task Name: ")

            if len(new_task.tasks) > 0:
                self.list_of_tasks.append(new_task)

    def ending_messages(self):
        response = []
        response.append("Report Successfully Generated!")
        response.append("Report Name")
        response.append(self.output_filename)
        response.append("Save Location")
        response.append(self.output_filename_path)
        self.print_statements_for_app.print_ending(response)
                

    def workday_today(self):
        if self.weekly_calender.isworkday:
            return True
        else:
            return False


    def input_check(self,textToDisplay):
        response = input(str(textToDisplay))
        while len(response) <= 0:
            print("Cannot be empty. Please enter text")
            response = input(str(textToDisplay))
            print()
        else:
            return response
    
    def defaultuser_directory_exists(self):
        self.default_user_directory = ""
        if self.sys_info.os_name == "windows":
            self.default_user_directory = self.sys_info.current_working_directory +  "\defaultuser"
        else:
            self.default_user_directory = self.sys_info.current_working_directory + "/" + "defaultuser"
        
        self.set_default_username_file()
        if not os.path.exists(self.default_user_directory):
            return False
        else: 
            return True
    
    def completed_reports_directory_exists(self):
        self.completed_reports_directory_path = ""
        if self.sys_info.os_name == "windows":
            self.completed_reports_directory_path = self.sys_info.current_working_directory + "\completed_reports"
        else:
            self.completed_reports_directory_path = self.sys_info.current_working_directory + "/completed_reports"
        
        if not os.path.exists(self.completed_reports_directory_path):
            return False
        else:
            return True
    
    def create_defaultuser_directory(self):
        os.makedirs(self.default_user_directory)

    def create_completed_reports_directory(self):
        os.makedirs(self.completed_reports_directory_path)

    def create_output_file(self):
        if not self.completed_reports_directory_exists():
            self.create_completed_reports_directory()
        _dayf = "weekly_report_" + str(self.weekly_calender.todays_date.month) + str(self.weekly_calender.todays_date.day) + str(self.weekly_calender.todays_date.year) + str(self.weekly_calender.todays_date.hour) + str(self.weekly_calender.todays_date.minute) + ".txt" 
        _filename = ""
        if self.sys_info.os_name == "windows":
            _filename = self.completed_reports_directory_path + f"\{_dayf}"
        else:
            _filename = self.completed_reports_directory_path + f"/{_dayf}"

        self.output_filename_path = _filename
        self.output_filename = _dayf

        self.write_report.write_output_file_tasks(_filename,self.list_of_tasks,self.developer,self.weekly_calender.todays_date_pretty)

    def ask_for_report_title(self):
        self.title = input(str("What is the report title you want to use when you finish entering tasks? Default is Weekly Tasks: "))
        print()
        confirm = f"Report title is: {self.title}. Is that correct?(y/n)"
        yesno = input(str(confirm))
        while yesno.lower() == "n":
            self.title = input(str("What is the report title you want to use when you finish entering tasks? Default is Weekly Tasks: "))
            confirm = f"Report title is: {self.title}. Is that correct?(y/n)"
            yesno = input(str(confirm))

    def newuserpath(self):
        self.create_defaultuser_directory()
        self.print_statements_for_app.print_intro(self.title,self.developer,self.description)
        self.ask_for_username()
        self.create_default_user_file()
        self.ask_for_report_title()
        self.loopthroughwork_days()
        self.create_output_file()
        self.ending_messages()
    def useralreadycreatedpath(self):
        #defaultuser directory exists
    # app.create_defaultuser_directory()
        self.print_statements_for_app.print_intro(self.title,self.developer,self.description)
    # app.ask_for_username()
        self.get_username_from_defaultuser()
        self.ask_for_report_title()
        self.loopthroughwork_days()
        self.create_output_file()
        self.ending_messages()

app = weeklyreport()

if app.check_defaultuser():
    app.useralreadycreatedpath()
else:
    app.newuserpath()
    


