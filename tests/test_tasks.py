"""Test peridic tasks"""
# pylint: disable=unused-argument

import pytest
from flask_mail import Mail

from src.environment import MarketAlert
from src.tasks.messenger import daily_report_task, market_alert_task

task_list = [daily_report_task, market_alert_task]


@pytest.mark.parametrize(
    "task",
    task_list,
    ids=[task.name for task in task_list],
)
def test_tasks(client, _db, load_environment_data, task):
    """Test daily alert periodic celery task."""

    with Mail().record_messages() as outbox:
        task()
        assert len(outbox) == 1

    if task is not daily_report_task:
        alert = MarketAlert.find_by_id(1)
        assert not alert.active
