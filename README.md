
# Data Mining API

This repository provides a data mining toolbox designed for various data extraction and processing tasks. The project is containerized using Docker for easy deployment and management.

## Requirements

- Docker Desktop (Ensure it is installed and running)
- GNU Make (for managing commands)

## Setup and Usage

To start the application, navigate to the project directory and run:

```sh
make up
```

To stop the application, run:

```sh
make down
```

## Testing API Availability

To verify if the API is working, navigate to the `make` directory and execute the test file. If the output returns a `jobid`, the API is functioning correctly.

```sh
cd make
python test.py
```

If the `jobid` is returned, the API is successfully operational.

## Quickstart 
[Guide to Data Mining](https://alixf.ch/blog/guide-data-mining)  

The `make`  directory contains various tools gater information from websites. 

#### `main.py`
This script uses a list of urls in JSON format that will be acessed by the api and return data you enquire. Adjust the script to your needs by changeing the Xpaths. 
- by executing this file, while the api is running, you will submit jobs that return data the `make/data/` directory. 

## Contribution

Feel free to contribute by submitting pull requests or opening issues for feature requests and bug reports.

## Acknowledgment

This repository was created with the help of Jayden Pyles work 





