from django.contrib.auth.models import User

def get_user_from_request(request):
    data = request.data
    username = data["username"] if "username" in data else None
    user = User.objects.get(username=username)
    return user