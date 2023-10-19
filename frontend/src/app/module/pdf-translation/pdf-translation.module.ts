import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UploadFileComponent } from './view/upload-file/upload-file.component';
import { PdfTranslationService } from './service/pdf-translation.service';
import { SharedModule } from '@app/shared/shared.module';



@NgModule({
  providers: [PdfTranslationService],
  declarations: [
    UploadFileComponent
  ],
  imports: [
    CommonModule,
    SharedModule
  ]
})
export class PdfTranslationModule { }
