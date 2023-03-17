# Analysis of UK Population Health and Tenure
This data science project focuses on the analysis of the UK population's health and tenure rates. The project utilizes data downloaded from the Nomis database, containing information on general health, tenure class, age, date, and geographic encoding. The goal of this project is to provide valuable insights into the relationship between tenure categories and general health conditions in the UK population, which could serve as a reference for policymakers in improving the socio-economic well-being of the population.

## Technologies Used
Python
Tableau
## Data Preparation
The datasets used in this project were downloaded from the Nomis database and are formatted in a CSV file containing multiple tables. The basic data wrangling process involved aligning all keys and tables into a separate list by their respective index. Further wrangling processes were performed inside each iteration depending on the area of interest. For the analysis task, the population data was transformed into percentages and identified as quantitative, categorical, and ordinal data. For the query task, data projection methods such as PCA and UMAP were used to decompose the attributes into lower dimensions for visualisation.

## Visualisation
All visualisations were created on a Tableau dashboard and designed to address the various tasks required in the analysis of the UK population's health and tenure rates. The visualisation techniques used include choropleth maps, bar charts, box plots, and scatter plots.

The scatter plots are created using UMAP and PCA analysis, which are powerful techniques for reducing data dimensionality while preserving the most relevant features. The UMAP algorithm is used for embedding the health data, while the PCA algorithm is used for embedding the age data.

## Conclusion
The insights provided by this analysis could serve as a valuable reference for policymakers to help improve the socio-economic well-being of the population in the UK. By using Tableau, we were able to create comprehensive visualisations that allow for easy exploration and interpretation of the data. The use of PCA and UMAP analysis provided an efficient way of reducing the data dimensionality while preserving the most relevant features.
