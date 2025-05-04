import React from 'react';
import { Route } from 'react-router-dom'
import { Routes } from 'react-router-dom'
import ResponsiveAppBar from './components/ResponsiveAppBar'
import HomePage from './pages/HomePage'
import InstitutesPage from './pages/InstitutesPage'
import ScholarsPage from './pages/ScholarsPage'
import ScholarDetailPage from './pages/ScholarDetailPage'
import InstitutDetailPage from './pages/InstitutDetailPage'
import { Box } from '@mui/material'
import { useFetch } from './hooks/useFetch';
import { Author } from './apiModels/AuthorsInterface';

function App() {

const { data, loading, error } = useFetch<{ authors: Author[]}>('getAuthors');

console.log(data)
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
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/scholars" element={<ScholarsPage authors={data?.authors ?? []}/>} />
            <Route path="/institutes" element={<InstitutesPage />} />
            <Route path="/scholars/:scholarId" element={<ScholarDetailPage authors={data?.authors ?? []}/>} />
            <Route path="/institutes/:instituteId" element={<InstitutDetailPage />} />
          </Routes>
        </Box>
      </Box>
    </>
  )
}

export default App
