# Geographic Information Systems

<p align="center">
<img src="https://github.com/samuelexferri/unibg-gis/blob/master/images/datacube.png" width="200">
</p>

Geographic Information Systems project

![alt text](https://img.shields.io/badge/Language-Italian-infomrmational?style=for-the-badge)

## Installation

### Requirements

-   Create new environment
    ```bash
    virtualenv env
    ```
-   Install requirements
    ```bash
    pip install -r requirements.txt
    ```

### Database setup

-   Install PostgreSQL
-   Create database
    ```bash
    psql -U postgres
    > create database datacube;
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
        db_password: XXX
        ```

### Datacube installation

-   Install datacube

    ```bash
    cd datacube-core-develop
    python setup.py install
    ```

-   Initialize database schema

    ```bash
    datacube -v system init
    ```

### Dataset

Download data from the example in the docs:

-   Go to <https://earthexplorer.usgs.gov/>

-   Select "Landsat 8 OLI/TIRS C1 Level-1" data set

      ![](images/download-1.jpg)

-   Click on the download icon for the first data piece

      ![](images/download-2.jpg)

-   Download the necessary files

      ![](images/download-3.jpg)

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
