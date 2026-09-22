-- ==========================================
-- Drop staging table if it already exists
-- ==========================================
DROP TABLE IF EXISTS stg_eco_driving;

-- ==========================================
-- Create staging table
-- ==========================================
CREATE TABLE stg_eco_driving AS

SELECT

    -- Generate synthetic Trip ID
    ROW_NUMBER() OVER (ORDER BY eco_score) AS trip_id,

    -- Generate synthetic Driver ID (150 drivers)
    NTILE(150) OVER (ORDER BY eco_score) AS driver_id,

    -- Original telemetry columns
    rpm_variation,
    harsh_braking_count,
    idling_time,
    fuel_consumption,
    acceleration_smoothness,
    eco_score,
    created_at

FROM raw_eco_driving;