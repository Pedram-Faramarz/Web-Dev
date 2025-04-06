import { Component, inject } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { PhotoElement } from '../../model/interface';
import { signal } from '@angular/core';
import { ServicesService } from '../../services/services.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-photos',
  standalone:true,
  imports: [CommonModule],
  templateUrl: './photos.component.html',
  styleUrl: './photos.component.css'
})
export class PhotosComponent {
  private route = inject(ActivatedRoute);
  private router = inject(Router);
  private albumPhotosService = inject(ServicesService);

  albumId = Number(this.route.snapshot.paramMap.get('id'));
  photos = signal<PhotoElement[]>([]);

  constructor() {
    this.fetchPhotos();
  }

  fetchPhotos() {
    this.albumPhotosService.getPhotos(this.albumId).subscribe((data) => {
      this.photos.set(data);
    });
  }

  goBack() {
    this.router.navigate(['/albums', this.albumId]);
  }
}
