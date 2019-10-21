import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TaskModule } from './task/task.module';



@NgModule({
  declarations: [],
  imports: [
    CommonModule,TaskModule
  ],
  exports:[TaskModule]
})
export class ComponentsModule { }
