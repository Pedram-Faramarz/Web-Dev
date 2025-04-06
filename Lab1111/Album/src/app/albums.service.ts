import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Album } from './album.model';
import { provideHttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class AlbumsService {



  private apiUrl = 'https://jsonplaceholder.typicode.com/albums/1/photos';

  private ablumSubject = new BehaviorSubject<Album[]>([]);
  albums = this.ablumSubject.asObservable(); // observable to share album data

  constructor(private http: HttpClient) {}

  fetchAlbums():void {
    this.http.get<Album[]>(this.apiUrl).subscribe((data)=> {
      this.ablumSubject.next(data);
    }) // store the feched albums
    ;
  }
}
