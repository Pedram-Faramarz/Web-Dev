import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { Vacancy } from '../../../core/models/vacancy.model';
import { Company } from '../../../core/models/company.model';
import { VacancyService } from '../../../core/services/vacancy.service';
import { CompanyService } from '../../../core/services/company.service';
import { combineLatest } from 'rxjs';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-vacancy-detail',
  standalone:true,
  imports:[CommonModule, RouterModule],
  templateUrl: './vacancy-detail.component.html',
  styleUrls: ['./vacancy-detail.component.css']
})
export class VacancyDetailComponent implements OnInit {
  vacancy: Vacancy | null = null;
  company: Company | null = null;
  loading = true;
  error: string | null = null;

  constructor(
    private vacancyService: VacancyService,
    private companyService: CompanyService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.loadVacancy();
  }

  loadVacancy(): void {
    this.loading = true;
    const id = Number(this.route.snapshot.paramMap.get('id'));
    
    if (isNaN(id)) {
      this.error = 'Invalid vacancy ID';
      this.loading = false;
      return;
    }
    
    this.vacancyService.getVacancyById(id).subscribe({
      next: (data) => {
        this.vacancy = data;
        
        // If company is just an ID, fetch the company details
        if (typeof this.vacancy.company === 'number') {
          this.companyService.getCompanyById(this.vacancy.company).subscribe({
            next: (companyData) => {
              this.company = companyData;
              this.loading = false;
            },
            error: (err) => {
              this.error = 'Failed to load company details. Please try again later.';
              this.loading = false;
              console.error('Error loading company:', err);
            }
          });
        } else {
          // If company object is already included
          this.company = this.vacancy.company as Company;
          this.loading = false;
        }
      },
      error: (err) => {
        this.error = 'Failed to load vacancy details. Please try again later.';
        this.loading = false;
        console.error('Error loading vacancy:', err);
      }
    });
  }

  goBack(): void {
    this.router.navigate(['/vacancies']);
  }
  
  viewCompany(): void {
    if (this.company) {
      this.router.navigate(['/companies', this.company.id]);
    }
  }
}