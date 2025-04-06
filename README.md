#  Healthcare Readmission Analysis 

This project explores U.S. hospital data to uncover insights about hospital distribution, types, and ownership across states. Using real-world datasets, the goal is to build a clean and visual exploratory analysis, setting the foundation for advanced analytics and cloud integration (AWS S3, Athena, QuickSight).

## Project Objectives
- Analyze hospital distribution by state
- Examine hospital ownership models
- Visualize hospital types and ratings
- Prepare data for cloud pipeline (AWS)

## Project Structure

- data/ : Dataset(s) from CMS
- notebooks/ : Jupyter Notebooks with data cleaning and analysis
- outputs/ : Visualizations and exported reports

## Visualizations
- Top states by number of hospitals
- Hospital types distribution
- Ownership analysis
- PDF report included

## Next Steps
- Upload dataset to AWS S3
- Use AWS Athena for query analysis
- Build QuickSight dashboard

## Tools & Technologies
- Python: Pandas, Matplotlib, Seaborn
- Jupyter Notebook
- Git & GitHub for version control
- AWS (planned): S3, Athena, QuickSight

## Visualizations

### Top 10 States by Number of Hospitals
![Top States](outputs/top_states_hospitals.png)

### Hospital Type Distribution
![Hospital Types](outputs/hospital_type_distribution.png)

## Report
- [EDA Report PDF](outputs/EDA_Hospital_info.pdf)

## Next Steps
- Upload cleaned dataset to AWS S3
- Query with AWS Athena
- Build visual dashboard in AWS QuickSight
- Extend analysis with healthcare cost and patient outcome datasets

## Connect
Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/shazia-kashif-958621262/) for collaboration or feedback!
##  Cloud Extension

This project has been extended to the cloud using AWS services for scalable analytics.

-  Uploaded cleaned hospital dataset to **Amazon S3**
-  Created external table in **AWS Athena** to query directly from S3
-  Ran queries in Athena to analyze hospital distribution across states
- Results exported for future visualization in **AWS QuickSight**

### Athena Query Example

```sql
SELECT state, COUNT(*) AS hospital_count
FROM healthcare_readmission
GROUP BY state
ORDER BY hospital_count DESC
LIMIT 10;

## Cloud Dashboard

View the live dashboard on AWS QuickSight:
[Healthcare Readmission Dashboard](https://us-east-1.quicksight.aws.amazon.com/sn/dashboards/c1b0e242-7a30-4448-a77d-afda5890e77f)

#  Healthcare Readmission Analysis Project

## Overview
This project analyzes U.S. hospital data to explore readmission trends across states. Using cleaned CMS data, we identified states with higher counts of hospitals marked as "worse than national average" in readmission measures.

## Dataset
- **CMS Hospital General Information**
- Cleaned and processed dataset: `cleaned_cms_hospital_info.csv`

## Tools & Technologies
- Python (Pandas, Matplotlib, Seaborn)
- Jupyter Notebook
- Data visualization
- AWS (S3, Athena, QuickSight planned)

## Key Insights
- **Top states with higher readmission concerns identified**
- Bar chart visualized readmission measures across states
- Exported state-level summary for future dashboarding

## Project Files
- Bar chart: `state_readmission_chart.png`
- Summary CSV: `state_readmission_summary.csv`

## Next Steps
- AWS QuickSight dashboard creation
- Prepare for AWS MLOps Certification 
- Extend project with AWS Glue and Redshift

## Connect
Feel free to explore my full project and code on GitHub: [https://github.com/ShaziaK354/healthcare-readmission-analysis/tree/main]





