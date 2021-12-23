# PhysicalTestTask

A simple REST tool for determining the week number. December 30, 2018 - the 1st day of the 1st week.


### How to use
Run in the terminal:
```
git clone https://github.com/youngdanon/PhysicalTestTask.git
cd PhysicalTestTask
sudo docker-compose up --build
```
Create `.env` file in project root directory
```
DEBUG=(True/False)
SECRET_KEY=(Your secret key)
DJANGO_ALLOWED_HOSTS=(Your hostname)
```
Send a `GET` request in the following format
```
GET /api/week/?date=dd_mm_yyyy
```
Also you can test it on [my site](http://dfarsal1.fvds.ru/api/week/?date=6_01_2019)
### Example
#### request
```
GET /api/week/?date=6_01_2019
```
#### response
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "week": 2
}
```

