# from rest_framework import permissions
# from datetime import timedelta, datetime
#
#
# class CanEditWithinSpecialTime(permissions.BasePermission):
#     message = 'User Or Time exception'
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in ['PUT', 'PATCH', 'DELETE']:
#             if request.user.username != 'jasur':
#                 return False
#
#             deadline = datetime.now(obj.created_at.tzinfo) - obj.created_at
#             print(deadline)
#             return deadline < timedelta(hours=2)
#
#         return True



from rest_framework import permissions
from datetime import datetime, time


class IsWithinWorkingHours(permissions.BasePermission):

    message = "Ruxsat etilmagan: faqat ish vaqtida (9:00–18:00) o'zgartirish mumkin."

    def has_permission(self, request, view):
        # Faqat PUT, PATCH, DELETE uchun ish vaqti tekshiriladi
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            now = datetime.now().time()
            start_time = time(9, 0, 0)
            end_time = time(18, 0, 0)

            if start_time <= now <= end_time:
                return True
            return False

        return True
