from geoalchemy2 import Geometry

from app import db

class DustForecast(db.Model):
    __tablename__ = "aemet_dust_forecast"
    __table_args__ = (
        db.UniqueConstraint("gid", "init_date", "forecast_date", name='unique_dust_forecast_date'),
    )

    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.String(256), db.ForeignKey('geo_region.gid', ondelete="CASCADE"), nullable=False)
    init_date = db.Column(db.DateTime, nullable=False)
    forecast_date = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    geom = db.Column(Geometry(geometry_type="MultiPolygon", srid=4326), nullable=False)

    def __init__(self, gid, init_date, forecast_date, value, geom):
        self.gid = gid
        self.init_date = init_date
        self.forecast_date = forecast_date
        self.value = value
        self.geom = geom

    def __repr__(self):
        return '<DustForecast %r>' % self.id

    def serialize(self):
        """Return object data in easily serializable format"""
        dust_forecast = {
            "id": self.id,
            "gid": self.gid,
            "init_date": self.init_date,
            "forecast_date": self.forecast_date,
            "value": self.value,
        }
        return dust_forecast
