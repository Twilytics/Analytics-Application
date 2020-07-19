# Dataproc
Data is pulled from MongoDB, the Trend indicators are calculated and then inserted into the PostgreSQL.

## Trend indicator
* Change rate
* Equality factor
* Trendsetter value

Find more information at the wiki https://github.com/Twilytics/Analytics-Application/wiki/Trend-indicators
## Create Dataproc

Mark the checkbox to use component-gateways
![grafik](https://user-images.githubusercontent.com/37565059/87877336-0ad6e680-c9de-11ea-99a9-23d2c2da1b9b.png)

Use Cloud Dataproc-Image-Version: 1.5 (Ubuntu 18.04 LTS, Hadoop 2.10, Spark 2.4) and install Anaconda and Jupyter 
![grafik](https://user-images.githubusercontent.com/37565059/87877371-3ce84880-c9de-11ea-9239-4648260aee32.png)

## Preperation

```
conda install pymongo
conda install dnspython
conda install psycopg2
```
