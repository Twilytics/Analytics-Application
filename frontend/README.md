# Application for Running Grafana Locally  

This repository contains the environment for completing the tutorials at [grafana.com/tutorials](https://grafana.com/tutorials).

## Prequisites

You will need to have the following installed locally to complete this workshop:

- [Grafana](https://grafana.com/docs/grafana/latest/installation/)
- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

If you're running Docker for Desktop for macOS or Windows, Docker Compose is already included in your installation.

## Running

1. Clone the GitHub repository
2. Navigate into the frontend folder (which contains the docker-compose.yml)
3. Make sure Docker is running: $docker ps
4. Start the application: docker-compose up -d (for the first execution, all necessary resources for the app will be downloaded)
5. Ensure all services are up-and-running: docker-compose ps
6. Install the pie chat plugin via https://grafana.com/grafana/plugins/grafana-piechart-panel/installation
7. Browse the application via http://localhost:3000/login
8. Login into Grafana using: username (admin), password (admin)
9. Choose "Configuration" and then "Data Sources"
10. Select PostgreSQL database and SSL Mode = require
11. Ask repository creator for Host, Database, User, and Password
12. Choose dashboard and click on import
13. Import the dashboard from "frontend/app/twilytics_dashboard_importable.json" 
