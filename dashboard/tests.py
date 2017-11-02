import dramatiq

from django.test import TransactionTestCase

from .models import Job
from .tasks import process_job


class TestJobProcessing(TransactionTestCase):
    def setUp(self):
        super().setUp()

        self.broker = dramatiq.get_broker()
        self.worker = dramatiq.Worker(self.broker, worker_timeout=100)
        self.worker.start()

    def tearDown(self):
        super().tearDown()
        self.worker.stop()

    def test_can_process_jobs(self):
        # Given a web client
        # When I submit a job
        response = self.client.post("/", {"type": Job.TYPE_FAST})
        self.assertEqual(response.status_code, 302)

        # And wait for the queue and workers to complete
        self.broker.join(process_job.queue_name)
        self.worker.join()

        # Then I expect the job's status to be "done"
        job = Job.objects.get()
        self.assertEqual(job.status, Job.STATUS_DONE)
