# selenium_classic_framework BDD
GUI tests for https://opensource-demo.orangehrmlive.com/.

Following tech stack was used for this task: python 3, pipenv, unittest, selenium, webdriver-manager, behave, 
invoke, pyhamcrest.

How to execute tests
* download selenium_classic_framework to your local PC, or clone repo.
* open console in target folder 
* execute command `behave` to run all tests
* or execute  `invoke run --browser=[CH_HL,CH] --resh=[int] resw=[int] --tags=[tc1,tc2,tc3]`

How to execute tests in Docker container
Creating an image
* Install Docker on your local environment.
* download selenium_classic_framework to your local PC, or clone repo.
* open console in target folder.
* execute `docker build -t sel_bdd_fw .`.
Executing
* open console, execute `docker run -it sel_bdd_fw` and leave this console instance running.
* open another console instance, execute `docker ps` and note the "CONTAINER ID".
* execute `docker exec -it CONTAINER_ID sh` to get access for container CLI.
* execute command `invoke run` to run all tests.
* or execute  `invoke run --browser=[CH_HL,CH] --resh=[int] resw=[int] --tags=[tc1,tc2,tc3]`.
