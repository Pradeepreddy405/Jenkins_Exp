## my-app/
  │
  ├── Jenkinsfile
  ├── config/
  │   ├── dev.yaml
  │   ├── staging.yaml
  │   └── prod.yaml


## config/dev.yaml
   app_name: my-service
   server: dev.example.com
   replicas: 1
   deploy_cmd: "echo Deploying to DEV"

## config/prod.yaml
   app_name: my-service
   server: prod.example.com
   replicas: 5
   deploy_cmd: "echo Deploying to PROD"

## config/stag.yaml
   app_name: my-service
   server: stag.example.com
   replicas: 5
   deploy_cmd: "echo Deploying to STAG"
