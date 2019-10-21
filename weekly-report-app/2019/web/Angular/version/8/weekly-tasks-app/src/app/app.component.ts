import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'weekly-tasks-app';
  public week_days = 
  [
    {"day":"Monday","count":[{"task":"","task_detail":""}]},
        {"day":"Tuesday","count":[{"task":"","task_detail":""}]},
        {"day":"Wednesday","count":[{"task":"","task_detail":""}]},
        {"day":"Thursday","count":[{"task":"","task_detail":""}]},
    {"day":"Friday","count":[{"task":"","task_detail":""}]}

  ];
  public list_of_tasks = []

  add_new_task(day)
  {

    for(var i =0;i < this.week_days.length;i++)
    {
      if(this.week_days[i].day == day){
        
        // this.week_days[i].count.push();
        break;
      }
    }
  }
  delete_task(day,list,row_data){
    console.log(day);
    console.log(list);
    console.log(row_data);
    for(var i =0;i < this.week_days.length;i++)
    {
      if(this.week_days[i].day == day){

        this.week_days[i].count = [];
        for(var t = 0; t < list.length;t++)
        {
          if(list[t] != row_data)
          {
            this.week_days[i].count.push(list[t]);
          }
        }
        break;
      }
    }

  }

  add_toTasks(day,task,task_detail)
  {

    var new_task = {'day':day,'task':task,'task_detail':task_detail};
    this.list_of_tasks.push(new_task);
  }

}
