COPY gov_contract_analysis.contracting_table(
    contracting_agency_id,
    contracting_office_id,
    contracting_department_id,
    contracting_agency_name,
    contracting_office_name,
    contracting_department_name
)
FROM 'H:/DATA SCIENCE/DataProj/SMS-Data-Projects/pgADMIN/contracting_table_clean.csv'
WITH (
    FORMAT csv,
    DELIMITER ',',
    HEADER true,
    NULL ''
);
