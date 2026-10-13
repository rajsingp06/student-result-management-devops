# Student Result Management System — DevOps Practical Kit

A small Flask API for a two-hour Third Year Engineering DevOps practical. It demonstrates PyTest, GitHub Actions CI, SonarQube analysis, and Docker.

## Features
- Student marks, total, percentage, and PASS/FAIL status.
- Unknown roll number returns HTTP 404.
- `/health` endpoint for deployment checks.
- Automated PyTest cases.
- GitHub Actions workflow for tests, SonarQube scan, Docker build, and smoke tests.
- Docker container runs as a non-root user.

## 1. Prerequisites
Install Python 3.12, Git, Docker Desktop, and VS Code. A reachable SonarQube server and token are needed for the SonarQube CI job.

## 2. Run locally

### Windows PowerShell
Run these commands in the project folder:
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -v
python app.py
```
If activation is blocked, use Command Prompt and run `.venv\Scripts\activate.bat`.

### macOS / Linux
```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -v
python app.py
```
Keep the terminal running. Open:
- Home: http://127.0.0.1:5000/
- Roll 101: http://127.0.0.1:5000/results/101
- Roll 102: http://127.0.0.1:5000/results/102
- Roll 103: http://127.0.0.1:5000/results/103
- Unknown roll (404): http://127.0.0.1:5000/results/999
- Health: http://127.0.0.1:5000/health

Stop Flask with Ctrl+C.

## 3. Expected sample results
Each student has three subjects out of 100. Passing requires at least 35 in every subject.
- Roll 101: 234/300 = 78.0%, PASS
- Roll 102: 274/300 = 91.33%, PASS
- Roll 103: 101/300 = 33.67%, FAIL

## 4. Docker build and run
Ensure Docker Desktop is running:
```bash
docker build -t student-result-management:1.0 .
docker run -d --name result-app -p 5000:5000 student-result-management:1.0
```
Verify http://127.0.0.1:5000/health and http://127.0.0.1:5000/results/101. View logs with `docker logs result-app`. Stop and remove with:
```bash
docker stop result-app
docker rm result-app
```
If port 5000 is busy, use `-p 5001:5000` and open port 5001.

## 5. Push to GitHub
1. Create an empty GitHub repository named `student-result-management`.
2. In the VS Code terminal, run:
```bash
git init
git add .
git commit -m "Add Student Result Management DevOps project"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```
Replace `YOUR_REPOSITORY_URL` with the URL of your own repository. Then open the repository's **Actions** tab to view the workflow.

## 6. Configure SonarQube
In GitHub, open **Settings → Secrets and variables → Actions**:
1. Add repository secret `SONAR_TOKEN` with your analysis token.
2. Add repository variable `SONAR_HOST_URL` with the SonarQube base URL, e.g. `https://sonarqube.example.edu`.
3. Ensure project key `student-result-management` exists or the token can create/analyze it.
4. Push a commit or re-run the workflow.

Important: GitHub-hosted runners cannot reach a SonarQube instance available only at `localhost` or on a private college network. Use a reachable server or a self-hosted runner in that network. Without a valid server/token, the SonarQube job will fail, but local Flask, tests, and Docker can still work. Never commit tokens.

## 7. Verify CI
In GitHub **Actions**, open the latest `DevOps CI` run:
- PyTest should pass all tests.
- SonarQube analysis should complete if configured correctly.
- Docker job builds the image, starts a container, and checks `/health`, `/results/101`, and the 404 response for `/results/999`.

The CI container is temporary; this workflow does not create a permanent public deployment.

## 8. Troubleshooting
- `pytest` not found: activate `.venv`, then install requirements.
- `python` not found on Windows: try `py -3.12`.
- Docker daemon error: start Docker Desktop.
- Port already allocated: map host port 5001 to container port 5000.
- SonarQube fails: check token, URL, project permissions, and network access.
- Git push rejected: verify the repository URL and whether the remote already has commits.

## Suggested practical evidence
Capture screenshots of passing `pytest -v`, the `/results/101` endpoint, `docker ps`, successful GitHub Actions jobs, and the SonarQube dashboard.

## Viva quick revision
- **Flask:** Python framework for HTTP endpoints.
- **PyTest:** Runs automated tests.
- **CI:** Automatically tests code on pushes and pull requests.
- **Docker image:** Packaged application and dependencies.
- **Container:** Running instance of an image.
- **SonarQube:** Analyzes code quality and reports issues.
- **HTTP 404:** Resource not found.
- **Health check:** Endpoint to confirm the app responds.
- **Non-root container:** Runs as a normal user, not root.
