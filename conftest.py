import os
import pytest


def get_project_root():
    path = os.path.join(os.path.dirname(__file__))
    return os.path.abspath(path)


@pytest.fixture(autouse=True, scope='session')
def make_dir():
    make_results_dir()


def make_results_dir():
    """"
    Make the reuired directory
    """
    PROJECT_ROOT = get_project_root()
    if not os.path.exists(os.path.join(PROJECT_ROOT, 'Results')):
        os.makedirs(os.path.join(PROJECT_ROOT, 'Results'))
    return os.path.join(PROJECT_ROOT, 'Results')


def get_test_data_directory():
    PROJECT_ROOT = get_project_root()
    return os.path.join(PROJECT_ROOT, "resource", "data")


def get_reports_directory():
    PROJECT_ROOT = get_project_root()
    return os.path.join(PROJECT_ROOT, "Results")
