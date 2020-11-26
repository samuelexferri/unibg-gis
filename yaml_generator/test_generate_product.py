import os
import sys

import yaml

from models.measurement import Measurement
from models.product import Product

measurements = [Measurement("cloud_pressure", "float64", "Pa", -1)]

product = Product(
    "sentinel5p",
    "Sentinel5P NetCDF with various layers",
    measurements=measurements,
    storage_driver="NetCDF CF",
    storage_dimension_order=["time", "latitude", "longitude"],
)

# Suppress starting tag
yaml.emitter.Emitter.process_tag = lambda self, *args, **kw: None


with open(
    os.path.join(os.path.dirname(__file__), "./tests/product_generated.yaml"), "w"
) as f:
    data = yaml.dump(product, f, sort_keys=False)
