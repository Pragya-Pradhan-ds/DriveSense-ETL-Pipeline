CREATE TABLE IF NOT EXISTS raw_eco_driving (
    id SERIAL PRIMARY KEY,
    rpm_variation INTEGER,
    harsh_braking_count INTEGER,
    idling_time NUMERIC(6,2),
    fuel_consumption NUMERIC(6,2),
    acceleration_smoothness NUMERIC(6,2),
    eco_score NUMERIC(6,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);