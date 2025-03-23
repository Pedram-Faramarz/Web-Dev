import{ Component, OnInit } from '@angular/core';
import { AlbumsService } from '../albums.service';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { Album } from '../album.model';



@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule,RouterModule],
  templateUrl: './home.component.html',
  template:`
  
  `,
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit { 
  
  albums: Album[] = [];

  constructor(private albumsService: AlbumsService){}

  ngOnInit(): void {
      //fetch albums from API
      this.albumsService.fetchAlbums();

      //subscribe the albums$ to get latest data
      this.albumsService.albums.subscribe((data)=> {this.albums= data});
  }


  

}

