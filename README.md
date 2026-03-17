# Remote-Jobs-Scraper-Data-Pipeline-mini-project-2

## Project Overview

This project is an industry-level web scraping and data pipeline system that extracts remote job listings from RemoteOK and stores them in structured formats for further analysis.

The system uses browser automation with Playwright to simulate real user behavior and ensure reliable data extraction from dynamic web pages.

This project demonstrates real-world data engineering concepts, including scraping, cleaning, deduplication, and database storage.

## Business Objective

The goal of this project is to:

Collect real-time remote job listings

Structure job data for analysis and reporting

Build a reusable job data pipeline

Enable future use cases like:

Job recommendation systems

Market trend analysis

Salary insights

## Key Features

✔ Automated job scraping using browser automation
✔ Handles dynamic content (JavaScript rendering)
✔ Extracts key job attributes:

Job Title

Company Name

Salary (if available)

Job Link

Source

✔ Data cleaning and duplicate removal
✔ Stores data in:

CSV file

SQLite database

✔ Industry-level pipeline design

## Technologies Used

Python

Playwright (Browser Automation)

Pandas

SQLite

Data Engineering Concepts

## Project Structure

job-scraper-pipeline/


├── data/

   └── professional_jobs.csv
│
├── database/

   └── jobs_database.db
│
├── scripts/

   └── job_scraper.py
│
├── README.md

└── requirements.txt

## How It Works (Pipeline Flow)

### 1️⃣ Browser Automation

Launches a Chromium browser using Playwright

Navigates to RemoteOK job listings page

Scrolls to load dynamic content

### 2️⃣ Data Extraction

Extracts job details:

Title

Company

Salary

URL

### 3️⃣ Data Cleaning

Removes duplicates

Handles missing values

Filters invalid records

### 4️⃣ Data Storage

Saves cleaned data into:

CSV file (professional_jobs.csv)

SQLite database (jobs_database.db)

## Installation & Setup

### Clone Repository

git clone https://github.com/yourusername/job-scraper-pipeline.git

cd job-scraper-pipeline

### Install Dependencies

pip install -r requirements.txt

playwright install

## Usage

### Run the scraper:

python job_scraper.py

### Output:

CSV file with job listings

SQLite database for structured storage

## Example Output

Title	            Company	      Salary	       Source
Python Developer	XYZ Company	  $80k	         RemoteOK

## Key Highlights (Industry Level)

This project reflects real-world practices:

Uses Playwright instead of simple requests (important for modern scraping)

Implements data pipeline structure

Stores data in database (important for data engineering)

Handles dynamic websites

## Future Improvements

Add scheduling (Cron / Airflow)

Store data in cloud (AWS / GCP)

Build API for job access

Add dashboard (Streamlit / Power BI)

Multi-website scraping (LinkedIn, Indeed)

## Author

### Adeel Khan
### Aspiring Data Engineer
