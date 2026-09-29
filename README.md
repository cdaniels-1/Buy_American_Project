# Buy American Dashboard

## Overview
The Buy American Dashboard is a full‑stack application designed to analyze product origin data and associated spending records. 
It provides a structured interface for exploring domestic vs. foreign product classifications and inspecting detailed transaction information. 
It is designed for school food administrators in compliance with the Buy American Provision, which states that the purchase of non-domestic food
in the National School Lunch Program (NSLP) and School Breakfast Program (SBP) may not exceed 10% of the total commerical food purchases.

## Objectives
- Integrate product metadata with spending-row records.
- Provide a secure, well-typed API for querying the dataset.
- Render large datasets efficiently in a browser environment.
- Present summary statistics and detailed product views for analysis.

## System Architecture

### Frontend
- React.js  
- Chakra UI  
- Axios  
- Virtualized rendering for large tables (10,000+ rows)

### Backend
- FastAPI  
- Python  
- Pydantic validation  
- Parameterized SQL queries

### Database
- SQLite  
- Tables for product metadata and spending-row records  

## Core Functionality

### Summary View
Displays aggregate statistics:
- Total products  
- Domestic vs. foreign counts  
- Domestic vs. foreign percentages

### Product List
Searchable list of all products with key attributes.

### Product Detail View
Includes:
- Full metadata for a selected product  
- All associated spending-row records  
- Virtualized table for efficient rendering  

## Running the Application

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
