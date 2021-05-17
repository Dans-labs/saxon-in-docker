# saxon-in-docker

This docker setup together with `run.py` will convert the EASY social science XML to properly mapped json files for 
Dataverse to ingest. 

## Step 2 to use the setup
### configuration in .env file
```python
xml_path="absolute path to the directory which contains all xml files"
xsl_path="/absolute-path-to/to-json.xsl"
output_path="/absolute-path-to/output_path"
```
 * `xml_path` should point to a local folder on the host 
 * `xsl_path` should point to a local file on the host
 * `output_path` should point to a local folder on the host

All the 3 paths will be mounted to the container. The end result json files will be put in the `output-path` on host. 

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
