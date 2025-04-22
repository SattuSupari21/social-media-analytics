# 📊 Social Media Analytics Project

This project analyzes social media post performance across platforms, content types, and regions using a modern data stack. It provides insights into engagement trends, virality, and top-performing content to support data-driven social media strategies.

## 🚀 Tech Stack

- **ETL**: [Mage.ai](https://www.mage.ai/) – Low-code pipeline orchestration
- **Data Warehouse**: [PostgreSQL](https://www.postgresql.org/) – Central data storage
- **Visualization**: [Apache Superset](https://superset.apache.org/) – Interactive dashboards
- **Data Modeling**: SQL
- **Notebooks**: Jupyter (for EDA and feature engineering)

## ERD Schema
!(erd-schema)[https://raw.githubusercontent.com/SattuSupari21/social-media-analytics/refs/heads/main/docs/erd_schema.png]

## 📌 Dataset Description

| Column           | Description                        |
|------------------|------------------------------------|
| `Post_ID`        | Unique identifier for each post    |
| `Platform`       | Platform name (e.g., Instagram)    |
| `Hashtag`        | Hashtags used in the post          |
| `Content_Type`   | Type of content (Reel, Shorts, etc.) |
| `Region`         | Region where post was targeted     |
| `Views`          | Number of views                    |
| `Likes`          | Number of likes                    |
| `Shares`         | Number of shares                   |
| `Comments`       | Number of comments                 |
| `Engagement_Level` | Label (Low, Medium, High)        |

## 📊 KPIs & Metrics

- **Total Posts**
- **Total Views**
- **Engagement Rate** = (Likes + Shares) / Views
- **Virality Score** = Shares / Views
- **Platform vs Content Type Performance**

## 📈 Key Visualizations (Superset)

- **KPI Cards**: Engagement Rate, Views, Top Region
- **Time Trends**: Views, Likes, Shares over time
- **Bar Charts**: Engagement by Platform and Content Type
- **Geo View**: Region-wise Engagement
- **Tables**: Top and Bottom Performing Posts
- **Hashtag Analysis**: Word cloud or frequency bar

## 🧪 How to Run Locally

1. Clone the repo
```
git clone https://github.com/SattuSupari21/social-media-analytics.git
cd social-media-analytics
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Navigate to your project directory and initialize Mage:
```
cd mage-ai
mage start social-media-analytics-pipeline
```
4. Navigate to http://localhost:6789
5. Update the Mage PostgreSQL integration:
- Go to "Pipilines" → Select "etl_pipeline" → Click on "Edit pipeline"
- Edit your PostgreSQL credentials in the "io_config.yaml" file: 
```
POSTGRES_DBNAME: postgres
POSTGRES_SCHEMA: public # Optional
POSTGRES_USER: "your_username"
POSTGRES_PASSWORD: "your_password"
POSTGRES_HOST: localhost
POSTGRES_PORT: 5432
```
6. Run the Pipeline:
```
mage run social-media-analytics-pipeline etl_pipeline
```
