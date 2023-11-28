# Introduction

## Presto Workshop - Building an Open Data Lakehouse with Presto

Welcome to our workshop! In this workshop, you’ll learn the basics of Presto, the open-source SQL query engine, and it's support for Iceberg. You’ll get Presto running locally on your machine and connect to an S3-based data source and a Hive metastore (which enables our Iceberg support). This is a beginner-level workshop for software developers and engineers who are new to Presto and Iceberg. At the end of the workshop, you will understand how to integrate Presto with Iceberg and MinIO and how to understand the Iceberg table format.

The goals of this workshop are to show you:

* What is Apache Iceberg and how to use it
* How to connect Presto to MinIO s3 storage and a Hive metastore using Docker
* How to take advantage of Iceberg using Presto and why you would want to

### About this workshop

The introductory page of the workshop is broken down into the following sections:

* [Agenda](#agenda)
* [Compatibility](#compatibility)
* [Technology Used](#technology-used)
* [Credits](#credits)

## Agenda

|  |  |
| :--- | :--- |
| [Introduction](introduction/README.md) | Introduction to the technologies used |
| [Prerequisite](prerequisite/README.md) | Prerequisites for the workshop |
| [Lab 1: Set up an Open Lakehouse](lab-1/README.md) | Set up a Presto cluster with Hive metastore and data source connection |
| [Lab 2: Set up the Data Source](lab-2/README.md) | Set up a storage bucket in MinIO |
| [Lab 3: Exploring Iceberg Tables](lab-3/README.md) | Explore how to create Iceberg tables and use Iceberg features |

## Compatibility

This workshop has been tested on the following platforms:

* **Linux**: Ubuntu 22.04
* **MacOS**: M1 Mac

## Technology Used

* [Docker](https://www.docker.com/): A container engine to run several applications in self-contained containers.
* [Presto](https://prestodb.io/): A fast and Reliable SQL Engine for Data Analytics and the Open Lakehouse
* [Apache Iceberg](https://iceberg.apache.org/): A high-performance format for huge analytic tables
* [MinIO](https://min.io/): A high-performance, S3 compatible object store

## Credits

* [Kiersten Stokes](https://github.com/kiersten-stokes)
* [Yihong Wang](https://github.com/yhwang)
