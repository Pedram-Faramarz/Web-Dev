import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable()
export class ApiInterceptor implements HttpInterceptor {

  constructor() {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    const apiRequest = request.clone({
      headers: request.headers.set('Content-Type', 'application/json')
    });
    
    return next.handle(apiRequest).pipe(
      catchError((error: HttpErrorResponse) => {
        console.error('API Error:', error);
        return throwError(() => error);
      })
    );
    }
  }