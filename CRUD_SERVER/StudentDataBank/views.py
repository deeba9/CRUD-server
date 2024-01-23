#from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student,Score,User
from django.db.models import Prefetch
from django.core import serializers
from django.views.decorators.http import require_POST
from django.middleware.csrf import get_token
from django.core import serializers


@csrf_exempt
def index(request):
    return HttpResponse("Welcome to Mobile App Development with BITF20")


#USER
@csrf_exempt
def create_user(request, username, password):
    user = User(username=username, password=password)
    user.save()

    # Create a dictionary representing the user response
    user_response = {
        'username': user.username,
        'password': user.password,  # Note: It's not recommended to return the password
    }

    # Return the user response as JSON
    return JsonResponse({'user': user_response})

@csrf_exempt
def get_csrf_token(request):
    # Get the CSRF token using Django's built-in method
    csrf_token = get_token(request)

    # Return an empty JSON response with the CSRF token
    response = JsonResponse({})
    response['X-CSRFToken'] = csrf_token

    return response

@csrf_exempt
def get_all_users_with_scores(request):
    users = User.custom_objects.prefetch_related(Prefetch('score_set', queryset=Score.objects.all(), to_attr='scores')).all()

    users_list = []
    for user in users:
        user_data = {
            'username': user.username,
            'password': user.password,
            'scores': [{'score_id': score.score_id, 'score': score.score} for score in user.scores]
        }
        users_list.append(user_data)

    return JsonResponse(users_list, safe=False)

@csrf_exempt
def get_user_by_username(request, username, password):
    try:
        user = User.custom_objects.get(username=username, password=password)
        # Process the user data if needed
        user_data = {
            'username': user.username,
            'password': user.password,
        }
        return JsonResponse({'user': user_data})
    except User.DoesNotExist:
        # Handle the case where the user is not found
        return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def get_quiz_score(request, username):
    try:
        user = User.custom_objects.get(username=username)
        quiz_score = Score.objects.filter(user=user).first()
        # Process the score data if needed
        return JsonResponse({'quiz_score': quiz_score.score})
    except User.DoesNotExist:
        # Handle the case where the user is not found
        return JsonResponse({'error': 'User not found'}, status=404)
    except Score.DoesNotExist:
        # Handle the case where the quiz sc
        # ore is not found
        return JsonResponse({'quiz_score': 0}, status=200)

@csrf_exempt
def add_quiz_score(request, username, score_value):
    try:
        user = User.custom_objects.get(username=username)
        # Check if a score entry already exists for this user and quiz
        existing_score = Score.objects.filter(user=user).first()

        if existing_score:
            existing_score.score = score_value
            existing_score.save()
        else:
            # Create a new score entry
            Score.objects.create(user=user, score=score_value)

        return JsonResponse({'success': True})
    except User.DoesNotExist:
        # Handle the case where the user is not found
        return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def delete_user(request, username):
    try:
        user = User.custom_objects.get(username=username)
        # Delete associated quiz scores
        Score.objects.filter(user=user).delete()
        # Delete the user
        user.delete()

        return JsonResponse({'success': True, 'message': 'User and associated scores deleted successfully'})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)