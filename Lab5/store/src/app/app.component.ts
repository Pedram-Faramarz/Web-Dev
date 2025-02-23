import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { CATEGORIES } from './data/categories';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterModule],
  template: `
    <header>
    <h1>Online Store</h1>
    <nav>
      <a *ngFor="let category of categories" [routerLink]="['/products', category.id]">
        {{ category.name }}
      </a>
    </nav>
  </header>
    <router-outlet></router-outlet>
  `,
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  categories = CATEGORIES;
}
