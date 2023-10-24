import { Component } from '@angular/core';
import { FileAttachmentCore } from '@app/shared/core/FileAttachmentCore';
import { PdfTranslationService } from '../../service/pdf-translation.service';
import { LoadingService } from '@app/shared/service/loading.service';
import { ApiProcess } from '@app/shared/decorator/decorator';

@Component({
  selector: 'app-upload-file',
  templateUrl: './upload-file.component.html',
  styleUrls: ['./upload-file.component.css']
})
export class UploadFileComponent extends FileAttachmentCore {
  constructor(private service: PdfTranslationService, private loadingService: LoadingService) {
    super();
  }

  @ApiProcess()
  public async clickDownloadFile() {
    if (!this.file) return;
    const form = new FormData();
    form.append('file', this.file, this.file.name);
    form.append('fileName', this.file.name);
    await this.service.uploadFile(form)
  }
}
