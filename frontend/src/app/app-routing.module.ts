import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UploadFileComponent } from './module/pdf-translation/view/upload-file/upload-file.component';

const routes: Routes = [
  {
    path: "pdf-translation",
    component: UploadFileComponent
  },
  {
    path: "",
    pathMatch: "full",
    redirectTo: "pdf-translation"
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
