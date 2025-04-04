import { Route } from 'react-router-dom'
import { Routes } from 'react-router-dom'
import ResponsiveAppBar from './components/ResponsiveAppBar'
import HomePage from './pages/HomePage'
import InstitutesPage from './pages/InstitutesPage'
import ScholarsPage from './pages/ScholarsPage'
import ScholarDetailPage from './pages/ScholarDetailPage'
import InstitutDetailPage from './pages/InstitutDetailPage'
function App() {

  return (
    <>
      <ResponsiveAppBar />
      <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/scholars" element={<ScholarsPage />} />
      <Route path="/institutes" element={<InstitutesPage />} />
      <Route path="/scholars/:scholarId" element={<ScholarDetailPage />} />
      <Route path="/institutes/:instituteId" element={<InstitutDetailPage />} />
    </Routes>
    </>
  )
}

export default App
