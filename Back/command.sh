deactivate
sudo service docker start
sudo python killprocess.py
docker-compose down
sleep 3
docker-compose up
