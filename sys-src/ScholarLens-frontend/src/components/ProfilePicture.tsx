import Box from '@mui/material/Box';

const ProfilePicture = () => {

    const profilePicture = "https://via.placeholder.com/150"
  return (
    <Box
  sx={{
    backgroundColor: '#e0e0e0', // light gray background
    border: '1px solid #0097a7', // teal border
    borderRadius: '16px', // rounded corners
    boxShadow: 3, // MUI shadow level
    padding: 2,
    width: 150,
    height: 200,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  }}
>
  <img src={profilePicture} alt="Graduation Icon" style={{ width: 50, height: 50 }} />
</Box>
  )
}

export default ProfilePicture