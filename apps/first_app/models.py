from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here
class UserManager(models.Manager):
    def register_val(self, postData):
        print postData
        results ={'status': True, 'errors':[], 'user':None}
        if not postData['fname'] or len(postData['fname'])<=2:
            results['status']= False
            results['errors'].append('First Name must be longer')
        if not postData['lname'] or len(postData['lname'])<=2:
            results['status']= False
            results['errors'].append('Last Name must be longer')
        if not EMAIL_REGEX.match(postData['email']):
            results['status']= False
            results['errors'].append('invalid is not email')
        if not postData['password'] or len(postData['password'])<=8:
            results['status']= False
            results['errors'].append('not a valid password')
        if str(postData['password']) == str(postData['cpassword']):
            results['status']= False
            results['errors'].append('password do not match')

        if results['status']:
            new_user = User.objects.create(
            fname = postData['fname'],
            lname = postData['lname'],
            email = postData['email'],
            password = postData['password']
            )
            results['user'] = new_user
        return results

    def login(self, postData):
        results = {'status':True, 'errors':[], 'user':None}
        try:
            results['user'] = User.objects.get(email = postData['email'])
        except:
            results['status'] = False
            results['errors'].append('no email or password')
            return results

        if str(results['user'].password) == str(postData['password']):
            results['status'] = True
        else:
            results['status'] = False
            results ['erros'].append('no email or password')
        return results
    # def login():


class User(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

# class ___(models.Model):
