#!/bin/sh

set -e

git pull
docker build --tag=banking-prod .
docker rm -f banking
docker run -d --volumes-from banking-data --link banking-db:db -v `pwd`/banking/banking/settings/production.py:/opt/code/banking/banking/settings/production.py --restart=always --name banking banking-prod
docker rm -f banking-nginx
docker run --name banking-nginx --net="host" --volumes-from banking-data -p 80:80 -v `pwd`/nginx.conf:/etc/nginx/nginx.conf --restart=always -d nginx

echo "Cleaning up old docker images..."
docker rmi $(docker images | grep "<none>" | awk '{print($3)}')
