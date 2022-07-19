# Django-auth-demo
This is a Django authentication website made as a demo. This is hosted on Heroku and connected to a Postgresql databse.

Visit this website to check it out: https://django-authentication-demo.herokuapp.com/

This is a basic demo which allows users to create a new account based on a unique username. The user can login after signing up, and once logged in, the sign in page is hidden from the user. The logout button shows up only when the user is logged in. Users with the same username cannot be created. 

The User model is the default model that Django is pre-equipped with. The sign up and sign in forms are also the default Django forms, styled better using crispy forms. 
The navbar and the pages are bootstrapped using CSS bootstrap4.
