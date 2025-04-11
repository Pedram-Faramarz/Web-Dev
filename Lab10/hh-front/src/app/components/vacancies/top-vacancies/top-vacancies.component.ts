import { Component, OnInit } from '@angular/core';
import { Vacancy } from '../../../core/models/vacancy.model';
import { VacancyService } from '../../../core/services/vacancy.service';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-top-vacancies',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './top-vacancies.component.html',
  styleUrls: ['./top-vacancies.component.css'],
})
export class TopVacanciesComponent implements OnInit {
  vacancies: Vacancy[] = [];
  loading = true;
  error: string | null = null;

  constructor(private vacancyService: VacancyService) { }

  ngOnInit(): void {
    this.loadTopVacancies();
  }

  loadTopVacancies(): void {
    this.loading = true;
    this.vacancyService.getTopVacancies().subscribe({
      next: (data) => {
        this.vacancies = data;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Failed to load top vacancies. Please try again later.';
        this.loading = false;
        console.error('Error loading top vacancies:', err);
      }
    });
  }
}
