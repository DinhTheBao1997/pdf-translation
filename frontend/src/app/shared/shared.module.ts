import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { SidebarComponent } from './ui/sidebar/sidebar.component';
import { Utilities } from './utility/utilities';
import { ApiService } from './service/api.service';



@NgModule({
  providers: [Utilities, ApiService],
  declarations: [
    SidebarComponent
  ],
  imports: [
    HttpClientModule,
    CommonModule
  ],
  exports: [
    SidebarComponent
  ]
})
export class SharedModule { }
