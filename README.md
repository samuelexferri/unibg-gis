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

-   Create new environment
    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```
-   Install requirements
    ```bash
    pip install -r requirements.txt
    ```
-   Install Jupyter Notebooks
    ```bash
    pip install jupyter
    ```

### Database setup

-   Install [PostgreSQL](https://www.postgresql.org/download/)

-   Add to environment variables


    C:\Program Files\PostgreSQL\13\bin
    C:\Program Files\PostgreSQL\13\lib

-   Create database

    ```bash
    psql -U postgres
    > CREATE DATABASE datacube;
    ```

-   Create configuration file in `~/.datacube.conf`

    ```toml
    [datacube]
    db_database: datacube

    # A blank host will use a local socket. Specify a hostname (such as localhost) to use TCP.
    db_hostname: localhost

    # Credentials are optional: you might have other Postgres authentication configured.
    # The default username otherwise is the current user id.
    db_username: datacube
    db_password: 0
    ```

### Datacube installation

-   Install datacube

    ```bash
    cd datacube-core-develop
    python setup.py install
    ```

-   Check datacube version

    ```bash
    pip install numpy==1.19.3
    datacube --version
    ```

-   Initialize database schema

    ```bash
    datacube -v system init
    ```

### Dataset USGS

Download data from the example in the docs:

-   Go to <https://earthexplorer.usgs.gov/>

-   Select "Landsat 8 OLI/TIRS C1 Level-1" data set

      ![](images/download-1.jpg)

-   Click on the download icon for the first data piece

      ![](images/download-2.jpg)

-   Download the necessary files

      ![](images/download-3.jpg)

-   Rename `LC08_L1TP_097011_20201101_20201106_01_T2_MTL.txt` in `MTL.txt`

-   Prepare the dataset with `ls_usgs_prepare.py` and rename the output file with extension `ls8_usgs_lv1.yaml`

    ```bash
    python ls_usgs_prepare.py --output ls8_usgs_lv1 C:\Users\samuelexferri\Desktop\ODC\LC08_L1TP_097011_20201101_20201106_01_T2a
    ```

-   Add product `ls_usgs_level1_scene.yaml` to datacube (THIS YAML MUST BE SEARCHED ON INTERNET)

    ```bash
    datacube product add ls_usgs_level1_scene.yaml
    ```

-   Add dataset `ls8_usgs_lv1.yaml` to datacube

    ```bash
    datacube dataset add --auto-match ls8_usgs_lv1.yaml
    ```

### Dataset Sentinel5P (NetCDF)

We are using `S5P_OFFL_L3__NO2____20200310T111355_20200310T125526_12472_01_010302_20200313T160857.nc` NetCDF file.
We need to develop a script with two `.yaml` output files in order to define the product and add the dataset data in the Open Data Cube.

TODO

### Other

-   Jupyter Notebook

```bash
jupyter notebook
```

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
