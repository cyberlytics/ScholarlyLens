import {  Tabs, Tab, Box,Typography } from "@mui/material"
import { Link } from "react-router-dom"
import { useState } from "react"
import ScholarRankCard from "../components/ScholarRankCard";
import Publication from "../components/Publication";
import InstitesAnalytics from "../components/InstittutesAnalytics";

const InstitutDetailPage = () => {

  const [tabIndex, setTabIndex] = useState(0);

  const institutesLogo = "src/assets/OTH-AW_Logo_Mini.png"
  const instituteName = "Ostbayerische Technische Hochschule Amberg-Weiden"
  const adress = "Kaiser-Wilhelm-Ring 23, 92224 Amberg, Germany"
  const website = "https://www.oth-aw.de/"

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setTabIndex(newValue);
  };

  function TabPanel(props: { children: React.ReactNode; value: number; index: number }) {
    const { children, value, index } = props;
  
    return (
      <div hidden={value !== index}>
        {value === index && (
          <Box sx={{ pt: 2 }}>
            {children}
          </Box>
        )}
      </div>
    );
  }

  return (
    <Box>
      
      <Box display="flex" gap="2rem" alignItems="flex-start" width="100%" mb={4}>
      <Box display="flex" flexDirection="column" alignItems="center" gap={2}>
        <img style={{ width: 150 }} src={institutesLogo} alt="Logo" />
        <InstitesAnalytics/>
        </Box>
        <Box>
          <Typography variant="h1" sx={{ fontSize: '2rem', mb: 1 }}>{instituteName}</Typography>
          <Typography>Address: {adress}</Typography>
          <Link to={website} target="_blank" rel="noopener noreferrer">{website}</Link>

          <Tabs value={tabIndex} onChange={handleTabChange} aria-label="institute detail tabs">
        <Tab label="Forschenden" />
        <Tab label="Publications" />
      </Tabs>

      {/* Tab Panels */}
      <TabPanel value={tabIndex} index={0}>
        <ScholarRankCard/>
      </TabPanel>
      <TabPanel value={tabIndex} index={1}>
        <Publication/>
      </TabPanel>
        </Box>
        
      </Box>

    </Box>
  );
}

export default InstitutDetailPage