class report:
    report_type = "weekly"

    def write_output_file(self, filename, list_of_work_days, list_of_tasks, author_name, date_of_report):
        if self.report_type == "weekly":
            with open(filename) as file:
                file.write("Weekly Report/Tasks\n")
                file.write("")
                file.write(f"{author_name}\n")
                file.write("")
                file.write("\n")
                for i in list_of_work_days:
                    file.write(f"{i}\n")
                    file.write("")
                    for num, task in enumerate(list_of_tasks):
                        file.write(f"{num}.Name: {task['Task_Name']}\n")
                        file.write("")
                        file.write(f"Details: {task['Task_Details']}\n")
                        file.write("")
                        file.write("\n")
                    file.write("\n")

    def write_output_file_tasks(self, filename, list_of_tasks, author_name, date_of_report,title):
        if self.report_type == "weekly":
            with open(filename,"w") as file:
                file.write(f"{title}\n")
                file.write("")
                file.write(f"{author_name}\n")
                file.write("")
                file.write("\n")
                for i in list_of_tasks:
                    file.write(f"{i.task_day}\n")
                    file.write("")
                    for num, task in enumerate(i.tasks,start=1):
                        file.write(f"{num}.Name: {task['Task_Name']}\n")
                        file.write("")
                        file.write(f"Details: {task['Task_Details']}\n")
                        file.write("")
                        file.write("\n")
                    file.write("\n")
