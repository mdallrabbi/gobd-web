from __future__ import absolute_import
import time
import json
import logging
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.contrib.auth.models import User
from channels import Channel
from celery import shared_task
from celery.utils.log import get_task_logger
from main.models import Store, Task, DeliveryBoy
from main.serializers import TaskSerializer
from gobdWeb.celery import app


log = logging.getLogger(__name__)
logger = get_task_logger(__name__)


@app.task
def deliver_task_accept_notification(task_id, reply_channel):
	task = Task.objects.get(pk=task_id)
	log.debug("Running Task_name=%s", task.title)
	task.status = Task.PICKUP
	task.save()

	# send status update back to browser client

	if reply_channel is not None:
		Channel(replay_channel).send({
			"text": json.dumps({
					"action": "deliver_task_has_accepted",
					"task_id": task_id,
					"task_name": task.title,
					"task_status": task.status,
					"task_priority": task.priority,
					"task_store": task.store,
				})
			})


@app.task
def store_manager_created_new_task(task_id, reply_channel):
	task = Task.objects.get(pk=task_id)
	log.debug("Running Task Name=%s", task.title)
	if reply_channel is not None:
		Channel(reply_channel).send({
				"text": json.dumps({
					"action": "order_has_been_picked_up",
					"task_id": task_id,
					"task_title": task.title,
					"task_status": task.status,
					"task_priority": task.priority,
					"task_store": task.store
				})
			})


@app.task
def deliver_task_reject_notification(task_id, reply_channel):
	task = Task.objects.get(pk=task_id)
	log.debug("Running Task Name=%s", task.title)
	if reply_channel is not None:
		Channel(reply_channel).send({
				"text": json.dumps({
					"action": "your_order_has_delivered",
					"task_id": task_id,
					"task_name": task.title,
					"task_status": task.status,
					"task_priority": task.priority,
					"task_store": task.store,
				})
			})


@app.task
def deliver_task_completed_notification(task_id, reply_channel):
	task = Task.objects.get(pk=task_id)
	log.debug("Running Task Name=%s", task.title)
	if reply_channel is not None:
		Channel(reply_channel).send({
				"text": json.dumps({
					"action": "please_collect_your_product",
					"task_id": task_id,
					"task_name": task.title,
					"task_status": task.status,
					"task_priority": task.priority,
					"task_store": task.store,
				})
		})	