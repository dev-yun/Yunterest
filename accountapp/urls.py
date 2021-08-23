from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

urlpatterns = [

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
# path를 지정할때 FBV인 hello_world는 그냥 hello_world로 받아오지만
# CBV인 create는 AccountCreateView.as_view() 라는 as_view()를 명시해줘야한다.
# detail은 특정 user의 정보를 읽어야 하므로, 특정 user의 id (즉 prime key)가 필요하다. => <int:pk>(몇번 user에 접근할건지)