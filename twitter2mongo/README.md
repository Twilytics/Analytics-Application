# Twitter to MongoDB
## Describtion
This python script is responsible to call the TwitterAPI and insert the data into MongoDB for further processing

## Execution
The twitter2mongo script is executed by a cron job
```
0 * * * * python3 /path/twitter2mongo.py
```
If you want to change the cron schedule expressions check [crontab guru](https://crontab.guru/ "crontab guru"). It is also possible to run the script by 
```
python3 twitter2mongo.py
```
