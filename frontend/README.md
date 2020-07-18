# Application for Running Grafana Locally  

This repository contains the environment for completing the tutorials at [grafana.com/tutorials](https://grafana.com/tutorials).

## Prequisites

You will need to have the following installed locally to complete this workshop:

- [Grafana](https://grafana.com/docs/grafana/latest/installation/)
- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

If you're running Docker for Desktop for macOS or Windows, Docker Compose is already included in your installation.

## Running

1. Make sure Docker is running: $docker ps
2. Navigate into the folder with the docker-compose.yml
3. Start the application: docker-compose up -d (for the first execution, all necessary resources for the app will be downloaded)
4. Ensure all services are up-and-running: docker-compose ps
5. Install the pie chat plugin via https://grafana.com/grafana/plugins/grafana-piechart-panel/installation
6. Browse the application via http://localhost:3000/login
7. Login into Grafana using: username (admin), password (admin)
8. Choose "Configuration" and then "Data Sources"
9. Select PostgreSQL database and SSL Mode = require
10. Ask repository creator for Host, Database, User, and Password
11. Choose dashboard and click on import
12. Import the dashboard from "frontend/app/twilytics_dashboard_importable.json" 
