import { Route } from 'react-router-dom'
import { Routes } from 'react-router-dom'
import ResponsiveAppBar from './components/ResponsiveAppBar'
import HomePage from './pages/HomePage'
import InstitutesPage from './pages/InstitutesPage'
import ScholarsPage from './pages/ScholarsPage'
import ScholarDetailPage from './pages/ScholarDetailPage'
import InstitutDetailPage from './pages/InstitutDetailPage'
import { Box } from '@mui/material'

function App() {
  return (
    <>
      <ResponsiveAppBar />
      <Box 
        component="main" 
        sx={{ 
          display: 'flex',
          justifyContent: 'center',
          p: { xs: '1rem', sm: '6rem' }
        }}
      >
        <Box>
          <InstitutDetailPage/>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/scholars" element={<ScholarsPage />} />
            <Route path="/institutes" element={<InstitutesPage />} />
            <Route path="/scholars/:scholarId" element={<ScholarDetailPage />} />
            <Route path="/institutes/:instituteId" element={<InstitutDetailPage />} />
          </Routes>
        </Box>
      </Box>
    </>
  )
}

export default App
