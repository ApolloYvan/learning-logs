""" define learning_los's urlpatterns """

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
	# 主页
	path('', views.index, name='index'),
	path('topics/', views.topics, name='topics'),
	path('topic/<int:topic_id>', views.entries, name='topic'),
	path('new_topic/', views.new_topic, name='new_topic'),
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
	path('delete_topic/<int:topic_id>', views.delete_topic, name='delete_topic'),
]
