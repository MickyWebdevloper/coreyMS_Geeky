urls.py -->

    # made by me.
    from django.contrib.auth import views as auth_view

from miniblog.settings import INSTALLED_APPS

    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LoginView.as_view(template_name='users/logout.html'), name='logout'),


settenigs.py --->

    INSTALLED_APPS -->
         # made by me.
        'crispy_forms',

        
    # made by me for crispy form
    CRISPY_TEMPLATE_PACK = "bootstrap4"

    # made by me.
    LOGIN_REDIRECT_URL = 'home'
    LOGIN_URL = 'login'
