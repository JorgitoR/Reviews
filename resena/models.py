# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime, operator
from decimal import *
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import formats
from django.utils.html import format_html, mark_safe, linebreaks
from .defaults import *


class ReviewsManager(models.Manager):

	def filtrar_por_instancia(self, instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)
		obj_id = instance.id
		qs =super(ReviewsManager, self).filter(content_type= content_type, object_id= obj_id)
		return qs

class Review(models.Model):

    if REVIEWABLE_MODELS:
        limit = reduce(operator.or_, (models.Q(**condition) for condition in REVIEWABLE_MODELS))
    else:
        limit = None

    content_type = models.ForeignKey(ContentType,  limit_choices_to=limit, help_text="Modelo de objeto revisado",)
    
    object_id = models.PositiveIntegerField(help_text="ID de objeto revisado",)
    
    reviewed_object = GenericForeignKey('content_type', 'object_id',)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', help_text="User that submitted the review",)
    
    score = models.PositiveSmallIntegerField(
        choices=SCORE_CHOICES,
        help_text="Puntuación entera en un rango de %d a  %d" % (MIN_SCORE, MAX_SCORE),
    )

    comment = models.TextField(
        max_length=MAX_COMMENT_LENGTH,
        blank=not COMMENT_REQUIRED,
        help_text="Un comentario explicando el resultado de la revision",
    )

    anonymous = models.BooleanField(
        default=False,
        help_text="Mantenga la identidad del revisor anonima",
    )
    comment_approved = models.BooleanField(
        default=not COMMENT_APPROVAL_REQUIRED,
        help_text="The comment has been approved by an admin",
    )

    created = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time created",
    )
    modified = models.DateTimeField(
        auto_now=True,
        help_text="Date and time last modified",
    )

    objects =ReviewsManager()

    def is_updated(self):
        """
        Return false if review not modified, otherwise return datetime of update.
        """
        if self.modified - self.created > datetime.timedelta(0, UPDATED_COMPARISON_SECONDS):
            # modified datetime is within 10 sec of created datetime
            return self.modified
        else:
            return False

    def __unicode__(self):
        return "object: {o}, score: {s}, user: {u}".format(
                 o=self.reviewed_object, s=self.score, u=self.user.username)

    def save(self, *args, **kwargs):
        # set self.comment_approved if no comment
        if not self.comment:
            self.comment_approved = True

        super(Review, self).save(*args, **kwargs)