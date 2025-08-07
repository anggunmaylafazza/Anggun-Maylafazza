from auth_app.models import ArsysInstitutionRole, ArsysStudent, ArsysStaff

def get_user_role(user_id):
    if ArsysStudent.objects.filter(user_id=user_id).exists():
        return 'student'
    elif ArsysStaff.objects.filter(user_id=user_id).exists():
        return 'staff'
    elif ArsysInstitutionRole.objects.filter(user_id=user_id).exists():
        return 'admin'
    else:
        return 'unknown'

