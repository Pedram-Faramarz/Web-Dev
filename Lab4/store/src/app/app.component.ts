import { Component } from '@angular/core';
import { ProductsComponent } from "./products/products.component";
import { TestComponent } from './test/test.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ProductsComponent, TestComponent],
  //templateUrl: './app.component.html',
  template:`<app-products></app-products>
            <div><app-test></app-test></div>`,
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'store';
}
