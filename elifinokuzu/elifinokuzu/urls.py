from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from reports import views as report_views
from support import views as support_views
from dictionary import views as dictionary_views
from accounts import views as account_views
from comments import views as comment_views
from django.contrib.auth import views


urlpatterns = [
    # Basic templates
    path('', dictionary_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about/', dictionary_views.about, name='about'),
    path('support/', support_views.support, name='support'),
    path('supportdone/', support_views.supportdone, name ='supportdone'),
    # Account
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', account_views.signup, name='signup'),
    path('accounts/profile/<int:id>', account_views.dashboard, name='dashboard'),
    # Dictionary
    path('nodes/<int:id>/', dictionary_views.node_detail, name='node_detail'),
    path('edges/<int:id>/', dictionary_views.edge_detail, name='edge_detail'),
    path('nodes/<int:id>/comment/', comment_views.add_comment_to_node, name='add_comment_to_node'),
    path('edges/<int:id>/comment/', comment_views.add_comment_to_edge, name='add_comment_to_edge'),
    path('submit/', dictionary_views.submit, name='submit'),
    path('search/<str:word>/', dictionary_views.search, name='search'),
    path('language/<str:language>/', dictionary_views.language, name='language'),
    # Report
    path('json', report_views.jsondata, name='jsondata'),
    path('report/<int:id>', report_views.report, name='report'),
    path('reportdone/', report_views.reportdone, name ='reportdone'),
    # Comments
    path('avatar/', include('avatar.urls')),
    path('delete/<int:id>/<int:node_id>', comment_views.delete_own_comment, name='delete_own_comment'),
    path('delete/<int:own_id>', dictionary_views.delete_own_created, name="delete_own_created")
]
