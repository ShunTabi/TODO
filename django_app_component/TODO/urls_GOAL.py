from django.urls import path
from .views import views_GOAL


GOAL_TOP = path(
    'GOAL_TOP/<int:GOAL_PAGE>',
    views_GOAL.GOAL_TOP,
    name="GOAL_TOP"
)

GOAL_FORM = path(
    'GOAL_FORM/',
    views_GOAL.GOAL_FORM,
    name="GOAL_FORM"
)
GOAL_FORM_UPDATE = path(
    'GOAL_FORM/<int:GOAL_ID>',
    views_GOAL.GOAL_FORM_UPDATE,
    name="GOAL_FORM_UPDATE"
)
GOAL_TOP_DEL = path(
    'GOAL_TOP_DEL/<int:GOAL_PAGE>',
    views_GOAL.GOAL_TOP_DEL,
    name="GOAL_TOP_DEL"
)
GOAL_DEL = path(
    'GOAL_DEL/<int:GOAL_ID>',
    views_GOAL.GOAL_DEL,
    name="GOAL_DEL"
)
