# Kedro POC

Kedro official docs: https://kedro.readthedocs.io/

## Project Setup

1. Create conda environment and activate
1. Install `kedro`
1. `kedro new`
    1. You may want to put the `/env` inside the project folder, which is created with `kedro new`. 
    If so, you may need to
        1. Install `kedro` in another env (may be `base`)
        1. Run `kedro new`
        1. Go to project folder, create env and install `kedro` again
1. Go to the project folder (same folder with `kedro_cli.py`)
1. Add the packages you need to `<project_folder>/requirements.txt`
1. Run `kedro install`
    1. For Windows users, it is important to have `kedro` installed before running `kedro install`! Otherwise all packages will be installed to `base` env.
    1. For Linux/Mac users, not tested yet.
1. For the use of AWS S3 / MinIO, `s3fs<=0.4.2` should be installed.