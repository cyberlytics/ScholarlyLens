import { Box } from "@mui/material"

import CitationChart from "./CitationChart"

interface AnalyticsProps {
  citations?: number;
  hIndex?: number;
  i10Index?: number;
  cites_per_year?: {};
}

const Analytics: React.FC<AnalyticsProps> = ({ citations, hIndex, i10Index, cites_per_year }) => {
  return (
    <Box sx={{ 
      display: 'flex', 
      gap: '2rem',
      borderRadius: '15px',
      boxShadow: '8px 8px 30px rgba(0,0,0,0.1)',
      padding: '1.5rem'
    }}>
      <div>
        <CitationChart cites_per_year={cites_per_year}/>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
        <div>Zitate: {citations ?? '—'}</div>
        <div>last5y: 530</div>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
        <div>H-Index: {hIndex ?? '—'}</div>
        <div>last5y: 530</div>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
        <div>I10-Index: {i10Index ?? '—'}</div>
        <div>last5y: 530</div>
      </div>
    </Box>
  )
}

export default Analytics