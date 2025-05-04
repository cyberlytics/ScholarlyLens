import {BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip} from 'recharts';
import { useTheme } from '@mui/material/styles';

const CitationChart = ({ cites_per_year }: { cites_per_year?: Record<string, number> }) => {
  const theme = useTheme();

  console.log(cites_per_year)
  const data = Object.entries(cites_per_year ?? {}).map(([year, count]) => ({
    year,
    count
  }));

  return (
    <BarChart width={280} height={150} data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="year" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="count" fill={theme.palette.primary.main} />
    </BarChart>
  );
}

export default CitationChart