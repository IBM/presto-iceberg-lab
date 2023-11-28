#!/bin/sh

export HADOOP_VERSION=3.2.0
export HADOOP_HOME=/opt/hadoop-$HADOOP_VERSION
export HADOOP_CLASSPATH=$HADOOP_HOME/share/hadoop/tools/lib/aws-java-sdk-bundle-1.11.375.jar:$HADOOP_HOME/share/hadoop/tools/lib/hadoop-aws-3.2.0.jar
export HIVE_AUX_JARS_PATH=$HADOOP_CLASSPATH
export JAVA_HOME=/usr/local/openjdk-8
export DB_HOSTNAME=${DB_HOSTNAME:-localhost}

echo "Waiting for MySQL database on ${DB_HOSTNAME} to launch..."
while ! nc -z $DB_HOSTNAME 3306; do
    sleep 1
done

echo "Starting Hive metastore service on $DB_HOSTNAME:3306"
/opt/apache-hive-metastore-3.0.0-bin/bin/schematool -initSchema -dbType mysql
/opt/apache-hive-metastore-3.0.0-bin/bin/start-metastore
