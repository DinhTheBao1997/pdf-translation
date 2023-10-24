import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { SidebarComponent } from './ui/sidebar/sidebar.component';
import { Utilities } from './utility/utilities';
import { ApiService } from './service/api.service';
import { LoadingComponent } from './ui/loading/loading.component';
import { NgxLoadingModule } from "ngx-loading";
import { LoadingService } from './service/loading.service';



@NgModule({
  providers: [Utilities, ApiService, LoadingService],
  declarations: [
    SidebarComponent,
    LoadingComponent
  ],
  imports: [
    HttpClientModule,
    CommonModule,
    NgxLoadingModule,
  ],
  exports: [
    SidebarComponent
  ]
})
export class SharedModule { }
