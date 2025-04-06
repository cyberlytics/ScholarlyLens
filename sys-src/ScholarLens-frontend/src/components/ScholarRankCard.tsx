import { Box, Typography, IconButton, Avatar } from '@mui/material';
import SchoolOutlinedIcon from '@mui/icons-material/SchoolOutlined';
import NavigateNextRoundedIcon from '@mui/icons-material/NavigateNextRounded';

const ScholarRankCard = () => {
  const scholarName = "Horst Karl Hahn";
  const scholarsAffiliation = "Institut director at OTH-AW";
  const rank = 1;

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
          {scholarName}
        </Typography>
        <Typography sx={{ fontSize: '1rem', color: 'text.secondary' }}>
          {scholarsAffiliation}
        </Typography>
        <Typography sx={{ fontSize: '0.95rem', color: 'gray' }}>
          Zitate: 531&nbsp;&nbsp;|&nbsp;&nbsp;H-Index: 531&nbsp;&nbsp;|&nbsp;&nbsp;i10-Index: 531
        </Typography>
      </Box>

      {/* Arrow Button */}
      <IconButton sx={{ padding: 0 }}>
        <NavigateNextRoundedIcon sx={{ fontSize: '2.5rem', color: 'black' }} />
      </IconButton>
    </Box>
  );
};

export default ScholarRankCard;
