from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('create/', AccountCreateView.as_view(), name='create')
]
# path를 지정할때 FBV인 hello_world는 그냥 hello_world로 받아오지만
# CBV인 create는 AccountCreateView.as_view() 라는 as_view()를 명시해줘야한다.