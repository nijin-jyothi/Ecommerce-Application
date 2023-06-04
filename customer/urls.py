from django.urls import path
from customer import views

urlpatterns=[
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("login",views.SignInView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="home"),
    path("products/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
    path("products/<int:id>/carts/add",views.AddToCartView.as_view(),name="cart-add"),
    path("customer/carts/all",views.CartListView.as_view(),name="cart-list"),
    path("carts/<int:id>/change", views.CartRemoveView.as_view(),name="cart-change"),
    path("orders/add/<int:id>",views.MakeOrderView.as_view(),name="create-order"),
    path("order/list",views.OrdersListView.as_view(),name="order-list"),
    path("orders/<int:id>/cancel",views.OrderCancelView.as_view(),name="order-cancel"),
    path("offers/all",views.DiscountProductView.as_view(),name="offers"),
    path("review/<int:id>/add",views.ReviewCreateView.as_view(),name="review-add"),
    path("logout",views.signout_view,name="signout")
]