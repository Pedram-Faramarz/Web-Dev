import { Component, inject,signal ,WritableSignal,} from '@angular/core';
import { AlbumInterface } from '../../model/interface';
import { ServicesService } from '../../services/services.service';
import { Router,RouterLink, ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-details',
  standalone: true,
  imports: [RouterLink,CommonModule],
  templateUrl: './details.component.html',
  styleUrl: './details.component.css'
})
export class DetailsComponent {
  private route = inject(ActivatedRoute);
  private router = inject(Router);
  private albumService = inject(ServicesService);

  album: WritableSignal<AlbumInterface | null> = signal(null);
  editedTitle = signal('');

  constructor() {
    const albumId = Number(this.route.snapshot.params['id']);
    this.fetchAlbum(albumId);
  }

  fetchAlbum(id: number) {
    this.albumService.getAlbum(id).subscribe((album) => {
      this.album.set(album);
      this.editedTitle.set(album.title);
    });
  }

  saveChanges() {
    if (!this.album()) return;

    const updatedAlbum: AlbumInterface = {
      id: this.album()!.id,
      userId: this.album()!.userId,
      title: this.editedTitle(),
    };

    this.albumService.updateAlbum(updatedAlbum).subscribe({
      next: (response) => {
        this.album.set(response);
        console.log('Album updated:', response);
      },
      error: (err) => console.error('Error updating album:', err),
    });
  }

  onTitleChange(event: Event) {
    const input = event.target as HTMLInputElement;
    this.editedTitle.set(input.value);
  }

  goBack() {
    this.router.navigate(['/albums']);
  }

  
}
