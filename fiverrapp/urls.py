from django.urls import path,re_path
from .views import (home, login_view, register_view, logout_view, create_gig, my_gigs, edit_gig, gig_detail, profile,
                    create_purchase, my_sellings, my_buyings, show_gig_by_category)

urlpatterns = [
    re_path(r'^$', home, name='home'),
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^register/$', register_view, name='register'),
    re_path(r'^logout/$', logout_view, name='logout'),
    re_path(r'^my_gigs/$', my_gigs, name='my_gigs'),
    re_path(r'^create_gig/$', create_gig, name='create_gig'),
    re_path(r'^edit_gig/(?P<id>[0-9]+)/$', edit_gig, name='edit_gig'),
    re_path(r'^gigs/(?P<id>[0-9]+)/$', gig_detail, name='gig_detail'),
    re_path(r'^profile/(?P<username>\w+)/$', profile, name='profile'),
    re_path(r'^checkout/$', create_purchase, name='create_purchase'),
    re_path(r'^my_sellings/$', my_sellings, name='my_sellings'),
    re_path(r'^my_buyings/$', my_buyings, name='my_buyings'),
    re_path(r'^category/(?P<category>\w+)/$', show_gig_by_category, name='category'),
]
