import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SuccefullRoutingModule } from './succefull-routing.module';
import { SuccefullComponent } from './succefull.component';
import {MatIconModule} from '@angular/material/icon';




@NgModule({
  declarations: [
    SuccefullComponent 
  ],
  imports: [
    CommonModule,
    SuccefullRoutingModule,
    MatIconModule
  ]
})
export class SuccefullModule { 
}
