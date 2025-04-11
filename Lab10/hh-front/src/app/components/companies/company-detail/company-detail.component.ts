import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Company } from '../../../core/models/company.model';
import { CompanyService } from '../../../core/services/company.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-company-detail',
  standalone:true,
  imports:[CommonModule],
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {
  company: Company | null = null;
  loading = true;
  error: string | null = null;

  constructor(
    private companyService: CompanyService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.loadCompany();
  }

  loadCompany(): void {
    this.loading = true;
    const id = Number(this.route.snapshot.paramMap.get('id'));
    
    if (isNaN(id)) {
      this.error = 'Invalid company ID';
      this.loading = false;
      return;
    }
    
    this.companyService.getCompanyById(id).subscribe({
      next: (data) => {
        this.company = data;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Failed to load company details. Please try again later.';
        this.loading = false;
        console.error('Error loading company:', err);
      }
    });
  }

  goBack(): void {
    this.router.navigate(['/companies']);
  }

  viewVacancies(): void {
    if (this.company) {
      this.router.navigate(['/companies', this.company.id, 'vacancies']);
    }
  }
}