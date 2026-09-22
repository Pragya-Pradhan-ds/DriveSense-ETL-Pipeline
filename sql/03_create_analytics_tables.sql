-- Drop tables if they already exist
DROP TABLE IF EXISTS agg_driver_summary;
DROP TABLE IF EXISTS anomaly_trips;

---------------------------------------------------
-- Driver Summary
---------------------------------------------------
CREATE TABLE agg_driver_summary AS
SELECT
    driver_id,
    COUNT(*) AS total_trips,
    ROUND(AVG(eco_score), 2) AS avg_eco_score,
    ROUND(AVG(fuel_consumption), 2) AS avg_fuel_consumption,
    ROUND(AVG(harsh_braking_count), 2) AS avg_harsh_braking,
    ROUND(AVG(idling_time), 2) AS avg_idling_time
FROM stg_eco_driving
GROUP BY driver_id;

---------------------------------------------------
-- Anomaly Trips
---------------------------------------------------
CREATE TABLE anomaly_trips AS
SELECT *
FROM stg_eco_driving
WHERE eco_score < 40
   OR harsh_braking_count > 8
   OR fuel_consumption >
      (
        SELECT AVG(fuel_consumption) + 2 * STDDEV(fuel_consumption)
        FROM stg_eco_driving
      );    