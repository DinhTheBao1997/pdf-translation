import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { of, Observable, firstValueFrom } from "rxjs";
import { catchError } from "rxjs/operators";
import { IResponse } from "../interface/IResponse";
import { CustomType } from "../type/dynamic-type";
import { from } from 'rxjs';
import { IApiService } from "../interface/IApiService";
import { ObjectUtils } from "../utility/ObjectUtils";
import { environment } from "environment/environment";

@Injectable({
  providedIn: "root",
})
export class ApiService implements IApiService {
  constructor(private httpClient: HttpClient) { }

  public get(pathname: string, query: CustomType<string> = null): Promise<IResponse> {
    const strQuery = this.createUrlQuery(query);
    const url = this.joinApiUrl(pathname, strQuery);
    const request = this.httpClient.get(url);
    return firstValueFrom(this.catchError(request));
  }

  public post(pathname: string, body: Object, query: CustomType<string> = null): Promise<IResponse> {
    const strQuery = this.createUrlQuery(query);
    const url = this.joinApiUrl(pathname, strQuery);
    const request = this.httpClient.post(url, body);
    return firstValueFrom(this.catchError(request));
  }

  public requestSubscribe(request: Promise<IResponse>): Observable<IResponse> {
    return from(request);
  }

  private catchError(request: Observable<IResponse>): Observable<IResponse> {
    return request.pipe(catchError(error => of({ errorCode: error?.error?.errorCode || '500' })));
  }

  private joinApiUrl(pathname: string, query: string) {
    let url = environment.api.APP_API + pathname;
    if (typeof query == 'string') url += query;
    return url;
  }

  private createUrlQuery(query: CustomType<string>): string {
    if (typeof query == "string") return query;
    if (typeof query != "object") return "";
    if (ObjectUtils.isEmpty(query)) return "";

    let arrQuery: string[] = [];
    for (const [key, value] of Object.entries<string>(query)) {
      let encode = "";
      if (!ObjectUtils.isEmpty(value)) {
        encode = encodeURIComponent(value);
      }
      arrQuery.push([key, encode].join("="));
    }

    return "?" + arrQuery.join("&");
  }
}
