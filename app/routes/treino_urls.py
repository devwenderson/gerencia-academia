from django.urls import path
from app.views.treino_views import TreinoCreateView, TreinoListView

urlpatterns = [
    path("treino/criar", TreinoCreateView.as_view(), name="create-treino"),
    path("treino/listar", TreinoListView.as_view(), name="list-treino"),
]