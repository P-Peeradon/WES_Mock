DROP TABLE student;
DROP TABLE unit;
DROP TABLE enrolment;

"""
    This is the DDL statement for creating database
"""

CREATE TABLE student(
	stu_id CHAR(8) NOT NULL UNIQUE,
    stu_fname VARCHAR(20) NOT NULL,
    stu_lname VARCHAR(30) NOT NULL,
    stu_dob DATE NOT NULL,
    stu_program VARCHAR(50),
    stu_email VARCHAR(40),
    stu_address VARCHAR(80),
    CONSTRAINT stu_pk PRIMARY KEY (stu_id)
);

CREATE TABLE unit(
	u_unitcode CHAR(5) NOT NULL UNIQUE,
    u_unitname VARCHAR(25) NOT NULL UNIQUE,
    u_unitdesc VARCHAR(100), 
    u_creditpoint INTEGER DEFAULT(6),
    u_duration FLOAT4,
    CONSTRAINT unit_pk PRIMARY KEY (u_unitcode)
);

CREATE TABLE enrolment(
	en_enroldate DATE NOT NULL,
    stu_id CHAR(8) NOT NULL,
    u_unitcode CHAR(5) NOT NULL,
    en_semester INTEGER NOT NULL,
    en_year INTEGER NOT NULL,
    CONSTRAINT en_pk PRIMARY KEY (stu_id, u_unitcode, en_semester, en_year)
);    

ALTER TABLE enrolment 
	ADD CONSTRAINT en_unit_fk FOREIGN KEY (u_unitcode) REFERENCES unit (u_unitcode);
    
ALTER TABLE enrolment 
	ADD CONSTRAINT en_stu_fk FOREIGN KEY (stu_id) REFERENCES student (stu_id);