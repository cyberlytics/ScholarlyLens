import { Typography, Paper } from "@mui/material";

const Publication = () => {
  const title = "Fully automatic breast segmentation in 3D breast MRI";
  const authors = ["L. Wang", "B. Platel", "T. Ivanovskaya", "M. Harz", "H.K. Hahn"];
  const details = "2012 9th IEEE International Symposium on Biomedical Imaging 1024-1027";

  return (
    <Paper
      elevation={3}
      sx={{
        borderRadius: "16px",
        padding: 2,
        backgroundColor: "#e0e0e0", // light grey background
        maxWidth: "100%",
      }}
    >
      <Typography variant="h6" sx={{ color: "#008080", fontWeight: 500 }}>
        {title}
      </Typography>
      <Typography variant="body2" sx={{ mt: 0.5 }}>
        {authors.join(", ")}
      </Typography>
      <Typography variant="body2" sx={{ mt: 0.5 }}>
        {details}
      </Typography>
    </Paper>
  );
};

export default Publication;
