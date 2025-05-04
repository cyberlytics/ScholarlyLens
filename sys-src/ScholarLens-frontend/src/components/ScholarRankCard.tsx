import { Box, Typography, IconButton, Avatar } from '@mui/material';
import SchoolOutlinedIcon from '@mui/icons-material/SchoolOutlined';
import NavigateNextRoundedIcon from '@mui/icons-material/NavigateNextRounded';
import { Author } from '../apiModels/AuthorsInterface';
import { useNavigate } from 'react-router-dom';


interface ScholarRankCardProps {
  author: Author;
  rank: number;
}

const ScholarRankCard = ({ author, rank }: ScholarRankCardProps) => {
  const navigate = useNavigate();

  return (
    <Box
      sx={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        borderRadius: '16px',
        backgroundColor: '#e0e0e0',
        padding: '1.5rem 2rem',
        gap: 3,
        maxWidth: 800,
        width: '100%',
        boxShadow: '8px 8px 30px rgba(0,0,0,0.1)',
      }}
    >
      {/* Rank Number */}
      <Typography
        variant="h3"
        sx={{
          fontWeight: 'bold',
          color: 'teal',
          minWidth: '40px',
        }}
      >
        {rank}
      </Typography>

      <Avatar
        sx={{
          border: '2px solid teal',
          width: 60,
          height: 60,
          bgcolor: 'white',
        }}
      >
        <SchoolOutlinedIcon sx={{ color: 'teal', fontSize: '2rem' }} />
      </Avatar>

      {/* Main Content */}
      <Box sx={{ flexGrow: 1 }}>
        <Typography sx={{ fontWeight: 600, fontSize: '1.25rem' }}>
          {author.name}
        </Typography>
        <Typography sx={{ fontSize: '1rem', color: 'text.secondary' }}>
          {author.affiliation || '—'}
        </Typography>
        <Typography sx={{ fontSize: '0.95rem', color: 'gray' }}>
          Zitate: {author.citations ?? '—'}&nbsp;&nbsp;|&nbsp;&nbsp;H-Index: {author.h_index ?? '—'}&nbsp;&nbsp;|&nbsp;&nbsp;i10-Index: {author.i10_index ?? '—'}
        </Typography>
      </Box>

      // TODO change author.name to id tauschen or so
      <IconButton sx={{ padding: 0 }} onClick={() => navigate(`/scholars/${encodeURIComponent(author.name)}`)}>
        <NavigateNextRoundedIcon sx={{ fontSize: '2.5rem', color: 'black' }} />
      </IconButton>
    </Box>
  );
};

export default ScholarRankCard;
