
FROM python:3.8-slim-buster
COPY . /app/
WORKDIR /app

RUN pip3 install -r requirements.txt

ENV FLAG="securinets{F00LY_ID0R_Is_C00L}"
ENV PORT=5000 

# NOT TASK RELATED
ENV FLASK_SECRET_KEY="OVD8q3vaXLYFoPBJiDg45E0xQHqnnVJW"

EXPOSE 8080
CMD ["./run.sh"]

