# from rest_framework.authentication import BaseAuthentication, get_authorization_header
# from rest_framework import exceptions
# from accounts.models import User
#
# import jwt
# from django.conf import settings
#
#
# class JWTAuthentication(BaseAuthentication):
#     """
#     override basic HTTP authentication of BaseAuthentication
#     to use JWT
#     """
#
#     def authenticate(self, request):
#
#         # get headers
#         header = get_authorization_header(request)
#
#         # decode to be usable by python
#         data = header.decode('utf-8')
#
#         # split array of headers into two elements: header (Bearer) and the JWT
#         token_split = data.split(" ")
#
#         # error checks
#         if len(token_split) == 1:
#             raise exceptions.AuthenticationFailed('Invalid basic header. No credentials provided.')
#         elif len(token_split) > 2:
#             raise exceptions.AuthenticationFailed('Invalid basic header. Credentials string should not contain spaces.')
#
#         # JWT value
#         token = token_split[1]
#
#         try:
#             payload = jwt.decode(token, "secret", algorithm="HS256")
#
#             username = payload['username']
#
#             user = User.objects.get(username=username)
#
#             return user, token
#         except:
#             pass
#
#         return super().authenticate(request)
