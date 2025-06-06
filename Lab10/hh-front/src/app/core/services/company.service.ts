import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Company } from '../models/company.model';
import { Vacancy } from '../models/vacancy.model';


@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  private apiUrl = "http://127.0.0.1:8000/api";

  constructor(private http: HttpClient) { }

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.apiUrl}/companies/`);
  }

  getCompanyById(id: number): Observable<Company> {
    return this.http.get<Company>(`${this.apiUrl}/companies/${id}/`);
  }

  getCompanyVacancies(id: number): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.apiUrl}/companies/${id}/vacancies/`);
  }
}
