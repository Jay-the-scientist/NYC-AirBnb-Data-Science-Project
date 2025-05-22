# NYC Airbnb Market Analysis

## Objective
Analyze Airbnb listings in New York City to uncover pricing trends, neighborhood dynamics, and occupancy patterns to support data-driven decision-making for hosts and travelers.

## Project Description
This project explores the publicly available NYC Airbnb dataset to better understand how location, room type, availability, and other features affect listing prices and distribution. Insights from this analysis can help inform pricing strategies and identify areas of high or low saturation.

## Installation
Required packages can be installed using:
```bash
pip install pandas numpy matplotlib seaborn
```

## Dataset
**Source:** Inside Airbnb — [http://insideairbnb.com/get-the-data/](http://insideairbnb.com/get-the-data/)  
**Size:** ~49,000 listings across five NYC boroughs  
**Features:** Listing ID, host ID, neighborhood, room type, price, minimum nights, number of reviews, availability, etc.  
**Timeframe:** Data snapshot from 2019  

## Methodology
- Loaded and cleaned the dataset  
- Removed outliers in price and minimum nights  
- Aggregated data by borough and neighborhood  
- Visualized distribution of room types and prices  
- Analyzed correlations between features and pricing  
- Identified patterns in availability and review counts  

## Visualizations
- Price distribution histograms  
- Box plots by room type and borough  
- Heatmap of average prices by neighborhood  
- Correlation matrix of numerical features  
- Availability vs. price scatter plots  

## Insights
- Manhattan has the highest density and prices for Airbnb listings  
- Private rooms are the most common room type overall  
- Prices vary significantly by borough and neighborhood  
- Listings with higher availability tend to be moderately priced  
  

