from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout, login, password_change, password_change_done
from django.views.generic import ListView
from qsub.views import *
from qsub.models import *

import django

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'QuEST.views.home', name='home'),
    # url(r'^QuEST/', include('QuEST.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^main/$', main),
    (r'^$', main),
    (r'^register/$', register),
    (r'^accounts/login/$', django.contrib.auth.views.login),
    (r'^accounts/logout/$', logout),
    (r'^profile/$', profile),
    (r'^password_change_done/$', django.contrib.auth.views.password_change_done),
    (r'^password_change/$', django.contrib.auth.views.password_change, {'post_change_redirect': '/profile/',
                                                                        'template_name': 'registration/password.html'}),
    #(r'^password_change/$', password_change),
    (r'^question_sets/$', question_sets),
    (r'^create_question_set/$', create_question_set),
    (r'^edit_question_set/(?P<qset_id>[0-9]+)/$', edit_question_set),
    (r'^distributions/$', distributions),
    (r'^add_editor/(?P<qset_id>[0-9]+)/$', add_editor),
    (r'^add_writer/(?P<qset_id>[0-9]+)/$', add_writer),
    (r'^edit_distribution/(?P<dist_id>[0-9]+)/$', edit_distribution),
    (r'^edit_distribution/$', edit_distribution),
    (r'^edit_tiebreak/(?P<dist_id>[0-9]+)/$', edit_tiebreak),
    (r'^edit_tiebreak/$', edit_tiebreak),
    (r'^edit_set_distribution/(?P<qset_id>[0-9]+)/$', edit_set_distribution),
    (r'^edit_set_tiebreak/(?P<qset_id>[0-9]+)/$', edit_set_tiebreak),
    (r'^add_tossups/(?P<qset_id>[0-9]+)/$', add_tossups),
    (r'^add_tossups/(?P<qset_id>[0-9]+)/(?P<packet_id>[0-9]+)/$', add_tossups),
    (r'^edit_tossup/(?P<tossup_id>[0-9]+)/$', edit_tossup),
    (r'^delete_tossup/$', delete_tossup),
    (r'^add_bonuses/(?P<qset_id>[0-9]+)/$', add_bonuses),
    (r'^add_bonuses/(?P<qset_id>[0-9]+)/(?P<packet_id>[0-9]+)/$', add_bonuses),
    (r'^edit_bonus/(?P<bonus_id>[0-9]+)/$', edit_bonus),
    (r'^delete_bonus/$', delete_bonus),
    (r'^add_packets/(?P<qset_id>[0-9]+)/$', add_packets),
    (r'^edit_packet/(?P<packet_id>[0-9]+)/$', edit_packet),
    (r'^type_questions/$', type_questions),
    (r'^type_questions/(?P<qset_id>[0-9]+)/$', type_questions),
    #(r'^edit_packet/(?P<packet_id>[0-9]+)/change_tossup_position/(?P<old_index>[0-9]+)/(?P<new_index>[0-9]+)$', change_tossup_order),
    #(r'^edit_packet/(?P<packet_id>[0-9]+)/change_bonus_position/(?P<old_index>[0-9]+)/(?P<new_index>[0-9]+)$', change_bonus_order),
    (r'^delete_packet/$', delete_packet),
    (r'^settings/$', settings),

    (r'^upload_questions/(?P<qset_id>[0-9]+)/$', upload_questions),
    (r'^complete_upload/$', complete_upload),

    # json calls
    (r'^get_unassigned_tossups/$', get_unassigned_tossups),
    (r'^get_unassigned_bonuses/$', get_unassigned_bonuses),
    (r'^assign_tossups_to_packet/$', assign_tossups_to_packet),
    (r'^assign_bonuses_to_packet/$', assign_bonuses_to_packet),
    (r'^change_question_order/$', change_question_order),
    #(r'^change_tossup_position/$', change_tossup_order),
    #(r'^change_bonus_position/$', change_bonus_order),

    # commenting framework
    (r'^comments/', include('django_comments.urls')),
)
