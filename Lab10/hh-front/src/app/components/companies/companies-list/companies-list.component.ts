import { Component, OnInit } from '@angular/core';
import { Company } from '../../../core/models/company.model';
import { CompanyService } from '../../../core/services/company.service';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-companies-list',
  standalone: true,
  templateUrl: './companies-list.component.html',
  styleUrl: './companies-list.component.css',
  imports: [RouterModule,CommonModule]
})
export class CompaniesListComponent implements OnInit{
  companies : Company[] = [];
  loading = true;
  error: string | null = null;

  constructor(private companyService : CompanyService){}

  ngOnInit(): void {
      this.loadCompanies();
  }

  loadCompanies():void {
    this.loading = true;
    this.companyService.getCompanies().subscribe({
      next:(data)=> {
        this.companies = data;
        this.loading = false;
      },
      error:(err)=> {
        this.error= 'Failed to load companies. Please try again later';
        this.loading = false;
        console.error('Error loading companies: ', err);
      }
    });

  }

}
