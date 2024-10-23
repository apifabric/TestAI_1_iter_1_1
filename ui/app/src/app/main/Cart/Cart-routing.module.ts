import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CartHomeComponent } from './home/Cart-home.component';
import { CartNewComponent } from './new/Cart-new.component';
import { CartDetailComponent } from './detail/Cart-detail.component';

const routes: Routes = [
  {path: '', component: CartHomeComponent},
  { path: 'new', component: CartNewComponent },
  { path: ':id', component: CartDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Cart-detail-permissions'
      }
    }
  }
];

export const CART_MODULE_DECLARATIONS = [
    CartHomeComponent,
    CartNewComponent,
    CartDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CartRoutingModule { }