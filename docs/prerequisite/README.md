# Prerequisite

This workshop uses the [Docker](https://docs.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) CLI tools to set up a Presto cluster, a local REST server on top of a PostgreSQL database, and a MinIO s3 object storage instance. We recommend [Podman](https://podman.io/), which is a rootless - and hence more secure - drop-in replacement for Docker. [Install Podman](https://podman.io/docs/installation) and ensure that `podman` has been successfully `alias`'ed to `docker` in your working environment.

## Access your environment

Follow this link to get assinged to a virtual environment. You will need to [have an IBMid](https://urldefense.proofpoint.com/v2/url?u=https-3A__u8160902.ct.sendgrid.net_ls_click-3Fupn-3Du001.WEgFBoj4nWPI2JVlMtlISVaUWb-2D2BKVVRyzKGz4-2D2Fk-2D2BN5gX-2D2Bzbzzuj7knp-2D2BRrBtADnUCKfKzQZMR795EP0qc-2D2BqNMEeXHDUkbIDUbuhAr79fPybqvB1-2D2BwK5D-2D2BGY-2D2FjrblXATO3zDjzELtGvt2mnxmUDfZhzRpe1UzPJ9oWMbsScfMgAiN2cCSzJBW2q3wKQWCTYcvggG70bwHIJNAwLlw2qvmGy7QUV4lz7QxjeuTsXGcQ2zJbdqVO8iEWIkwyEKJVlztaEx-2D2BbOy9NdEtPOrrcVxZGsE0vbOg7ZmofVOIJw-2D2Bi-2D2FUZrkhNv8ZNLbfB5Maega10QcFOd-5F2KNIHf68nrNXZBhbSjT32rtBn8AcSdShM0OFmJCOy-2D2F8mM8KLPVzgoIryCNce9eHb5GAB-2D2FmZxYqUGZQrkV4vr4iiHE5q9m0R5zIZ0xhwrjTZsZk9CpnhbQdF9IHndzCHaGopV4L-2D2Fh3yaQBXhiTw1YmAJFFfk9I906QeRXULRR3gfpEsFKvRUgXDB77xOQKUGntFzlkb-2D2FDi80zmnLU-2D2Bv1DQ37IjLJUfJUd-2D2F3woNREwuju0k5eDkEdg11omP9xazHVGD2n3PNzgYwCMYq7xySb9jnLjM-2D2FU-2D2BIiER5pK2LwF4ctNL34IVShdZfbjSJXZ-2D2FT-2D2FKnEFgsY7Ee1-2D2B0sXHsucf6A0GgSPwV6wSenvCt5YF8PWB80mnsMiGIaAXgPLjDM8h7rBiYGnaDg2vK3uIOtgytMkg-2D3D-2D3D&d=DwMFAg&c=BSDicqBQBDjDI9RkVyTcHQ&r=dIs2381eqVWuNGLqb7ZQ673HFdGQmASi_gH1hQrYTAo&m=T2uF0fYsP5fo-n_b3Z7XO-n-S3wSbm4riV_qoZzc6ogopcUw6yk0637bgFFbOsIX&s=2C6Qc0g6ia89JzvkqhiFUYSwiGQDxWw5MQmV3El0Ha4&e=) to do so.

The password for this lab is `iceberg`.

You will need to download your ssh key from the environment page. Place the file somewhere easy for you to access. Then, open a terminal and change the permissions for the file:

```bash
chmod 600 <PATH_TO_FILE>/pem_ibmcloudvsi_download.pem
```

Now you can log into the environment. Plug in the noted options with the information for your environment.

```bash
ssh –i <PATH_TO_FILE>/pem_ibmcloudvsi_download.pem itzuser@<PUBLIC_IP> -p 2223
```

Once you are logged into your environment, run the following command:

```bash
cd presto-iceberg-lab/conf
```

## Clone the workshop repository

Various parts of this workshop will require the configuration files from the workshop repository. Use the following command to download the whole repository:

```bash
git clone https://github.com/IBM/presto-iceberg-lab.git
cd presto-iceberg-lab
```

Alternatively, you can [download the repository as a zip file](https://codeload.github.com/IBM/presto-iceberg-lab/zip/refs/heads/main), unzip it and change into the `presto-iceberg-lab` main directory.
