# Geographic Information Systems

<p align="center">
<img src="https://github.com/samuelexferri/unibg-gis/blob/master/images/datacube.png" width="200">
</p>

Geographic Information Systems project

[Open Data Cube](https://www.opendatacube.org/overview)

![alt text](https://img.shields.io/badge/Language-Italian-infomrmational?style=for-the-badge)

## Installation

[Open Data Cube Documentation (Installation)](https://datacube-core.readthedocs.io/en/latest/ops/install.html)

### Requirements

-   Create new virtual environment:
    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```
-   Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
-   Install Jupyter Notebooks:
    ```bash
    pip install jupyter
    ```

### Database setup

-   Install [PostgreSQL](https://www.postgresql.org/download/)

-   Add PostgreSQL to environment variables:

    ```bash
    C:\Program Files\PostgreSQL\13\bin
    C:\Program Files\PostgreSQL\13\lib
    ```

-   Create database:

    ```bash
    psql -U postgres
    > CREATE DATABASE datacube;
    ```

-   Create configuration file in `~/.datacube.conf`:

        [datacube]
        db_database: datacube

        # A blank host will use a local socket. Specify a hostname (such as localhost) to use TCP.
        db_hostname: localhost

        # Credentials are optional: you might have other Postgres authentication configured.
        # The default username otherwise is the current user id.
        db_username: datacube
        db_password: 0

### Datacube installation

-   Install datacube:

    ```bash
    cd datacube-core-develop
    python setup.py install
    ```

-   Check datacube version:

    ```bash
    datacube --version
    ```

-   In case of errors with `numpy`, maybe this can resolve:

    ```bash
    pip install numpy==1.19.3
    ```

-   Initialize database schema:

    ```bash
    datacube -v system init
    ```

### Dataset Sentinel5P (NetCDF)

We are using `S5P_OFFL_L3__NO2____20200310T111355_20200310T125526_12472_01_010302_20200313T160857.nc` (or `dataset.nc`) NetCDF file with HARP conventions.

We need to create two `.yaml` files in order to define the product and add the dataset data in Open Data Cube.

#### Product YAML

We create a `product.yaml` file in order to define the product in Open Data Cube.

-   Add product `product.yaml` to datacube:

    ```bash
    datacube product add product.yaml
    ```

#### ~~Dataset YAML (Test)~~

We are using `Dataset (Test).ipynb` jupyter notebook.

Initially we analyze a test dataset `dataset pr_wtr.eatm.2018.test.nc` from [GeoscienceAustralia (EO Datasets)](https://github.com/GeoscienceAustralia/eo-datasets).

-   Install prerequisites:

    ```bash
     pip install eodatasets3 deepdiff ciso8601
     pip install eodatasets3 --no-deps
    ```

-   Run the main script that generate `pr_wtr.eatm.2018.test.ga-md.yaml`

-   In case of errors with `shapely`, maybe this can resolve:

    ```bash
    pip uninstall shapely
    pip install C:\GitHub\unibg-gis\whls\Shapely-1.7.1-cp38-cp38-win_amd64.whl
    ```

    or

    ```bash
    from shapely import speedups
    speedups.disable()
    ```

-   We halved the documents dataset and saved in `pr_wtr.eatm.2018.test.ga-md_dimezzato.yaml`

-   Validate `pr_wtr.eatm.2018.test.ga-md_dimezzato.yaml` (Option `--thorough` -> Attempt to read the data/measurements, and check their properties match the product):

    ```bash
    eo3-validate "pr_wtr.eatm.2018.test.ga-md_dimezzato.yaml"
    eo3-validate --thorough "pr_wtr.eatm.2018.test.ga-md_dimezzato.yaml"
    ```

Now we have a `pr_wtr.eatm.2018.test.ga-md_dimezzato.yaml` file as basepoint to build our `dataset.yaml`.

**TODO**

```bash
# FILE product.yaml

# TODO

# HARP Conventions (Datetime, Indipendent)
```

#### Dataset YAML

We are using `Dataset.ipynb` jupyter notebook.

We had to specify all the required parameters (extrapolating them from the NetCDF) by the EO3 convention.

Dataset metadata documents define critical metadata about a dataset including:

-   Available data measurements
-   Platform and sensor names
-   Geospatial extents and projection
-   Acquisition time
-   Provenance information

We analyze our Sentinel5P dataset `S5P_OFFL_L3__NO2____20200310T111355_20200310T125526_12472_01_010302_20200313T160857.nc` (or `dataset.nc`) and create the `dataset.yaml` file.

-   Validate `dataset.yaml` (Option `--thorough` -> Attempt to read the data/measurements, and check their properties match the product):

    ```bash
    eo3-validate "dataset.yaml"
    eo3-validate --thorough "dataset.yaml"
    ```

-   Add dataset `dataset.yaml` to datacube:

    ```bash
    datacube dataset add --auto-match dataset.yaml
    ```

-   In case of errors with `shapely`, maybe this can resolve:

    ```bash
    pip uninstall shapely
    pip install C:\GitHub\unibg-gis\whls\Shapely-1.7.1-cp38-cp38-win_amd64.whl
    ```

    or

    ```bash
    from shapely import speedups
    speedups.disable()
    ```

-   In case of errors with `sqlalchemy`, maybe this can resolve:

    ```bash
    pip install sqlalchemy==1.3.20
    ```

**TODO**

```bash
# FILE dataset.yaml

# $schema -> OK
# id (UUID) -> CASO
# product -> OK
# crs -> CASO
# geometry -> CASO
# grids -> FORSE
# lineage -> OK (Vuoto)
# measurements -> AGGIUNGERE
# properties -> CASO

# HARP Conventions (Datetime, Indipendent)
```

### Analysis

We are using `Analysis.ipynb` jupyter notebook.

**TODO**

### Other

-   Jupyter Notebook

    ```bash
    jupyter notebook
    ```

**REMOVE**:  `pr_wtr.eatm.2018.test.ga-md.yaml` (Files, Guide)

## Authors

### Team

-   **Samuele Ferri**: [Site](https://samuelexferri.com), [GitHub](https://github.com/samuelexferri)
-   **Lorenzo Conti**
-   **Fabio Sangregorio**
-   **Simone Sudati**

## Version

![alt text](https://img.shields.io/badge/Version-0.0.1-blue.svg?style=for-the-badge)

## License

[![License](https://img.shields.io/badge/License-MIT_License-blue.svg?style=for-the-badge)](https://badges.mit-license.org)
