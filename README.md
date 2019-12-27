# Updater
A remote updater accessible via a browser

## How to build locally:
This install guide assumes you have docker and git installed and configured
1. Clone this repo
```
git clone https://www.github.com/highsaltlevels/Updater
```
2. Start up the docker daemon (if it is not already running)
```
sudo systemctl daemon-reload
sudo systemctl start docker.service
```
3. Build the docker image
```
docker build -t updater .
```
**Note**: If you need to work around a proxy, you'll want to include your proxy as build-args
```
docker build -t updater --build-arg HTTPS_PROXY=<Your Proxy> HTTP_PROXY=<Your Proxy> NO_PROXY="*"
```
4. Run the image
```
docker run -it --network=host -p 7777:7777 updater
```

## Notes
 - You are free to change the port, but you will have to change the `EXPOSE` statement in the Dockerfile and rebuild the docker image
 - If you would like the docker image to run in the background, add the `-d` option. 
 - If you would not like to use my certs (which are in plain text because I generated them using openSSL and I signed them myself), you are free to do so as well
 - You will also need to get your browser to trust my certs because _I am the signer_ and no browser will trust my self signed certs (as well as it shouldn't)

### TODOs
 - I plan to add a docker-compose file to allow an easier run of the docker image
 - ~~I plan to add html pages so it will be much more browser friendly~~ Done :)
 - I plan to add the option to prune the IP Addresses to only Linux Operating Systems
