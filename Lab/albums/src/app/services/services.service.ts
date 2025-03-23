import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AlbumInterface } from '../model/interface';
import { PhotoElement } from '../model/interface';
@Injectable({
  providedIn: 'root'
})
export class ServicesService {
  private http  = inject(HttpClient);
  private apiUrl = 'https://jsonplaceholder.typicode.com/albums';

  constructor() { }

  getAlbums(): Observable<AlbumInterface[]> {
    return this.http.get<AlbumInterface[]>(this.apiUrl);
  }

  getAlbum(id: number): Observable<AlbumInterface> {
    return this.http.get<AlbumInterface>(`${this.apiUrl}/${id}`);
  }

  updateAlbum(updatedAlbum: AlbumInterface): Observable<AlbumInterface> {
    return this.http.put<AlbumInterface>(
      `${this.apiUrl}/${updatedAlbum.id}`,
      updatedAlbum
    );
  }
  getPhotos(albumId: number): Observable<PhotoElement[]> {
    return this.http.get<PhotoElement[]>(`${this.apiUrl}/${albumId}/photos`);
  }
}
