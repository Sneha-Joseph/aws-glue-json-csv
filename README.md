# aws-glue-json-csv
# JSON to CSV Data Transformation Using AWS Glue Studio

## 📖 Project Overview

In this project, I built a data processing pipeline using **AWS Glue Studio’s visual ETL interface** to transform JSON data into CSV format. The pipeline reads data from an input S3 bucket, removes duplicate records, selects relevant fields, and stores the cleaned data into an output S3 bucket in CSV format.

---

## ✅ What I Have Implemented

1. **Data Ingestion from S3**
   - Uploaded JSON files containing employee information to an input Amazon S3 bucket.

2. **Data Cleaning and Transformation**
   - Used AWS Glue Studio's visual ETL interface to configure the pipeline.
   - Removed duplicate records to ensure data accuracy.
   - Selected only required fields (`emp_id`, `name`, `salary`, `address`) for the output.

3. **Data Storage in CSV Format**
   - Stored the transformed data into another Amazon S3 bucket in CSV format for analysis or reporting.

4. **IAM Configuration**
   - Created an IAM role with:
     - **Amazon S3 Full Access** – to read from and write to the S3 buckets.
     - **AWS Glue Service Role** – to allow AWS Glue to access resources securely.

---

## 🛠 Tools & Technologies Used

- **Amazon S3** – For storing both input and output data files.
- **AWS Glue Studio** – For visually designing and running the ETL pipeline without coding.
- **AWS IAM** – For managing permissions using appropriate roles and policies.
- **ETL (Extract, Transform, Load)** – To clean and format the data.
- **CSV Format** – The final output format for structured data analysis.
- **PySpark (underlying technology)** – AWS Glue jobs use PySpark for data transformation, though the logic was configured through the visual interface.

---

## 📂 Input File Format

The input files are in JSON format. Example structure:

```json
[
  {
    "emp_id": "101",
    "name": "John Doe",
    "salary": "70000",
    "address": "123 Main Street"
  },
  {
    "emp_id": "102",
    "name": "Jane Smith",
    "salary": "80000",
    "address": "456 Oak Avenue"
  }
]
