import uuid
from datetime import datetime


class Dataset:
    def __init__(
        self,
        product_name,
        longitudes,
        latitudes,
        measurements,
        product_href="",
        crs="EPSG:4326",
        grid_transform=[1, 0, 0, 0, 1, 0, 0, 0, 1],
    ):
        self.id = str(uuid.uuid4())
        self.product = {"name": product_name, "href": product_href}

        self.crs = crs

        min_lat = "%" + str(min(latitudes)) + "%"
        max_lat = "%" + str(max(latitudes)) + "%"
        min_lon = "%" + str(min(longitudes)) + "%"
        max_lon = "%" + str(max(longitudes)) + "%"
        self.geometry = {
            "type": "Polygon",
            "coordinates": [
                [
                    [max_lon, max_lat],
                    [max_lon, min_lat],
                    [min_lon, min_lat],
                    [min_lon, max_lat],
                    [max_lon, max_lat],
                ]
            ],
        }

        print(self.geometry)
        self.grids = {
            "default": {"shape": [len(longitudes), len(latitudes)]},
            "transform": grid_transform,
        }
        self.lineage = {}
        self.measurements = []
        for measurement in measurements:
            self.measurements.append(
                {
                    "layer": measurement.layer,
                    "path": measurement.path,
                }
            )

        time_now = datetime.utcnow().isoformat()[:-3] + "Z"
        self.properties = {
            "odc:file_format": "NetCDF",
            "odc:processing_datetime": time_now,
            "datetime": time_now,
        }
