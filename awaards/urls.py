from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views as awaard_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'profiles', awaard_views.ProfileViewSet)
router.register(r'projects', awaard_views.ProjectViewSet)

urlpatterns= [
    path('signup/',awaard_views.signup, name='signup'),
    path('', awaard_views.homepage, name='homepage'),
    path('api/', include(router.urls)),
    path('profiles/', awaard_views.ProfileListView.as_view(), name='profiles'),
    path('profiles/<int:pk>/', awaard_views.ProfileDetailView.as_view(), name='profile'),
    path('profiles/<int:pk>/update/', awaard_views.ProfileUpdateView.as_view(), name='profileUpdate'),
    path('projects/', awaard_views.ProjectListView.as_view(), name='projects'),
    path('projects/new/', awaard_views.ProjectCreateView.as_view(), name='projectNew'),
    path('projects/<int:pk>/', awaard_views.ProjectDetailView.as_view(), name='project'),
    path('projects/<int:pk>/update/', awaard_views.ProjectUpdateView.as_view(), name='projectUpdate'),
    path('projects/<int:pk>/delete/', awaard_views.ProjectDeleteView.as_view(), name='projectDelete'),
    path('projects/<int:pk>/rate/new/', awaard_views.RateCreateView.as_view(), name='rateNew'),
    path('rate/<int:pk>/update/', awaard_views.RateUpdateView.as_view(), name='rateUpdate'),
    path('rate/<int:pk>/delete/', awaard_views.RateDeleteView.as_view(), name='rateDelete'),
    path('search-results/',awaard_views.search_results,name='searchProject')
]
