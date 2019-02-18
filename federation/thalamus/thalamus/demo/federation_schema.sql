/* People table */
CREATE TABLE IF NOT EXISTS people (
    id varchar PRIMARY KEY,
    data jsonb
    );

/* Page of Life */
CREATE TABLE IF NOT EXISTS pols (
    id varchar PRIMARY KEY,
    book varchar REFERENCES people (id),
    data jsonb
    );

/* Personal Documents */
CREATE TABLE IF NOT EXISTS personal_docs (
    id varchar PRIMARY KEY,
    fedacct varchar REFERENCES people (id),
    pol varchar REFERENCES pols (id),
    document bytea,
    data jsonb);

/* Domiciliary Units */
CREATE TABLE IF NOT EXISTS dus (
    id varchar PRIMARY KEY,
    data jsonb);

/* Institutions */
CREATE TABLE IF NOT EXISTS institutions (
    id varchar PRIMARY KEY,
    data jsonb);
