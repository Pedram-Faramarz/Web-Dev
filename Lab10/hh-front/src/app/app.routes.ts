import { RouterModule, Routes } from '@angular/router';
import { CompaniesListComponent } from './components/companies/companies-list/companies-list.component';
import { CompanyDetailComponent } from './components/companies/company-detail/company-detail.component';
import { CompanyVacanciesComponent } from './components/companies/company-vacancies/company-vacancies.component';
import { VacanciesListComponent } from './components/vacancies/vacancies-list/vacancies-list.component';
import { VacancyDetailComponent } from './components/vacancies/vacancy-detail/vacancy-detail.component';
import { TopVacanciesComponent } from './components/vacancies/top-vacancies/top-vacancies.component';
import { NgModule } from '@angular/core';

export const routes: Routes = [
    { path: '', redirectTo: '/companies', pathMatch: 'full' },
    { path: 'companies', component: CompaniesListComponent },
    { path: 'companies/:id', component: CompanyDetailComponent },
    { path: 'companies/:id/vacancies', component: CompanyVacanciesComponent },
    { path: 'vacancies', component: VacanciesListComponent },
    { path: 'vacancies/top_ten', component: TopVacanciesComponent},
    { path: 'vacancies/:id', component: VacancyDetailComponent },
    
    // { path: '**', redirectTo: '/companies' }
  ];

  @NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
  })
  export class AppRoutingModule { }
