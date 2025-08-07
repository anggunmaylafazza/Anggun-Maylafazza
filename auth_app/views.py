from .decorators import role_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Users
from django.conf import settings
import jwt
from datetime import datetime, timedelta  # ← tambahkan ini
from .utils import get_user_role

@csrf_exempt
@role_required(['student'])  # hanya student bisa akses ini
def student_only_view(request):
    return JsonResponse({'success': True, 'message': f"Halo mahasiswa ID {request.user_id}!"})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            email = data.get('email')
            password = data.get('password')

            user = Users.objects.filter(email=email, password=password).first()

            if user:
                # DETEKSI ROLE
                user_role = get_user_role(user.id)

                # BUAT JWT
                payload = {
                    'user_id': user.id,
                    'email': user.email,
                    'role': user_role,
                    'exp': datetime.utcnow() + timedelta(days=1),
                }
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

                return JsonResponse({
                    'success': True,
                    'message': 'Login berhasil',
                    'token': token,
                    'user': {
                        'id': user.id,
                        'name': user.name,
                        'email': user.email,
                        'role': user_role
                    }
                })
            else:
                return JsonResponse({'success': False, 'message': 'Email atau password salah'}, status=401)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)
