## Personal Django boilerplate

Based of JustDjango's boilerplate tutorial but adaption is made to use for easy website setup and styling.

### To rename your project
cd in src and execute the following
```python
python manage.py rename_project 'YourNewProjectName'
```
#### Small script to generate a new secret key
###### _Does not replace the current secretkey_
In src folder
```python
python manage.py generate_secret_key
```

__Do not forget that when you are going live to remove__
* __rename_project.py__
* __delete_user.py__


#### App creation TODO:
- [x] Website app
- [x] Model creation website app
- [x] Admin creation website app
- [x] Project setup Global
- [ ] Project setup individual

#### PageStyling TODO:
- [x] ColorField
- [x] ImageField
- [x] Background Image
- [ ] Testimonial carousel
- [ ] Background Image with Parralax scroll
