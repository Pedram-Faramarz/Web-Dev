import { Component, inject, signal } from '@angular/core';
import { ServicesService } from '../../services/services.service';
import { Router } from '@angular/router';
import { AlbumInterface } from '../../model/interface';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './albums.component.html',
  styleUrl: './albums.component.css'
})
export class AlbumsComponent {
  private albumservices = inject(ServicesService);
  private router = inject(Router);

  albums = signal<AlbumInterface[]>([]);

  constructor(){
    this.fetchAlbums();
  }

  
  fetchAlbums():void {
    this.albumservices.getAlbums().subscribe((data) => this.albums.set(data));
  }

  deleteAlbum(id: number): void {
    this.albums.set(this.albums().filter((album) => album.id !== id));
  }

  openAlbumDetails(id:number) : void {
    this.router.navigate(['/albums', id]);
  }
}
