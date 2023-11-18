# IELTSWays_Task

Run commands to install and run APIs

pip install virtualenv

python3 -m venv env

in mac or linux source env/bin/activate

//In Windows CMD env/Scripts/ac tivate.bat

pip install -r requirements.txt

Python3 manage.py migrate

Python3 manage.py runserver

The API url path is http://127.0.0.1:8000/api/schema/docs/.

I use Swagger for API documentation.


I use a simple SQLite database but you can change it to Postgresql database. You can just create your PostgreSQL database in pgAdmin and change the DATABASE in setting.py.

# IELTSWays_Task_Procedure

First you create user with user registeration api and then login in account APIs.
In login API when ypou logged in successfully you get access token,copy it and past in authentication without Bearer.

Next I created 2 types of IELTS exam you get them.In examregisterationpost method you can register a exam with exam id it means you can just use 1 or 2 as exam.Also you not enter any user and user detected from our authentication.
Example of body request 

{
  "exam": 1,
  "date": "2023-11-18T08:48:04.179Z"
}
For exam_withdrawal_registeration should do it too.

Finally you can get list of exams and list of user that registered and withdrawaled user in other APIs.Also you can get list of user that registered base on exam_id.


# IELTSWays_Task_Tests
Run   python3 manage.py test  see some tests for APIs