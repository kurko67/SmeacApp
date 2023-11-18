import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SuccefullComponent } from './succefull.component';

const routes: Routes = [{
  path: '',
  component: SuccefullComponent
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SuccefullRoutingModule { }
