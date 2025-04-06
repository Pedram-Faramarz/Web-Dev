import { Component } from '@angular/core';
import { RouterOutlet, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterModule, RouterOutlet], // ✅ Corrected imports
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'], // ✅ Corrected "styleUrl" to "styleUrls"

})
export class AppComponent {
  title = 'Album';
}
