
# Message Broker using RabbitMq

This project was carried out to fulfill one of the assignments for the Enterprise Application Integration course

## Build By

- [Bintang Anugrah Akbar](https://.github.com/bintangaakbar)
- [Safik Assegaf](https://github.com/safikassegaf)

## Deployment

To deploy this project run

```bash
  Download RabbitMq
  https://www.rabbitmq.com/download.html

  Download Erlang
  https://www.erlang.org/downloads
```

```bash
  Run command prompt and change directory to 'sbin' folder inside RabbitMq installation Folder
  
  Starting rabbitmq server
    run command 'rabbitmq-service start'
  
  then check the status
    run command 'rabbitmqctl status'
  
  Enabling Web Interface
    run command 'rabbitmq-plugins enable rabbitmq_management'
    default port is localhost:15672
    default username and password is 'guest' & 'guest'
```


## Run the project

Clone this repository

```bash
  use two different terminals to run the python file
  run the producer first
  then run the consumer
```
    
## Credit

[Our beloved professor website](https://ngodingdata.com/pengenalan-message-broker-dengan-rabbitmq/)


## Documentation

[Youtube Video](https://youtu.be/1hdo09v3f-4)

