# FROM tools.standardbank.co.za:8093/cib-automation/python-oracle19c-base:1.0.0
FROM python:Latest

   
WORKDIR /usr/src/app

COPY . /usr/src/app/.
# RUN rm -rf /usr/src/app/db_scripts

#RUN pip install openapi-cli-tool
#RUN openapi-cli-tool bundle openapi3-spec.yaml -t html > ./static/index.html

EXPOSE 8080 5000

RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

RUN chmod 775 /usr/src/app/*

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
