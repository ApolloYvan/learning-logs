from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic,Entry
from .form import TopicForm,EntryForm
# Create your views here.
def index(request):
	""" 学习笔记的主页 """
	return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
	""" 获取所有Topic页面 """
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics':topics}
	return render(request, 'learning_logs/topics.html', context)

@login_required
def entries(request, topic_id):
	""" 获取指定Topic的所有条目 """
	topic = Topic.objects.get(id=topic_id)
	if request.user != topic.owner:
		raise Http404
	entries = topic.entry_set.order_by('date_added')
	context = {"topic":topic, "entries":entries}
	return render(request, 'learning_logs/entry.html', context)

@login_required
def new_topic(request):
	""" 用于创建新Topic """
	if request.method != 'POST':
		form = TopicForm()
	else:
		form = TopicForm(data=request.POST)
		if form.is_valid:
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('learning_logs:topics')
	context = {'form':form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid:
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return redirect('learning_logs:topic',topic_id=topic_id)
	context = {'form':form, 'topic':topic}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404
	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid:
			form.save()
			return redirect('learning_logs:topic', topic_id=topic.id)
	context = {'form':form,'entry':entry, 'topic':topic}
	return render(request, 'learning_logs/edit_entry.html', context)

@login_required
def delete_topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	if topic.owner != request.user:
		raise Http404
	topic.delete()
	return redirect('learning_logs:topics')
