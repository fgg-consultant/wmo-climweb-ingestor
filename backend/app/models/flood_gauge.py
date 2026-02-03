from geoalchemy2 import Geometry

from app import db


class FloodGauge(db.Model):
    __tablename__ = "google_flood_gauge"

    gauge_id = db.Column(db.String(256), primary_key=True)
    site_name = db.Column(db.String(512), nullable=True)
    river = db.Column(db.String(256), nullable=True)
    country_code = db.Column(db.String(3), nullable=False)
    source = db.Column(db.String(64), nullable=True)
    quality_verified = db.Column(db.Boolean, default=False)
    has_model = db.Column(db.Boolean, default=False)
    geom = db.Column(Geometry(geometry_type="POINT", srid=4326), nullable=False)

    def __repr__(self):
        return f'<FloodGauge {self.gauge_id}>'

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            "gauge_id": self.gauge_id,
            "site_name": self.site_name,
            "river": self.river,
            "country_code": self.country_code,
            "source": self.source,
            "quality_verified": self.quality_verified,
            "has_model": self.has_model,
        }
