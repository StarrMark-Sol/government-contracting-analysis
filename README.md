# Analysis of Government Contracting Data for Agile Transformation Opportunities

## Introduction
The goal of this project is to analyze government contracting data to identify opportunities for Agile transformation within the organization.

## Tools Used
- pgAdmin
- Python
- MS Excel
- Command Prompt
- Azure DevOps
- sam.gov

## Project Structures
government-contracting-analysis/
├── data/
│   ├── raw/                    # Raw data files downloaded from Sam.gov
│   │   ├── funding_table.csv
│   │   ├── vendor_table.csv
│   │   ├── contracting_table.csv
│   │   ├── naics_table.csv
│   │   ├── product_srvc_table.csv
│   │   └── labor_standard_table.csv
│   ├── cleaned/                 # Cleaned data files
│   │   ├── funding_table_clean.csv
│   │   ├── vendor_table_clean.csv
│   │   ├── contracting_table_clean.csv
│   │   ├── naics_table_clean.csv
│   │   ├── product_srvc_table_clean.csv
│   │   └── labor_standard_table_clean.csv
│
├── scripts/
│   ├── data_cleaning/           # Python scripts for data cleaning
│   │   ├── clean_funding_table.py
│   │   ├── clean_vendor_table.py
│   │   ├── clean_contracting_table.py
│   │   ├── clean_naics_table.py
│   │   ├── clean_product_srvc_table.py
│   │   └── clean_labor_standard_table.py
│   ├── sql/                     # SQL scripts for creating schema and importing data
│   │   ├── create_schema.sql
│   │   ├── import_funding_table.sql
│   │   ├── import_vendor_table.sql
│   │   ├── import_contracting_table.sql
│   │   ├── import_naics_table.sql
│   │   ├── import_product_srvc_table.sql
│   │   └── import_labor_standard_table.sql
│
├── docs/
│   ├── schema_diagram/          # Mermaid diagrams and documentation
│   │   ├── schema_diagram.mmd
│   │   └── schema_diagram.png
│
├── .gitignore                   # Git ignore file
├── README.md                    # Main README file
├── CONTRIBUTING.md              # Contributing guidelines
└── LICENSE                      # License information



## Steps Completed

1. **Create GitHub Account**
   - Signed up and confirmed email at [GitHub](https://github.com/).

2. **Create a New Repository**
   - Created a repository named `government-contracting-analysis`.

3. **Set Up Git on Computer**
   - Installed Git from [git-scm.com](https://git-scm.com/).
   - Configured Git with username and email.

4. **Clone Repository Locally**
   - Navigated to `D:\PROJECT` directory.
   - Cloned the repository using:
     ```sh
     git clone https://github.com/StarrMark-Sol/government-contracting-analysis.git
     ```

5. **Create Directory Structure**
   - Created the necessary folders:
     ```sh
     mkdir data
     mkdir scripts
     mkdir docs
     mkdir data\raw
     mkdir data\cleaned
     mkdir scripts\data_cleaning
     mkdir scripts\sql
     mkdir docs\schema_diagram
     ```

6. **Move Raw Data File**
   - Moved the raw data file from `H:\GovCon\PROPENSITY` to `data/raw` directory:
     ```sh
     move "H:\GovCon\PROPENSITY\DataAnalysis-541720.csv" "D:\PROJECT\government-contracting-analysis\data\raw\"
     ```

7. **Stage, Commit, and Push Changes**
   - Navigated to the repository directory:
     ```sh
     cd D:\PROJECT\government-contracting-analysis
     ```
   - Staged all changes:
     ```sh
     git add .
     ```
   - Committed the changes with a descriptive message:
     ```sh
     git commit -m "Added raw data file and organized project structure"
     ```
   - Pushed the changes to GitHub:
     ```sh
     git push origin main
     ```

## Next Steps
1. **Add Cleaned Data Files** (if applicable) to `data/cleaned`.
2. **Add Python Scripts for Data Cleaning** to `scripts/data_cleaning`.
3. **Add SQL Scripts for Creating Schema and Importing Data** to `scripts/sql`.
4. **Add Mermaid Diagrams and Documentation** to `docs/schema_diagram`.

## Contact
For any questions or support, please contact [your email].

## Steps Completed

...

8. **Add Cleaned Data Files**
   - Moved cleaned data files to the `data/cleaned` directory:
     ```sh
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\vendor_table_clean.csv" "D:\PROJECT\government-contracting-analysis\data\cleaned\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\product_srvc_table_clean.csv" "D:\PROJECT\government-contracting-analysis\data\cleaned\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\naics_table_clean.csv" "D:\PROJECT\government-contracting-analysis\data\cleaned\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\labor_standard_table_clean.csv" "D:\PROJECT\government-contracting-analysis\data\cleaned\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\funding_table_clean.csv" "D:\PROJECT\government-contracting-analysis\data\cleaned\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\contracting_table_clean.csv" "D:\PROJECT\government-contracting-analysis\data\cleaned\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\contract_table.csv" "D:\PROJECT\government-contracting-analysis\data\cleaned\"
     ```

## Next Steps

...

## Steps Completed

...

9. **Add Python Scripts for Data Cleaning**
   - Moved Python scripts for data cleaning to the `scripts/data_cleaning` directory:
     ```sh
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\clean_contracting.py" "D:\PROJECT\government-contracting-analysis\scripts\data_cleaning\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\create_table.py" "D:\PROJECT\government-contracting-analysis\scripts\data_cleaning\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\clean_labor.py" "D:\PROJECT\government-contracting-analysis\scripts\data_cleaning\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\import.py" "D:\PROJECT\government-contracting-analysis\scripts\data_cleaning\"
     ```

## Next Steps

...
## Steps Completed

...

10. **Add SQL Scripts for Creating Schema and Importing Data**
   - Moved SQL scripts to the `scripts/sql` directory:
     ```sh
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\data_import_contracting.sql" "D:\PROJECT\government-contracting-analysis\scripts\sql\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\update_column_data.sql" "D:\PROJECT\government-contracting-analysis\scripts\sql\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\validate_import.sql" "D:\PROJECT\government-contracting-analysis\scripts\sql\"
     ```

## Next Steps

...
## Steps Completed

...

11. **Add Raw CSV Files**
   - Moved raw CSV files to the `data/raw` directory:
     ```sh
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\contracting_table.csv" "D:\PROJECT\government-contracting-analysis\data\raw\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\funding_table.csv" "D:\PROJECT\government-contracting-analysis\data\raw\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\labor_standard_table.csv" "D:\PROJECT\government-contracting-analysis\data\raw\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\naics_table.csv" "D:\PROJECT\government-contracting-analysis\data\raw\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\product_srvc_table.csv" "D:\PROJECT\government-contracting-analysis\data\raw\"
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\vendor_table.csv" "D:\PROJECT\government-contracting-analysis\data\raw\"
     ```

## Next Steps

...

## Steps Completed

...

12. **Add Mermaid Diagrams**
   - Moved Mermaid diagrams to the `docs/schema_diagram` directory:
     ```sh
     move "H:\DATA SCIENCE\DataProj\SMS-Data-Projects\pgADMIN\schema_diagram.md" "D:\PROJECT\government-contracting-analysis\docs\schema_diagram\"
     ```

## Next Steps

...
