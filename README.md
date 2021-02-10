# Geographic Information Systems

<p align="center">
<img src="https://github.com/samuelexferri/unibg-gis/blob/master/images/datacube.png" width="200">
</p>

Geographic Information Systems project

Creation of an Open Data Cube and analysis of pollutant emissions in Lombardy

**Note:** Follow the documentation for all the information, in this file there will be only the part relating to the installation of the Open Data Cube.

[Open Data Cube](https://www.opendatacube.org/overview)

![alt text](https://img.shields.io/badge/Language-Italian-infomrmational?style=for-the-badge)

## Installation

Follow the documentation [Open Data Cube Documentation (Installation)](https://datacube-core.readthedocs.io/en/latest/ops/install.html)

### Requirements

Python v3.8.6

-   Create new virtual environment:
    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```
-   Install requirements (some `.whl` files):
    ```bash
    pip install -r requirements.txt
    ```
-   Install Jupyter notebooks:
    ```bash
    pip install jupyter
    jupyter notebook
    ```

### Database setup

-   Install [PostgreSQL](https://www.postgresql.org/download/)

-   Add PostgreSQL to the system environment variables (Path):

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

Get `datacube-core-develop` from [here](https://github.com/opendatacube/datacube-core).

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

We are using `dataset.nc` NetCDF file with HARP conventions.

**Note:** Dataset used are not in the repository due to big size!

We need to create two `.yaml` files in order to define the product and add the dataset data in Open Data Cube.

#### Product YAML

We create a `product.yaml` file in order to define the product in Open Data Cube.

-   Add product `product.yaml` to datacube:

    ```bash
    datacube product add product.yaml
    ```

#### Dataset YAML

We are using `Dataset.ipynb` jupyter notebook.

We had to specify all the required parameters by the [EO3 convention](https://datacube-core.readthedocs.io/en/latest/ops/dataset_documents.html), extrapolating them from the NetCDF.

Dataset metadata documents define critical metadata about a dataset including:

-   Available data measurements
-   Platform and sensor names
-   Geospatial extents and projection
-   Acquisition time
-   Provenance information

We analyze our Sentinel5P dataset `dataset.nc` and create the `dataset.yaml` file.

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

### Automated YAML Script

If the data have already been prepared from the source for inclusion in the Open Data Cube project, they can be imported into the database without further steps, as they will already be packaged with *dataset* and *product* documents compatible with ODC and will therefore already be ready for immediate indexing.

If, on the other hand, the data is from external or incompatible sources, it will be necessary to generate these *dataset* and *product* documents by hand. This is what we did for the first import of the data into the Data Cube. We then created a so-called "Data Preparation Script", that is a python script that reads the metadata format of the input file and automatically generates the *dataset* and *product* documents required for import.

### Analysis

See the full docs!

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
