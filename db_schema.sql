CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    name TEXT NOT NULL,
    location TEXT, 
    url TEXT,
    type TEXT
);