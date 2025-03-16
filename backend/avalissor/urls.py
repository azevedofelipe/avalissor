from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CollegeViewSet, CourseViewSet, ProfessorViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'colleges', CollegeViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'professors', ProfessorViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/', include('dj_rest_auth.urls')),
]
