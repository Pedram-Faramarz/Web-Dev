import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Vacancy } from '../models/vacancy.model';
import { environment } from '../../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  private apiUrl = "http://127.0.0.1:8000/api";

  constructor(private http: HttpClient) { }

  getVacancies(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.apiUrl}/vacancies/`);
  }

  getVacancyById(id: number): Observable<Vacancy> {
    return this.http.get<Vacancy>(`${this.apiUrl}/vacancies/${id}/`);
  }

  getTopVacancies(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.apiUrl}/vacancies/top_ten/`);
  }
}
