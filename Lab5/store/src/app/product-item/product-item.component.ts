import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../models/products.model';

@Component({
  selector: 'app-product-item',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="product-list">
    <div class="product-card">
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
        <div class="rating-like-box">
          <p>⭐ {{ product.rating }}</p>
          <p>❤️ {{ product.likes }}</p>
        </div>
        <div class="button-row">
            <button (click)="likeProduct()" >{{ like ? 'Unlike' : 'Like' }}</button>
            <button (click)="removeProduct()">Remove</button>
            <button (click)="share(product, 'whatsapp')">WhatsApp</button>
        </div>
    </div>
</div>

  `,
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {
  @Input() product!: Product;
  @Output() onRemove = new EventEmitter<number>();
  like: boolean = false; 

  likeProduct() {
    this.like = !this.like; 
    this.product.likes += this.like ? 1 : -1; 
  }
  
 
  removeProduct() {
    this.onRemove.emit(this.product.id);
  }

  public selectedImages: { [key: number]: string } = {};

  changeMainImage(product: Product, imageUrl: string): void {
    this.selectedImages[product.id] = imageUrl;
  }

  share(product: Product, platform: string): void {
    const url = `${platform}://send?text=Check out this product: ${product.link}`;
    window.open(url, '_blank');
  }
}
