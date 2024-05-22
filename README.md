# project-b-11

I was the REQUIREMENTS MANAGER. I was responsible for keeping up with the features of the project by elicitating requirements, tracking features throughout development, and monitoring the state of the project. Outside of the main role, I helped develop various aspects of the application.

I contributed to the project working on the following features:
- Added the ability to submit whistleblower statements
- Store whistelblower statements/reports in AWS S3 storage
- Allow users to upload .txt, .pdf, .jpg files with their reports (which got stored in S3)
- Added appeal function to user reports. This included the appeals model, page, and button.
- Added admin ability to review appeals and edit report status
- Information page on  Non-retaliation policies
- Company specific reporting information
- Button for users to stay anonymous
- Created terms of service and privacy policy
- Assisted a bit in the CSS and styling of the page

---------------------------------------------------------

To run the code do the following:

1) Create a virtual environment using Conda or Python Venv

Conda:

```
conda create --name project-b-11 python=3.11
conda activate project-b-11
pip3 install -r requirements.txt
```

Python Venv (Windows -> so adapt to Linux/Unix)
```
python3 -m venv venv
venv\Scripts\activate
pip3 install -r requirements.txt
```

2) To access the login page run:

```
python manage.py makemigrations
python manage.py makemigrations whistleblower
python manage.py migrate
python manage.py runserver
```

3) To begin, you need to create a site user from:
```
localhost/admin
```
Click users, then click create user group siteAdmin

4) Then all required setup is complete.
