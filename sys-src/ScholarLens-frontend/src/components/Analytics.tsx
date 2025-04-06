import { Box } from "@mui/material"

import CitationChart from "./CitationChart"

const Analytics = () => {
  return (
    <Box sx={{ 
      display: 'flex', 
      gap: '2rem',
      borderRadius: '15px',
      boxShadow: '8px 8px 30px rgba(0,0,0,0.1)',
      padding: '1.5rem'
    }}>
      <div>
        <CitationChart/>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
        <div>Zitate: 531</div>
        <div>last5y: 530</div>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
        <div>H-Index: 12</div>
        <div>last5y: 530</div>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
        <div>I10-Index: 34</div>
        <div>last5y: 530</div>
      </div>
    </Box>
  )
}

export default Analytics