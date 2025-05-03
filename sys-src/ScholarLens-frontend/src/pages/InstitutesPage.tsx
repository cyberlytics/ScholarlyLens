import { Typography } from "@mui/material"
import InstitutesRankCard from "../components/InstitutesRankCard"

const InstitutesPage = () => {
  return (
    <>
    <Typography sx={{ fontWeight: 600, fontSize: '1.25rem' }}>Institutes</Typography>
    <InstitutesRankCard/>
    </>
  )
}

export default InstitutesPage