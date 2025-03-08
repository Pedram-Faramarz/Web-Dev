import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class AlbumsService {

  // getEmptyAlbum(): Observable<{ title: string; artist: string; year: string; coverUrl: string }>{
  //   return of({
  //     title: '332',
  //     artist: 'Name',
  //     year: '2003',
  //     coverUrl: '3432'
  //   });
  // }

  private apiUrl = 'https://jsonplaceholder.typicode.com/albums/1/photos';

  constructor(private http: HttpClient) {}

  getAlbums(): Observable<{albumId: number; id: number; title: string; url: string; thumbnailUrl: string}[]> {
    return this.http.get<{albumId: number; id: number; title: string; url: string; thumbnailUrl: string}[]>(this.apiUrl);
  }
}
