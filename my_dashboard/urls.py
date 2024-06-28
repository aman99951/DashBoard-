from django.urls import path, include

urlpatterns = [
    path('api/', include('dashboard.urls')),
    # Add other URLs as needed
]
