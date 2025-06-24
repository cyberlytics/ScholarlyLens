import { Institut } from "./Institut";
import { Publication } from "./Publication";

export interface Author {
  google_scholar_id: string;
  name: string;
  institut: Institut;
  interests: string[];
  email: string;
  citations?: number;
  h_index?: number;
  i10_index?: number;
  h_index5y?: number;
  i10_index5y?: number;
  citation5y?: number;
  publications?: Publication[];
  cites_per_year: Record<string, number>;
}
