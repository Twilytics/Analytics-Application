import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HomeComponent} from './home/home.component';
import {SamplePageOneComponent} from './sample-page-one/sample-page-one.component';
import {SamplePageTwoComponent} from './sample-page-two/sample-page-two.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'sample-page-1', component: SamplePageOneComponent },
  { path: 'sample-page-2', component: SamplePageTwoComponent },
  {
    path: '',
    redirectTo: '/home',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
