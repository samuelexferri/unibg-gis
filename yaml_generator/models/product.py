class Product:
    def __init__(
        self,
        name,
        description,
        storage_driver,
        storage_dimension_order,
        measurements,
        crs="EPSG:4326",
        metadata_type="eo3",
    ):
        self.name = name
        self.description = description
        self.metadata_type = metadata_type
        self.metadata = {"product": {"name": name}}
        self.measurements = []

        for measurement in measurements:
            self.measurements.append(
                {
                    "name": measurement.name,
                    "dtype": measurement.dtype,
                    "nodata": measurement.nodata,
                    "units": measurement.units,
                }
            )

        self.storage = {
            "driver": storage_driver,
            "crs": crs,
            "dimension_order": storage_dimension_order,
        }
