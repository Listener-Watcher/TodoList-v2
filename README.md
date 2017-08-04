## Features
- Registration with verification
![](register.gif

- Contact
![](contact.gif

- Log in and log out
![](login_out.gif

- Add a task
![](add.gif

- Edit a task
![](edit.gif

- Done and delete a task
![](done_delete.gif

- Sort tasks
![](sort.gif)

## Steps to Runserver
### Change Admin Email for Registration Verification
- Edit settings.py
```
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'your_email@163.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
EMAIL_PORT = 25
EMAIL_USER_TLS = True
DEFAULT_FROM_EMAIL	= 'your_email@163.com'
```

### Install Modules
- `sudo pip install -r requirements.txt`
- `cd todol`
- `sudo python manage.py runserver`

## Others
- Note: [https://today2tmr.com/en/2017/08/04/notes-for-todo-list-project-with-django-and-react/](https://today2tmr.com/en/2017/08/04/notes-for-todo-list-project-with-django-and-react/)
- If you add more static files, don't forget to `sudo python manage.py collectstatic`.
