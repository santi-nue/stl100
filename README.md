# Binder Template for Launching Streamlit Apps

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml-starter-packs/binder-streamlit/main?urlpath=app/)

# Instructions
1. Use as template.
1. Modify `postBuild` to point to your app.
1. Modify `Dockerfile` if needed.



## Running with Docker (locally)
This project was set up to work with both mybinder.org and a local docker build which will launch `streamlit` by default.
To use it, run

```bash
docker build -t streamlit-demo .
docker run --rm -ti --name demo-env -p 8501:8501 streamlit-demo
```

or using `docker-compose.yml`:
```bash
version: "3"

services:
  demo:
    container_name: demo-env
    image: streamlit-demo
    build:
      dockerfile: Dockerfile
      context: .
    ports:
      - "8501:8501"
    command: streamlit run app.py --server.address 0.0.0.0 --server.port 8501 --server.enableCORS False --server.enableXsrfProtection False
 ```


## A Note on Reproducibility
To ensure future reproducibility, it is advised to pin the requirements in `postBuild` and `requirements.txt` to exact package versions.
The core dependencies to function with binder.org evolve (slowly) over time, and so they have been left unpinned here.
