class tasks:
    task_day = str()
    tasks = list()

    def addtask(self,task_name,task_details):
        new_task = dict()
        new_task["Task_Name"] = task_name
        new_task["Task_Details"] = task_details
        self.tasks.append(new_task)
    
    def clearlist(self):
        self.tasks.clear()
