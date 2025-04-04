import { createTheme } from '@mui/material/styles';

// Define your color palette here
const palette = {
  primary: {
    main: '#008C8B',
    light: '#00A3A9',
    dark: '#070F12',
  },
  background: {
    default: '#DEDDDD',
    paper: '#fff',
  },
  text: {
    primary: '#111',
  },
};

export const theme = createTheme({
  palette,
  typography: {
    fontFamily: '"Inter", "Roboto", "Arial", sans-serif',
  },
  spacing: 8,
});
