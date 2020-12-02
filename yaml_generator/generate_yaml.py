import os
from pathlib import Path
import yaml
import xarray
from models.measurement import Measurement
from models.product import Product
from models.dataset import Dataset


def generate_yaml_from_netCDF(nc_path, product_name, product_description, no_data):
    # Extract data from netCDF file
    dataset = xarray.load_dataset(nc_path)

    measurements = []
    dims = [i for i in dataset.sizes.mapping.mapping]
    for var in dataset:
        ds_var = dataset[var].variable
        if "units" in ds_var.attrs.keys():
            measurements.append(
                Measurement(
                    var,
                    ds_var.dtype.name,
                    ds_var.attrs["units"],
                    no_data,
                    Path(nc_path).name,
                )
            )

    # Classes generation
    dataset = Dataset(
        product_name,
        dataset.longitude.data,
        dataset.latitude.data,
        measurements,
    )

    product = Product(
        product_name,
        product_description,
        measurements=measurements,
        storage_driver="NetCDF CF",
        storage_dimension_order=dims,
    )

    # YAML configuration
    yaml.emitter.Emitter.process_tag = lambda self, *args, **kw: None
    CWD = os.path.dirname(__file__)
    # Product generation
    with open(os.path.join(CWD, "./tests/product_generated.yaml"), "w") as f:
        yaml.dump(product, f, sort_keys=False)

    # Dataset generation
    data = yaml.dump(dataset, sort_keys=False)
    data = data.replace("'%", "")
    data = data.replace("%'", "")
    with open(os.path.join(CWD, "./tests/dataset_generated.yaml"), "w") as f:
        f.write(data)


generate_yaml_from_netCDF(
    "datasets/S5P_OFFL_L3__NO2____20200310T111355_20200310T125526_12472_01_010302_20200313T160857.nc",
    "sentinel5p",
    "Sentinel5P NetCDF with various layers",
    "NaN",
)
