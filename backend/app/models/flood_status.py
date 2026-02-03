from app import db


class FloodStatus(db.Model):
    __tablename__ = "google_flood_status"
    __table_args__ = (
        db.UniqueConstraint("gauge_id", "issued_time", name='unique_flood_status'),
    )

    id = db.Column(db.Integer, primary_key=True)
    gauge_id = db.Column(db.String(256), db.ForeignKey('google_flood_gauge.gauge_id', ondelete="CASCADE"), nullable=False)
    issued_time = db.Column(db.DateTime(timezone=True), nullable=False)
    severity = db.Column(db.String(32), nullable=False)  # EXTREME, SEVERE, ABOVE_NORMAL, NO_FLOODING, UNKNOWN
    forecast_trend = db.Column(db.String(32), nullable=True)  # RISE, FALL, NO_CHANGE
    quality_verified = db.Column(db.Boolean, default=False)
    source = db.Column(db.String(64), nullable=True)
    forecast_start = db.Column(db.DateTime(timezone=True), nullable=True)
    forecast_end = db.Column(db.DateTime(timezone=True), nullable=True)
    value_change_lower = db.Column(db.Float, nullable=True)
    value_change_upper = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<FloodStatus {self.id}>'

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            "id": self.id,
            "gauge_id": self.gauge_id,
            "issued_time": self.issued_time.isoformat() if self.issued_time else None,
            "severity": self.severity,
            "forecast_trend": self.forecast_trend,
            "quality_verified": self.quality_verified,
            "source": self.source,
            "forecast_start": self.forecast_start.isoformat() if self.forecast_start else None,
            "forecast_end": self.forecast_end.isoformat() if self.forecast_end else None,
            "value_change_lower": self.value_change_lower,
            "value_change_upper": self.value_change_upper,
        }
