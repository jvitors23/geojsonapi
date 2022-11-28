from django.urls import path

from geojsonapi.apps.users.views import CreateTokenView, CreateUserView, ManageUserView

app_name = "users"

urlpatterns = [
    path("signup/", CreateUserView.as_view(), name="create"),
    path("token/", CreateTokenView.as_view(), name="token"),
    path("me/", ManageUserView.as_view(), name="manage-user"),
]
