from rest_framework import routers
from .views import *



# define all urls related to the users app
router = routers.DefaultRouter()

router.register("customer",CustomerViewSet,basename="customers")
router.register("project",ProjectViewSet,basename="projects")
router.register("survey",SurveyViewSet, basename="surveys")
router.register("questions",QuestionViewSet, basename="questions")
router.register("answers",QuestionAnswerViewSet, basename="answers")

urlpatterns = router.urls