import{ Component, OnInit } from '@angular/core';
import { AlbumsService } from '../albums.service';
import { Inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';


@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule,HttpClientModule,RouterModule],
  // templateUrl: './home.component.html',
  template:`
  <h2>Albums</h2>
  <ul>
    <li *ngFor="let album of albums">
      {{ album.title }}
    </li>
  </ul>
  `,
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit { 
  
  constructor(private albumsService: AlbumsService) {}
  albums: {albumId: number; id: number; title: string; url: string; thumbnailUrl: string}[] = [];
  ngOnInit() {
    this.albumsService.getAlbums().subscribe((data: any[])=>{
      console.log(data);
      this.albums = data;
    })
  }


  

}

