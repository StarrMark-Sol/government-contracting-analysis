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

## Project Structure
government-contracting-analysis/ ├── data/ │ ├── raw/ # Raw data files downloaded from Sam.gov│ ├── cleaned/ # Cleaned data files ├── scripts/ │ ├── data_cleaning/ # Python scripts for data cleaning │ ├── sql/ # SQL scripts for creating schema and importing data ├── docs/ │ ├── schema_diagram/ # Mermaid diagrams and documentation ├── .gitignore # Git ignore file ├── README.md# Main README file


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

