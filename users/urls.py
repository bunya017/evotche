from django.conf.urls import include, url
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views
from . import views



app_name = 'users'
urlpatterns = [
	url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^contact-us/$', views.contact_us, name='contact_us'),
	url(r'^contact-success/$', views.contact_success, name='contact_success'),
    url(r'^password-reset/$', auth_views.password_reset, {'template_name': 'users/registration/password_reset_form.html', 
    														'html_email_template_name': 'users/registration/password_reset_email.html', 
    														'subject_template_name': 'users/registration/password_reset_subject.txt'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'users/registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    	auth_views.password_reset_confirm, {'template_name': 'users/registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'users/registration/password_reset_complete.html'}, name='password_reset_complete'),
	url(r'^polls/(?P<ball_url>[-\w]+)/$', views.show_ballot_page, name='show_ballot_page'),
	url(r'^vote-page/(?P<ball_url>[-\w]+)/$', views.new_show_ballot_page, name='new_show_ballot_page'),
	url(r'^token/$', views.token_login, name='token_login'),
	url(r'^my-tokens/$', views.tokens_view, name='tokens_view'),
	url(r'^my-tokens/(?P<ball_url>[-\w]+)/$', views.my_token, name='my_token'),
	url(r'^check-results/$', views.check_results, name='check_results'),
	url(r'^profile/$', views.display_profile, name='display_profile'),
	url(r'^profile/update$', views.update_profile, name='update_profile'),
	url(r'^my-tokens/(?P<ball_url>[-\w]+)/upload/$', views.email_upload, name='email_upload'),
	# url(r'^free-tokens/(?P<ballot_url>[-\w]+)/$', views.get_free_tokens, name='get_free_tokens'),
	#url(r'^refresh-purchase/(?P<ref_code>[-\w]+)/$', views.refresh_purchase, name='refresh_purchase'),
]