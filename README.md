# MemoVerse

* Description: This is a toy application written in HTML, CSS, JavaScript, and Python, high-level programming languages. The application is created with the aim to help a person in the process of memorizing Biblical verses for spiritual health. Currently, it allows a user to chose a verse of interest, add it to the dynamodb database with a theme tag, and view added verses based on the theme. Themes allow a user to study particular themes like the character of God, where we came from, what God expects of us, the state of the dead, when Jesus is coming back, etc found in the Scriptures.

## Access application on the web
* Visit this page: [MemoVerse](https://memoverse.herokuapp.com/)


## Access application manually - TO_VERIFY

### Using your computer os for memoverse environment

#### Requirements
* Linux OS, Terminal, Python, Python3, Virtualenv, [API.Bible](https://scripture.api.bible/signup) API Key
* Note: will also work on Mac OS but with different commands for creating virtual environment
#### Starting the application
* Open terminal and clone this repository
* Change into the memoverse directory
* Create BIBLE_API_KEY environment variable by ```export BIBLE_API_KEY=PLACE_YOUR_KEY_HERE```
* Create local virtual environment using ```virtualenv -p python3 env``` command
* Activate the environment using ```source env/bin/activate``` command
* Install dependencies using ```pip install -r requirements.txt``` command
* Run the application using ```python application.py```
* Open your favorite browser and access the application at the following address: ```http://0.0.0.0:8000/```
#### Stopping the application
* In your terminal press ```ctrl+c``` to terminate the server
* Type ```deactivate``` to leave the local virtual environment


### Using Docker

#### Requirements
* Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
* Obtain [API.Bible](https://scripture.api.bible/signup) Key
#### How to run
* Start Docker
* Using Terminal, run application by ```docker run -di -p 8000:80 -e BIBLE_API_KEY=PLACE_YOUR_KEY_HERE vlames/memoverse``` command
* Open your favorite browser and access the application at the following address: ```http://0.0.0.0:8000/``` 
#### How to stop
* In terminal, do ```docker ps``` to find container id
* Stop container by ```docker stop container_id```
#### Clean up
* Find container id by ```docker ps -a```
* In terminal, type ```docker rm container_id``` to delete container
* Find image id by ```docker images```
* Delete image by ```docker rmi image_id```

## Credits

* The application was derived from the Internet, Cloud, and Sequrity class example at PSU
* MDN, Bootstrap, and W3Schools documentation was helpful in grasping concepts
* Usage of requests python library: https://www.youtube.com/watch?v=sbYXa6HJJ5M
* Flask select field: https://www.youtube.com/watch?v=I2dJuNwlIH0
