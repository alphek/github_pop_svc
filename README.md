# GITHUB_POP_SVC

This project provides an API to check the popularity of public GitHub repositories

---

## Assumptions and Further Improvements

- Used cache in front of GitHub api request to lower average response time and prevent possible DDOS attack
- I used 1 hour interval for cached(memcached) data and configured trough constants.py. But It can be given from
  external tool like Consul to provide more flexibility according to traffic
- It is better to create a class and instance For GitHub auth instead of just using variables
- I created a dummy GitHub account and used its access token in django settings for the sake of simplicity. Something
  like Consul or Vault can be used to make it more secure. I used dummy credentials and pushed them to Git
  repository.But We should not push any credentials in any coding.
- I did not implement exception handling to gain time. It needs better exception handling especially for the GitHub
  request part
- More tests like unit testing can be added
- This service has no logging and docker containers does not expose it logs to outside of container. Service needs
  better logging and monitoring
- Further statistics can be added to system status page(health_check)

---

## Tech Stack

- **Docker Compose** and **Docker** are used to containerize the project and make it easier for local development
- **Django (Python)** used to make it easier to build service (Rest framework, cache wrapper, settings, health-check)
- **Memcached** is used to lower average response time by not requesting data from GitHub for every single request
- **pytest** library used to create component tests
- **requests** library used to create an authenticated session and get requests to GitHub API's
- **drf-yasg** library used to implement automated API document creation over service by Swagger

---

## Useful Commands

- **Make build** >> to build docker compose
- **Make test** >> to run test cases (pytest)
- **Make start** >> to start and detach docker compose
- **Make stop** >> to stop docker compose
- **Make status** >> to check status of docker containers
- **Make clean** >> to clear up docker images
- **Make showmigrations** >> to check created Django migrations
- **Make makemigrations** >> to create new Django migrations if changes made
- **Make migrate** >> to make migrations did not make yet

---

## local urls

- **http://localhost:8000/github_pop/repos/<user_name>/<repository_name>/** (GitHub repository popularity check)
- **http://localhost:8000/health_check/** (system status)
- **http://localhost:8000/docs/swagger/** (api docs swagger)
- **http://localhost:8000/docs/redoc/**  (api docs redoc)
