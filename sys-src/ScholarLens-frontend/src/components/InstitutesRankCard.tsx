import { Box, IconButton, Typography } from "@mui/material";
import NavigateNextRoundedIcon from '@mui/icons-material/NavigateNextRounded';

const InstitutesRankCard = () => {
    const institutesName = "Ostbayerische Technische Hochschule Amberg-Weiden";
    const institutesLogo = "src/assets/OTH-AW_Logo_Mini.png"
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
        <img style={{width:'100px'}} src={institutesLogo}/>
        
  

        <Box sx={{ flexGrow: 1 }}>
          <Typography sx={{ fontWeight: 600, fontSize: '1.25rem' }}>
            {institutesName}
          </Typography>
          <Typography sx={{ fontSize: '0.95rem', color: 'gray' }}>
            Zitate: 531&nbsp;&nbsp;|&nbsp;&nbsp;H-Index: 531&nbsp;&nbsp;|&nbsp;&nbsp;i10-Index: 531
          </Typography>
        </Box>
  
        <IconButton sx={{ padding: 0 }}>
          <NavigateNextRoundedIcon sx={{ fontSize: '2.5rem', color: 'black' }} />
        </IconButton>
      </Box>
    );
}

export default InstitutesRankCard