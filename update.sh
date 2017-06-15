#!/bin/sh

set -e

#git pull
docker build --tag=banking-prod .
docker rm -f banking
docker run -d --volumes-from home-data --link banking-db:db -v `pwd`/banking/banking/settings/production.py:/opt/code/banking/banking/settings/production.py --restart=always --name banking banking-prod

bash nginx.sh

echo "Cleaning up old docker images..."
docker rmi $(docker images | grep "<none>" | awk '{print($3)}')
