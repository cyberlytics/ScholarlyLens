import { Box, Typography } from "@mui/material";
import CitationChart from "./CitationChart";

const InstitesAnalytics = () => {
  return (
    <Box
      sx={{
        border: "1px solid",
        borderColor: "primary.main",
        borderRadius: "12px",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        boxShadow: '8px 8px 30px rgba(0,0,0,0.1)',
        width: 300,
        gap: 1,
        backgroundColor: "background.main"
      }}
    >
      <Typography variant="subtitle1" sx={{ fontWeight: 100, mb: 1 }}>
        Citations per year
      </Typography>

      <Box sx={{ width: "100%" }}>
        <CitationChart />
      </Box>

      {/* Zitate Section */}
      <Box textAlign="center">
        <Typography variant="body2">Zitate: 531</Typography>
        <Typography variant="caption" color="primary">
          (last 5 y: 500)
        </Typography>
        <Typography variant="body2" sx={{ color: "green", fontWeight: 600 }}>
          ↑ +20%
        </Typography>
      </Box>

      {/* H-Index Section */}
      <Box textAlign="center">
        <Typography variant="body2">H-Index: 531</Typography>
        <Typography variant="caption" color="primary">
          (last 5 y: 500)
        </Typography>
        <Typography variant="body2" sx={{ color: "red", fontWeight: 600 }}>
          ↓ -20%
        </Typography>
      </Box>

      {/* i10-Index Section */}
      <Box textAlign="center">
        <Typography variant="body2">i10-Index: 531</Typography>
        <Typography variant="caption" color="primary">
          (last 5 y: 500)
        </Typography>
        <Typography variant="body2" sx={{ color: "#d4af37", fontWeight: 600 }}>
          0%
        </Typography>
      </Box>
    </Box>
  );
};

export default InstitesAnalytics;
