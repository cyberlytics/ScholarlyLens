import { Author } from "./Author";

export interface Publication{
    author: Author;
    content: string;
    year?: number;
    citation?: string;
    gs_id?: string;
    citation_count?: string;
    cited_by_url?: string;
    cites_id: string[];
}