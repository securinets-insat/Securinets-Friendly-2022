#!/bin/sh


# Here we will be spinning up multiple threads with multiple worker processess(-w) and perform a binding.
export FLAG="securinets{F00LY_ID0R_C00L}"
export PORT=5000

# NOT TASK RELATED
export FLASK_SECRET_KEY="OVD8q3vaXLYFoPBJiDg45E0xQHqnnVJW"


gunicorn wsgi:app --bind 0.0.0.0:8080 --log-level=debug --workers=4

