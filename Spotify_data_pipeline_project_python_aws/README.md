# Spotify ETL Pipeline using Python and AWS

## Project Overview

This project demonstrates a data engineering pipeline built using the Spotify Web API, Python, and Amazon Web Services (AWS).

The pipeline extracts music metadata from a Spotify playlist, stores the raw API response in Amazon S3, transforms the data into structured datasets, and stores the processed data in S3.

This hands-on project focuses on API integration, Python-based ETL development, JSON processing, and cloud storage.

## Architecture

**Spotify Web API → Python (Extraction) → Amazon S3 (Raw Data) → Python (Transformation) → Amazon S3 (Transformed Data)**

## Technologies Used

- **Python** — Data extraction and transformation
- **Spotify Web API** — Source of playlist and track metadata
- **Spotipy** — Python library for Spotify API integration
- **Amazon S3** — Storage for raw and transformed data
- **Boto3** — Python SDK for AWS services
- **Jupyter Notebook** — Development and exploration

## Project Structure

```text
Spotify-ETL-Pipeline-with-Python-AWS/
│
├── spitify_api_data_extract.py
├── spotify_transformation_load_function.py
├── Spotify data pipeline project python AWS.ipynb
├── README.md
└── .gitignore
```

## Data Pipeline Workflow

### 1. Extract

- Connect to the Spotify Web API using Spotipy.
- Retrieve playlist and track metadata, including album, artist, and song details.
- Serialize the API response into JSON format.

### 2. Store Raw Data

- Use Boto3 to upload the raw JSON response to Amazon S3.
- Organize raw files under the `raw_data/to_processed/` prefix.

### 3. Transform

- Extract album attributes, including album ID, name, release date, and total tracks.
- Extract artist attributes, including artist ID and artist name.
- Extract track attributes, including track ID, title, duration, popularity, and Spotify URL.
- Prepare structured datasets for further analysis.

### 4. Store Transformed Data

- Store the transformed datasets in Amazon S3 for downstream use and analysis.

## Prerequisites

- Python 3
- Spotify Developer account and application credentials
- AWS account and Amazon S3 bucket
- Appropriate AWS permissions
- Required Python libraries: `spotipy`, `boto3`, and `jupyter`

## Learning Outcomes

- REST API integration and data extraction
- Python-based ETL pipeline development
- JSON data processing and transformation
- Cloud object storage using Amazon S3
- AWS service integration using Boto3
- Organizing raw and transformed data for analytics

---

**Project Status:** Completed

**Project Type:** Personal Data Engineering Project