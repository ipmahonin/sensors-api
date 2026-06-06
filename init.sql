CREATE TABLE IF NOT EXISTS sensors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    value REAL NOT NULL,
    status TEXT NOT NULL
);