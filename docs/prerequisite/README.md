# Prerequisite

This workshop uses the [Docker](https://docs.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) CLI tools to set up a Presto cluster, a local Hive metastore on top of a MySQL database, and a MinIO s3 object storage instance. We recommend [Podman](https://podman.io/), which is a rootless - and hence more secure - drop-in replacement for Docker. [Install Podman](https://podman.io/docs/installation) and ensure that `podman` has been successfully `alias`'ed to `docker` in your working environment.

## Clone the workshop repository

Various parts of this workshop will require the configuration files from the workshop repository. Use the following command to download the whole repository:

```bash
git clone https://github.com/IBM/presto-iceberg-lab.git
cd presto-iceberg-lab
```

Alternatively, you can [download the repository as a zip file](https://codeload.github.com/IBM/presto-iceberg-lab/zip/refs/heads/main), unzip it and change into the `presto-iceberg-lab` main directory.
