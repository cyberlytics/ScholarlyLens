import { Author } from "./Author";

export interface Institut{
    name: string;
    domain: string[];
    webpage: string[];
    country: string;
    country_code: string;
    author: Author[];
}