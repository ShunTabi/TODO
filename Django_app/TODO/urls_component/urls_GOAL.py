from django.urls import path
from ..views_component import views_GOAL

GOAL_TOP = path("GOAL_TOP/<int:page>",views_GOAL.GOAL_TOP,name="GOAL_TOP")
GOAL_FORM = path("GOAL_FORM/",views_GOAL.GOAL_FORM,name="GOAL_FORM")
GOAL_UPDATE = path("GOAL_UPDATE/",views_GOAL.GOAL_UPDATE,name="GOAL_UPDATE")
GOAL_DEL = path("GOAL_DEL/",views_GOAL.GOAL_DEL,name="GOAL_DEL")