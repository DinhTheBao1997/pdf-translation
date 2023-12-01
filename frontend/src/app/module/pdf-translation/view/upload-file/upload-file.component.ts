import { Component, AfterViewInit, ViewContainerRef, ComponentRef } from '@angular/core';
import { FileAttachmentCore } from '@app/shared/core/FileAttachmentCore';
import { PdfTranslationService } from '../../service/pdf-translation.service';
import { LoadingService } from '@app/shared/service/loading.service';
import { ApiProcess } from '@app/shared/decorator/decorator';
import { SelectOption } from '@app/shared/type/SelectOption';
import { BackdropComponent } from '@app/shared/ui/backdrop/backdrop.component';

@Component({
  selector: 'app-upload-file',
  templateUrl: './upload-file.component.html',
  styleUrls: ['./upload-file.component.css']
})
export class UploadFileComponent extends FileAttachmentCore implements AfterViewInit {
  public readonly LanguageFromOptions: SelectOption[] = [
    {
      value: 'en',
      display: 'English'
    },
    {
      value: 'vi',
      display: 'Vietnamese'
    }
  ];
  public readonly LanguageToOptions: SelectOption[] = [
    {
      value: 'vi',
      display: 'Vietnamese'
    },
    {
      value: 'en',
      display: 'English'
    },
  ]
  constructor(private service: PdfTranslationService, private loadingService: LoadingService, private view: ViewContainerRef) {
    super();
  }

  addEventListener() {
    const queryEl = (query: string): HTMLElement => {
      return this.view.element.nativeElement.querySelector(query);
    }
    const dragDropEl = queryEl("#upload-document-form");
    dragDropEl.addEventListener("dragover", (event) => this.dragOver(event));
    dragDropEl.addEventListener("drop", (event) => this.dropHandler(event));

    const buttonEl = queryEl("#submit");
    buttonEl.addEventListener("click", () => this.clickUploadFile());

    const selectEl = queryEl("#upload-file");
    selectEl.addEventListener("click", () => this.onClickSelectFile());
  }

  @ApiProcess()
  public async clickUploadFile() {
    // const backdropComponent: ComponentRef<BackdropComponent> = this.view.createComponent(BackdropComponent);
    // const html: HTMLElement = backdropComponent.location.nativeElement;
    // document.body.appendChild(html)
    // setTimeout(()=> {
    //   backdropComponent.destroy()
    // }, 2000)
    if (!this.file) return;
    const form = new FormData();
    form.append('file', this.file, this.file.name);
    form.append('fileName', this.file.name);
    await this.service.uploadFile(form)
  }
}
