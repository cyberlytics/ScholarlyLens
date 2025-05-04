import InterestTag from "../components/InterestTag"
import ProfilePicture from "../components/ProfilePicture"
import Analytics from "../components/Analytics"
import Publication from "../components/Publication"
import Typography from '@mui/material/Typography';
import { Link } from "react-router-dom";
import { useParams } from 'react-router-dom';
import { Author } from '../apiModels/AuthorsInterface';


const ScholarDetailPage = ({ authors }: { authors: Author[] }) => {

  const { scholarId } = useParams();
  const author = authors.find(a => a.name === decodeURIComponent(scholarId || ''));
  console.log(author);

    const universityLogo = 'src/assets/OTH-AW_Logo_Mini.png';
  return (
    <div
  style={{
    display: 'flex',            
    padding: '2rem',
    maxWidth: '1200px',
  }}
>
  <div style={{ display: 'flex', gap: '2rem', alignItems: 'flex-start', width: '100%' }}>
    <ProfilePicture />
    <div>
      <Typography variant="h1" sx={{ fontSize: '2rem', mb: 1 }}>
        {author?.name}
      </Typography>
      <div style={{display: 'flex', gap: '1rem'}}>
        <img src={universityLogo} alt="University Logo" style={{height: '24px' }} />
        <Link to="https://www.oth-aw.de" target="_blank" rel="noopener noreferrer">Ostbayerische Technische Hochschule Amberg-Weiden</Link>
      </div>
      <InterestTag />
      <Typography variant="h2" sx={{ fontSize: '2rem', mb: 1 }}>
        Analytics
      </Typography>
      <Analytics citations={author?.citations}
  hIndex={author?.h_index}
  i10Index={author?.i10_index}
  cites_per_year={author?.cites_per_year}/>
      <Typography variant="h2" sx={{ fontSize: '2rem', mb: 1 }}>
        Publications
      </Typography>
      <Publication />
    </div>
  </div>
</div>

  )
}

export default ScholarDetailPage