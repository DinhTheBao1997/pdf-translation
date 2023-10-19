import { Component } from '@angular/core';
import { FileAttachmentCore } from '@app/shared/core/FileAttachmentCore';
import { PdfTranslationService } from '../../service/pdf-translation.service';

@Component({
  selector: 'app-upload-file',
  templateUrl: './upload-file.component.html',
  styleUrls: ['./upload-file.component.css']
})
export class UploadFileComponent extends FileAttachmentCore {
  constructor(private service: PdfTranslationService) {
    super();
  }
  public async clickDownloadFile() {
    if (!this.file) return;
    const form = new FormData();
    form.append('file_upload', this.file, this.file.name);
    this.service.uploadFile(form)
  }
}
