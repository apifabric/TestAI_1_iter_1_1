import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NewsHomeComponent } from './home/News-home.component';
import { NewsNewComponent } from './new/News-new.component';
import { NewsDetailComponent } from './detail/News-detail.component';

const routes: Routes = [
  {path: '', component: NewsHomeComponent},
  { path: 'new', component: NewsNewComponent },
  { path: ':id', component: NewsDetailComponent,
    data: {
      oPermission: {
        permissionId: 'News-detail-permissions'
      }
    }
  }
];

export const NEWS_MODULE_DECLARATIONS = [
    NewsHomeComponent,
    NewsNewComponent,
    NewsDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class NewsRoutingModule { }