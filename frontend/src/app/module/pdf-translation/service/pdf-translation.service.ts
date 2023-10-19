import { Injectable } from '@angular/core';
import { ApiService } from '@app/shared/service/api.service';
import { HttpClient, HttpHeaders } from "@angular/common/http";

@Injectable({ providedIn: 'root' })
export class PdfTranslationService {
  constructor(private apiService: ApiService, private httpClient: HttpClient) { }

  public uploadFile(form: FormData) {
    const headers = new HttpHeaders();
    headers.append('Content-Type', 'multipart/form-data');
    return this.httpClient.post("http://localhost:8000/pdf-translation/upload-file", form, {headers}).toPromise();
  }
}
