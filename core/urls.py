from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from polls.views import PollViewSet, QuestionViewSet, VoteViewSet
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

router = DefaultRouter()
router.register(r"polls", PollViewSet)
router.register(r"questions", QuestionViewSet)
router.register(r"votes", VoteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^v1/", include((router.urls, "v1"), namespace="v1")),
    path(
        'v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(
        'v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
