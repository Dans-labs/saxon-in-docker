# saxon-in-docker

This docker setup together with `run.py` will convert the EASY social science XML to properly mapped json files for 
Dataverse to ingest. 

### Start the docker container
`docker compose up -d`

### copy the python script to container
`docker cp run.py saxon-in-docker_1:/root/run.py`

### Go into the container
`docker exec -e COLUMNS="`tput cols`" -e LINES="`tput lines`" -it saxon-in-docker_1 /bin/bash -l`

### run the script
`cd /root && python3 run.py`

#### Note 1
Please be patient, it will take 1 to 2 hours

#### Note 2
Both python 2 and 3 is available in the container, please explicitly use `python3` when invoking the script. 
