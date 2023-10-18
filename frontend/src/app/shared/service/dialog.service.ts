import { ApplicationRef, ViewContainerRef, EmbeddedViewRef, Injectable, Injector, Type } from '@angular/core';
import { DialogCore } from '../core/DialogCore';
import { IDialogService } from '../interface/IDialogService';

/**
 * Reference: https://medium.com/hackernoon/angular-pro-tip-how-to-dynamically-create-components-in-body-ba200cc289e6
 */
@Injectable()
export class DialogService implements IDialogService {
  constructor(
    private viewContainerRef: ViewContainerRef,
    private appRef: ApplicationRef,
    private injector: Injector
  ) { }

  public appendDialogToBody<T extends DialogCore>(componentType: Type<T>): T {
    const componentRef = this.viewContainerRef.createComponent(componentType, { injector: this.injector });

    this.appRef.attachView(componentRef.hostView);

    const domElem = (componentRef.hostView as EmbeddedViewRef<HTMLElement>).rootNodes[0];
    document.body.appendChild(domElem);

    const component = componentRef.instance;
    component.closed$.subscribe(v => {
      if (v) {
        this.appRef.detachView(componentRef.hostView);
        componentRef.destroy();
      }
    });
    return component;
  }
}
