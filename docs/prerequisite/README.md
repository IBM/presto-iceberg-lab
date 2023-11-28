# Prerequisite

This workshop uses [Docker](https://docs.docker.com/) to set up a Presto cluster, a local Hive metastore on top of a MySQL database, and a MinIO s3 object storage instance. It also uses [Docker Compose](https://docs.docker.com/compose/) to run them all together.

Please follow the installation links below to set up your working environment:

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/desktop/install/linux-install/)

## Clone the workshop repository

Various parts of this workshop will require the configuration files from the workshop repository. Use the following command to download the whole repository

```bash
git clone https://github.com/IBM/presto-iceberg-lab.git
cd presto-iceberg-lab
```

Alternatively, you can [download the repository as a zip file](https://codeload.github.com/IBM/presto-iceberg-lab/zip/refs/heads/main), unzip it and change into the `presto-iceberg-lab-main` directory.
