import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { PRODUCTS } from '../data/products';
import { Product } from '../models/products.model';
import { ProductItemComponent } from '../product-item/product-item.component';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [CommonModule, ProductItemComponent],
  template: `
    <div *ngIf="products.length > 0">
      <h2>Products</h2>
      <div class="product-container">
        <app-product-item *ngFor="let product of products" [product]="product" (onRemove)="removeProduct($event)"></app-product-item>
      </div>
    </div>
    <p *ngIf="products.length === 0">No products found.</p>
  `,
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  products: Product[] = [];

  constructor(private route: ActivatedRoute) {
    this.route.params.subscribe(params => {
      const categoryId = Number(params['id']);
      this.products = PRODUCTS.filter(p => p.categoryId === categoryId);
    });
  }

  removeProduct(productId: number) {
    this.products = this.products.filter(p => p.id !== productId);
  }
}
