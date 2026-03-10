from django.urls import path
from app.views.treino_views import TreinoCreateView, TreinoListView, TreinoUpdateView, TreinoDetailView

urlpatterns = [
    path("treino/criar", TreinoCreateView.as_view(), name="create-treino"),
    path("treino/listar", TreinoListView.as_view(), name="list-treino"),
    path("treino/<int:pk>/atualizar", TreinoUpdateView.as_view(), name="update-treino"),
    path("treino/<int:pk>", TreinoDetailView.as_view(), name="detail-treino"),
]