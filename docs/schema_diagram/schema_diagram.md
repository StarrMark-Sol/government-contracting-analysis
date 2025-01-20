:::mermaid
classDiagram
    %% Funding Table
    class Funding {
        TEXT funding_department_id
        TEXT funding_department_name
        TEXT funding_agency_id
        TEXT funding_agency_name
        TEXT funding_office_id
        TEXT funding_office_name
        NUMERIC dollars_obligated
    }

    %% Vendor Table
    class Vendor {
        BOOLEAN is_8a_joint_venture
        BOOLEAN is_8a_program_participant
        BOOLEAN is_alaskan_native_corporation_owned
        BOOLEAN is_alaskan_native_servicing_institution
        BOOLEAN is_american_indian
        BOOLEAN is_asian_pacific_american_owned
        BOOLEAN is_black_american_owned
        BOOLEAN is_dot_certified_disadvantaged_business
        BOOLEAN is_educational_institution
        BOOLEAN is_emerging_small_business
        BOOLEAN is_economically_disadvantaged_wosb
        BOOLEAN is_hubzone_firm
        BOOLEAN is_hubzone_joint_venture
        BOOLEAN is_native_american_owned
        BOOLEAN is_tribally_owned
        BOOLEAN is_planning_commission
        BOOLEAN is_service_disabled_veteran_owned
        BOOLEAN is_veteran_owned
        BOOLEAN is_women_owned_smb
    }

    %% Contracting Table
    class Contracting {
        TEXT contracting_agency_id
        TEXT contracting_office_id
        TEXT contracting_department_id
        TEXT contracting_agency_name
        TEXT contracting_office_name
        TEXT contracting_department_name
    }

    %% NAICS Table
    class NAICS {
        TEXT naics_code
        TEXT naics_description
    }

    %% ProductService Table
    class ProductService {
        TEXT product_service_code
        TEXT product_service_description
    }

    %% LaborStandard Table
    class LaborStandard {
        TEXT labor_standards_code
        TEXT labor_standards_description
    }

    %% Contracts Table
    class Contracts {
        SERIAL contract_id
        INT vendor_id
        INT funding_id
        INT contracting_id
        INT major_command_id
        INT naics_id
        INT product_service_id
        INT set_aside_id
        INT labor_standards_id
        NUMERIC dollars_obligated
        DATE start_date
        DATE end_date
        DATE date_signed
        VARCHAR(255) period_of_performance
        DATE last_date_order
        DATE completion_date
    }

    %% Relationships
    Vendor <|-- Contracts : vendor_id (Foreign Key)
    Funding <|-- Contracts : funding_id (Foreign Key)
    Contracting <|-- Contracts : contracting_id (Foreign Key)
    NAICS <|-- Contracts : naics_id (Foreign Key)
    ProductService <|-- Contracts : product_service_id (Foreign Key)
    LaborStandard <|-- Contracts : labor_standards_id (Foreign Key)
:::


