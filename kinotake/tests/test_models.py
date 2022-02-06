from django.test import TestCase
from kinotake.models import Vote

# Create your tests here.
class VoteModelTests(TestCase):

    def test_is_empty(self):
        saved_votes = Vote.objects.all()
        self.assertEqual(saved_votes.count(), 1)

    def test_is_count_one(self):
        vote = Vote(target=Vote.KINOKO, comment='test_text')
        vote.save()
        saved_votes = Vote.objects.all()
        self.assertEqual(saved_votes.count(), 1)

    def test_saving_and_retrieving_post(self):
        vote = Vote()
        target = Vote.TAKENOKO
        comment = 'test_text_to_retrieve'
        vote.target = target
        vote.comment = comment
        vote.save()

        saved_votes = Vote.objects.all()
        actual_vote = saved_votes[0]

        self.assertEqual(actual_vote.target, target)
        self.assertEqual(actual_vote.comment, comment)
