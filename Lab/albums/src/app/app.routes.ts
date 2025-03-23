import { Routes } from '@angular/router';
import { HomeComponent } from './main-components/home/home.component';
import { AlbumsComponent } from './main-components/albums/albums.component';
import { DetailsComponent } from './main-components/details/details.component';
import { PhotosComponent } from './main-components/photos/photos.component';
import { AboutComponent } from './main-components/about/about.component';

export const routes: Routes = [
    {
        path: '',
        redirectTo: 'home',
        pathMatch: 'full',
    },
    {
        path: 'home',
        component: HomeComponent,
        title : 'Home Page',
    },
    {
        path: 'albums',
        component: AlbumsComponent,
        title : 'Albums',
    },{
        path: 'albums/:id',
        component: DetailsComponent,
        title: 'Details of Album',
      },
      {
        path: 'albums/:id/photos',
        component: PhotosComponent,
        title: 'Photos of Album',
      },
      {
        path: 'about',
        component: AboutComponent,
        title: 'About Page',
      },
];
