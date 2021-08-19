### Example of API Testing Framework using Python, Pytest, Pytest-BDD, and Requests.

#### API tests
![49599ACE-7C32-41A8-A327-8AFBFD3F218B](https://user-images.githubusercontent.com/10586980/129997542-7facdc6a-d2bb-44a2-beea-b5b7f106fcaa.GIF)

#### Smoke tests
![A5A9D42A-41DD-4639-B259-2C2F010C0339](https://user-images.githubusercontent.com/10586980/129998533-e9cc6145-4e21-48cc-9ce4-1cb4f7c27a72.GIF)


### How to Build/Run locally:
#### clone repo:
```
git clone https://github.com/Tolstr/public-api-automation-framework.git
cd public-api-automation-framework
```
#### Dependencies 
1. In order to run you have to install Python3.6+
2. You need to have pip installed
3. install python3 - pip  https://www.python.org/downloads/
4. Getting dependencies:
```
$ pip install virtualenv
$ python3 virtualenv env
$ env/Scripts/activate (for win)
$ source env/bin/activate (for mac-linux)
$ pip install -r requirements.txt
```
#### Running all tests
```
pytest --base_url https://swapi.dev/api/

```
#### Running smoke tests
```
pytest --base_url https://swapi.dev/api/ tests

```
