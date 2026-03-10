from django.urls import path
from app.views.assinatura_views import (AssinaturaDeleteView, 
                                        AssinaturaCreateView, 
                                        AssinaturaListView, 
                                        AssinaturaUpdateView, 
                                        AssinaturaDetailView,
                                        PagamentoListView)
urlpatterns = [
    path("assinatura/criar", AssinaturaCreateView.as_view(), name="create-assinatura"),
    path("assinatura/listar", AssinaturaListView.as_view(), name="list-assinatura"),
    path("assinatura/<int:pk>", AssinaturaDetailView.as_view(), name="detail-assinatura"),
    path("assinatura/<int:pk>/atualizar", AssinaturaListView.as_view(), name="update-assinatura"),
    path("assinatura/<int:pk>/excluir", AssinaturaDeleteView.as_view(), name="delete-assinatura"),
    path("pagamento/listar", PagamentoListView.as_view(), name="list-pagamento"),
]