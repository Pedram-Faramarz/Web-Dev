import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Products } from '../models/products.model';
import { PRODUCTS } from '../data/products-data';


@Component({
  selector: 'app-products',
  standalone: true,
  imports: [CommonModule],
  //templateUrl: './products.component.html',
  template: `
  <div class="product-list">
  <div *ngFor="let product of products" class="product-card">
    <div class="image-gallery">
      <img 
        [src]="selectedImages[product.id] || product.imageUrls[0]" 
        alt="{{ product.name }}" 
        class="main-image"
      >
      <div class="thumbnail-gallery">
        <img 
          *ngFor="let image of product.imageUrls.slice(0, 3)" 
          [src]="image"
          alt="Thumbnail" 
          class="thumbnail" 
          (click)="changeMainImage(product, image)"
        >
      </div>
    </div>
    
    <h2>{{ product.name }}</h2>
    <p>{{ product.description }}</p>
    <p>⭐ {{ product.rating }}</p>
    
    <div class="button-row">
      <button (click)="share(product, 'whatsapp')">WhatsApp</button>
      <button (click)="share(product, 'telegram')">Telegram</button>
    </div>
  </div>
</div>

  `,
  styleUrl: './products.component.css'
})
export class ProductsComponent {
  public products: Products[] = PRODUCTS;
    

  public selectedImages: { [key: number]: string } = {};

  changeMainImage(product: Products, imageUrl: string): void {
    this.selectedImages[product.id] = imageUrl;
  }

  share(product: Products, platform: string): void {
    const url = `${platform}://send?text=Check out this product: ${product.link}`;
    window.open(url, '_blank');
  }
}
