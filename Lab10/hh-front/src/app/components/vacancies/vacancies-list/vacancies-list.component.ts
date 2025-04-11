import { Component, OnInit } from '@angular/core';
import { Vacancy } from '../../../core/models/vacancy.model';
import { VacancyService } from '../../../core/services/vacancy.service';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-vacancies-list',
  standalone: true,
  imports: [CommonModule,RouterModule],
  templateUrl: './vacancies-list.component.html',
  styleUrls: ['./vacancies-list.component.css']
})
export class VacanciesListComponent implements OnInit {
  vacancies: Vacancy[] = [];
  loading = true;
  error: string | null = null;

  constructor(private vacancyService: VacancyService) { }

  ngOnInit(): void {
    this.loadVacancies();
  }

  loadVacancies(): void {
    this.loading = true;
    this.vacancyService.getVacancies().subscribe({
      next: (data) => {
        this.vacancies = data;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Failed to load vacancies. Please try again later.';
        this.loading = false;
        console.error('Error loading vacancies:', err);
      }
    });
  }
}