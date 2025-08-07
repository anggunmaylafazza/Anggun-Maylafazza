from functools import wraps
from django.http import JsonResponse
import jwt
from django.conf import settings

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            auth_header = request.META.get('HTTP_AUTHORIZATION')
            if not auth_header or not auth_header.startswith('Bearer '):
                return JsonResponse({'success': False, 'message': 'Unauthorized'}, status=401)

            token = auth_header.split(' ')[1]
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                user_role = payload.get('role')
                print(f"DEBUG ROLE JWT: {user_role}")  # ← Tambahkan log ini

                if user_role not in allowed_roles:
                    return JsonResponse({'success': False, 'message': 'Access denied'}, status=403)

                request.user_id = payload.get('user_id')
                request.user_role = user_role
            except jwt.ExpiredSignatureError:
                return JsonResponse({'success': False, 'message': 'Token expired'}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({'success': False, 'message': 'Invalid token'}, status=401)

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


