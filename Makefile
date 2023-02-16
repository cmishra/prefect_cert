
build-102:
	prefect deployment build -ib docker-container/docker --name=lab102_do_analysis lab102:do_analysis

push-102:
	prefect deployment apply do_analysis-deployment.yaml

build-image:
	docker build -f Dockerfile -t prefect .
	docker tag prefect us.gcr.io/chetanmishra/prefect

push-image:
	docker push us.gcr.io/chetanmishra/prefect

deploy-k8:
	kubectl apply -f k8-yamls 

# google how to install this
cloud-sql-proxy:
	./cloud-sql-proxy --address 0.0.0.0 --port 1234 chetanmishra:us-central1:mini-postgres -g

# Yes the password is exposed below but no incoming connections are approved so you won't be able to use it =)
start-local-orion:
	PREFECT_ORION_DATABASE_CONNECTION_URL=postgresql+asyncpg://postgres:aonsetutaoeuaeo778237827683haoe@0.0.0.0:1234/postgres prefect orion start

# TODO - never quite got GKE+cloud sql working