import {BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip} from 'recharts';
import { useTheme } from '@mui/material/styles';

const CitationChart = () => {
  const theme = useTheme();

  const cites_per_year = {
    2003: 13, 2004: 41, 2005: 64, 2006: 138, 2007: 107,
    2008: 127, 2009: 212, 2010: 226, 2011: 212, 2012: 170,
    2013: 103, 2014: 118, 2015: 87, 2016: 81, 2017: 54,
    2018: 42, 2019: 32, 2020: 38, 2021: 23, 2022: 16,
    2023: 21, 2024: 18, 2025: 1
  };

  const data = Object.entries(cites_per_year).map(([year, count]) => ({
    year,
    count
  }));

  return (
    <BarChart width={500} height={150} data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="year" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="count" fill={theme.palette.primary.main} />
    </BarChart>
  );
}

export default CitationChart