
build-102:
	prefect deployment build -ib docker-container/docker --name=lab102_do_analysis lab102:do_analysis

push-102:
	prefect deployment apply do_analysis-deployment.yaml

build-image:
	docker build -t prefect .

push-image:
	docker tag prefect us.gcr.io/chetanmishra/prefect
	docker push us.gcr.io/chetanmishra/prefect