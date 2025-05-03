export interface Author {
  name: string;
  affiliation?: string;
  interests: string[];
  citations?: number;
  h_index?: number;
  i10_index?: number;
  publications: Record<string, any>[];
  cites_per_year: Record<string, number>;
}
