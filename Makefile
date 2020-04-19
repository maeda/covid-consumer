freeze:
	pipenv lock --pre
	pipenv lock -r > requirements.txt

deploy: freeze
	gcloud functions deploy covid-consumer --runtime python37 --memory 256MB --entry-point run --trigger-http --allow-unauthenticated