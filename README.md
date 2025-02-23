
# Python-Docker-K8s-Project

I. Developed a Python-based web application using the Flask framework.

II. Containerized the application using Docker and published the image to DockerHub.

III. Deployed the application using Kubernetes manifest files and accessed it via a web interface.

IV. Uploaded the project code to GitHub for version control and collaboration.

### Below are the step-by-step commands followed during the implementation.


## -- Docker --

### Containerize the python application:

#### 1. Build docker image:
```bash
    docker build -t python-app .
```

#### 2. Run container:
```bash
	docker run -d -p 5000:5000 my-python-app
```

#### 3. Show images:
```bash
	docker images
```

#### 4. Show containers (including stopped):
```bash
	docker ps -a
```

### DockerHub

#### Upload the built image to docker Hub:
#### a. First login to docker hub:
```bash
	docker login -u rajeev3012
```

#### b. Tag the image with your docker hub username:
```bash
	docker tag my-python-app rajeev3012/python-app
```

#### c. Push
```bash
	docker push rajeev3012/python-app
```


### Cleanup:

#### 1. Stop running container:
```bash
	docker stop <container>
```
	
#### 2. Remove container:
```bash
	docker rm <container>
```
	
#### 3. Remove image:
```bash
	docker rmi <image>
```


## -- Kubernetes --

### 1. Deploy resources:
```bash
	kubectl apply -f deployment.yaml
	kubectl apply -f service.yaml
```

### 2. Show deployed resources:
```bash
	kubectl get all
	kubectl get pods
```

### 3. Access the app:
```bash
	minikube service python-app-service
```

### 4. Delete
```bash
	kubectl delete all --all
	kubectl delete pods -l app=python-app    (-l: label containing "python-app")
	kubectl delete pod python-app-123 --grace-period=0 --force    (force delete)
```


## -- GitHub --

### 1. Initialize git: 
```bash
	git init 
```
### 2. Create and checkout to main branch (by default it may be master): 
```bash
	git checkout -b main 
```
### 3. Check files: 
```bash
	git status 
```
###	4. Add to staging area: 
```bash
	git add . 
```
###	5. Add commit with message: 
```bash
	git commit -am "initial commit" 
```
###	6. Add GitHub remote repo: 
```bash
	git remote add origin https://github.com/rajeev3012/python-docker-k8s-project.git 
```
###	7. Fetch and merge latest change to local first: 
```bash
	git pull origin main --rebase 
```
###	8. Finally push changes to remote repo: 
```bash
	git push -u origin main 
```

