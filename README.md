## Personal Django boilerplate

#### BEFORE RUNNING
Run the initial setup
```
./initial_setup.sh <projectname>
```

If initial setup is done execute the following command to create a admin user

```python
python manage.py create_user -a <username> <email> <password>
```
___
##### Small Extra's
###### Small script to generate a new secret key
<small>Does not replace the current secretkey</small>

```python
python manage.py generate_secret_key
```

_Do not forget that when you are going live to remove_
* _rename_project.py_
* _delete_user.py_
