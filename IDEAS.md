# Project Ideas


## Where to run this scrapy

The initial idea is to run it on a Docker image. This docker image can run as a container on Raspberry Pi to download the audio files into the audio file. After the audio file is downloaded to the audio dir, Plex will add it to the library.


## Steps


### Build Scrapy

- Check and check how to help scrapy to select the audio files from the page.
  - Login page URL https://www.zad-academy.com/login/login.html this page will redirect to a page with a list of courses.
  - When you login you can use this CSS selector `h3.coursename a` to get into the course page.
  - 
- Build a registry to ignore the already downloaded audio files.
- Take care of the MP3 ID3 (Meta Data) This data will help Plex server.


### Create Docker image

- Mount the audio volumn in order Docker to download the files into.
- Use Scrapy docker image (Check in Docker hub and this image should suppoer ARM CPU as it will run on Raspberry Pi).:
  - https://hub.docker.com/r/aciobanu/scrapy


### Deploy and run docker on Raspberry Pi

- User portiner to run the container and mount the audio volumn.
