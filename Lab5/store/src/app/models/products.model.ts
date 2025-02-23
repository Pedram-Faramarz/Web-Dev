export interface Category {
    id: number;
    name: string;
  }
export interface Product {
    id: number;
    name: string;
    description: string;
    rating: number;
    imageUrls: string[];
    link: string;
    categoryId: number;
    likes: number;
  }
  