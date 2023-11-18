import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SuccefullComponent } from './pages/successfull/succefull.component';

const routes: Routes = [
	{
	 	path: 'pages',
		loadChildren: () => import('./pages/pages.module').then(x => x.PagesModule)
	},
	{ 
		path: '',
		redirectTo: 'pages/home',
		pathMatch: 'full'
	},
	{ 
		
	   path: 'succefull',
	   component: SuccefullComponent
	
	}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
