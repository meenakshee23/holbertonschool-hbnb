erDiagram
    PERSON {
        int id
        string first_name
        string last_name
        date birth_date
    }

    ADDRESS {
        int id
        string street
        string city
        string postal_code
    }

    COMPANY {
        int id
        string name
    }

    PERSON ||--o{ ADDRESS : has
    COMPANY ||--o{ PERSON : employs
