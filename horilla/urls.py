"""horilla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

import notifications.urls_v1

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("v1/", include("base.urls_v1")),
    path("recruitment/v1/", include("recruitment.urls")),
    path("employee/v1/", include("employee.urls_v1")),
    path("leave/v1/", include("leave.urls_v1")),
    path("onboarding/v1/", include("onboarding.urls_v1")),
    path("pms/v1/", include("pms.urls_v1")),
    path("asset/v1/", include("asset.urls_v1")),
    path("attendance/v1/", include("attendance.urls_v1")),
    path("payroll/v1/", include("payroll.urls.urls_v1")),
    path("helpdesk/v1/", include("helpdesk.urls_v1")),
    path("offboarding/v1/", include("offboarding.urls_v1")),
    path("horilla-widget/v1/", include("horilla_widgets.urls_v1")),
    re_path(
        "^inbox/notifications/v1/", include(notifications.urls_v1, namespace="notifications")
    ),
    path("i18n/", include("django.conf.urls.i18n")),

    path("api/v2/", include([
        path("", include("base.urls_v2")),
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path("employee/", include("employee.urls_v2")),
        path("asset/", include("asset.urls_v2")),
        path("attendance/", include("attendance.urls_v2")),
        path("helpdesk/", include("helpdesk.urls_v2")),
        path("leave/", include("leave.urls_v2")),
        path("notifications/", include("notifications.urls_v2")),
        path("offboarding/", include("offboarding.urls_v2")),
        path("onboarding/", include("onboarding.urls_v2")),
        path("payroll/", include("payroll.urls.urls_v2")),
        path("pms/", include("pms.urls_v2")),
        path("recruitment/", include("recruitment.urls_v2")),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
