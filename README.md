# Twilytics Analytics

This project was developed for the course "Data Engineering Project - Building real time data pipelines" of [Prof. Dr. David Klotz](mailto:david.klotz@hdm-stuttgart.de?subject=[GitHub]Twilytics) at the Stuttgart Media University. The data pipeline was developed by [Alexander Stahl](mailto:as291@hdm-stuttgart.de?subject=[GitHub]Twilytics) and [Johannes Ströbele](mailto:js349@hdm-stuttgart.de?subject=[GitHub]Twilytics).

The Twilytics dashboard provides insights into the trends on Twitter based on real time data. Users can get informations, for example, about how trends change on Twitter in a respective city or how the trends between cities correlate. For this samll university project, the cities Stuttgart and Berlin were analyzed.  

## Repository Structure
_This is the file structure of the project's repository:_
- dataproc: PySpark script for getting raw data from the MongoDB, processing Twitter data distributively, and inserting it into the PostgreSQL database
- frontend: Grafana dashboard that can be run locally (access to the database can be requested from Alexander Stahl](mailto:as291@hdm-stuttgart.de?subject=[GitHub]Twilytics) or [Johannes Ströbele](mailto:js349@hdm-stuttgart.de?subject=[GitHub]Twilytics)
- twitter2mongo: Python script for requesting raw Twitter data and inserting it into MongoDB
- .gitignore
- LICENSE
- README.md

## Software Architecture
https://user-images.githubusercontent.com/37565059/87839853-f0492400-c89c-11ea-9c5d-a31db556a015.png
1. Data source: REST API Twitter
2. VM "twitter2mongo" hosted on Google Cloud Compute Engine: Python script requests raw Twitter data and inserts it into MongoDB 
3. MongoDB hosted on AWS: stores raw Twitter data
4. VM "twilytics-spark" hosted on Google Cloud Compute Engine: Pyspark script requests the raw Twitter data from the MongoDB, analyzes it distributively via Apache Spark (PySpark), and inserts it into the PostgreSQL
5. PostgreSQL hosted on Google Cloud SQL: stores raw Twitter data
6. VM "grafana" hosted on Google Cloud Compute Engine: gets the processed data from the PostgreSQL and creates with it a dashboard
7. Users can access the Grafana dashboard: [https://twilytics.com](https://34.90.204.132:3000/d/3tEWWEnMk/twilytics?from=1565975319000&orgId=1&to=1626463178000 (username: test-user, password: test-user))

## Lessons Learned
_Are more detailed list can be found [here](https://github.com/Twilytics/Analytics-Application/wiki/Lessons-Learned)_
* [Grafana](https://grafana.com/) was chosen for building the dashboard due to its ease of use and fast setup (compared to [Dash](https://plotly.com/dash/) and [MEAN](https://en.wikipedia.org/wiki/MEAN_(solution_stack)))
* Google Cloud HTTPS Configuration was not setup due to costs (a domain would have needed to be purchased) 

## Contact
- [Alexander Stahl](mailto:as291@hdm-stuttgart.de?subject=[GitHub]Twilytics)
- [Johannes Ströbele](mailto:js349@hdm-stuttgart.de?subject=[GitHub]Twilytics)

## License

MIT License - Copyright 2020 ©
