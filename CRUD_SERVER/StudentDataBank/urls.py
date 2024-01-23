from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('get_csrf_token/', views.get_csrf_token, name='get_csrf_token'),
    path("SignUp/<str:username>/<str:password>", views.create_user, name="create_user"),
    path("SignIn/<str:username>/<str:password>", views.get_user_by_username, name="get_user_by_username"),
    path("add_quiz_score/<str:username>/<int:score_value>", views.add_quiz_score, name="add_quiz_score"),
    path("get_quiz_score/<str:username>", views.get_quiz_score, name="get_quiz_score"),
    path("delete_user/<str:username>/", views.delete_user, name="delete_user"),
    path("get_all_users_with_scores/", views.get_all_users_with_scores, name="get_all_users_with_scores")
]

