import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { Company } from '../../../core/models/company.model';
import { Vacancy } from '../../../core/models/vacancy.model';
import { CompanyService } from '../../../core/services/company.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-company-vacancies',
  standalone: true,
  imports : [CommonModule,RouterModule],
  templateUrl: './company-vacancies.component.html',
  styleUrls: ['./company-vacancies.component.css']
})
export class CompanyVacanciesComponent implements OnInit {
  company: Company | null = null;
  vacancies: Vacancy[] = [];
  loading = true;
  error: string | null = null;

  constructor(
    private companyService: CompanyService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.loadCompanyAndVacancies();
  }

  loadCompanyAndVacancies(): void {
    this.loading = true;
    const id = Number(this.route.snapshot.paramMap.get('id'));
    
    if (isNaN(id)) {
      this.error = 'Invalid company ID';
      this.loading = false;
      return;
    }
    
    this.companyService.getCompanyById(id).subscribe({
      next: (companyData) => {
        this.company = companyData;
        
        this.companyService.getCompanyVacancies(id).subscribe({
          next: (vacanciesData) => {
            this.vacancies = vacanciesData;
            this.loading = false;
          },
          error: (err) => {
            this.error = 'Failed to load company vacancies. Please try again later.';
            this.loading = false;
            console.error('Error loading vacancies:', err);
          }
        });
      },
      error: (err) => {
        this.error = 'Failed to load company details. Please try again later.';
        this.loading = false;
        console.error('Error loading company:', err);
      }
    });
  }

  goToCompanyDetails(): void {
    if (this.company) {
      this.router.navigate(['/companies', this.company.id]);
    }
  }

  goToAllCompanies(): void {
    this.router.navigate(['/companies']);
  }
}