CREATE OR REPLACE FUNCTION public.google_flood_status(
    z integer,
    x integer,
    y integer)
    RETURNS bytea
    LANGUAGE 'plpgsql'
    COST 100
    STABLE PARALLEL SAFE
AS $BODY$
DECLARE
    result bytea;
BEGIN
    WITH
        bounds AS (
            -- Convert tile coordinates to web mercator tile bounds
            SELECT ST_TileEnvelope(z, x, y) AS geom
        ),
        latest_status AS (
            -- Get the latest status for each gauge
            SELECT DISTINCT ON (gauge_id)
                gauge_id,
                issued_time,
                severity,
                forecast_trend,
                quality_verified,
                source,
                forecast_start,
                forecast_end,
                value_change_lower,
                value_change_upper
            FROM public.google_flood_status
            ORDER BY gauge_id, issued_time DESC
        ),
        mvt AS (
            SELECT
                ST_AsMVTGeom(ST_Transform(g.geom, 3857), bounds.geom) AS geom,
                g.gauge_id,
                g.site_name,
                g.river,
                g.country_code,
                g.source AS gauge_source,
                g.quality_verified AS gauge_quality_verified,
                g.has_model,
                s.issued_time,
                s.severity,
                s.forecast_trend,
                s.quality_verified AS status_quality_verified,
                s.source AS status_source,
                s.forecast_start,
                s.forecast_end,
                s.value_change_lower,
                s.value_change_upper
            FROM public.google_flood_gauge g
            CROSS JOIN bounds
            LEFT JOIN latest_status s ON g.gauge_id = s.gauge_id
        )
    -- Generate MVT encoding of final input record
    SELECT ST_AsMVT(mvt, 'default')
    INTO result
    FROM mvt;

    RETURN result;
END;
$BODY$;
