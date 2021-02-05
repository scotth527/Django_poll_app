from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question, Choice

# Create your tests here.

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is older than 1 days
        """
        time = timezone.now() - datetime.timedelta(days=2)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_current_question(self):
        """
        was_published_recently() returns True for questions whose pub_date is within a day
        """
        time = timezone.now()
        current_question = Question(pub_date=time)
        self.assertIs(current_question.was_published_recently(), True)