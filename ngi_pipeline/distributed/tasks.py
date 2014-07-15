""" Module to define Celery tasks for NGI pipeline
"""

from celery.task import task

from ngi_pipeline import conductor

@task(ignore_results=True, queue="ngi_pipeline", name="launch_main_analysis")
def launch_main_analysis(run_dir):
    """ Will call the main method in ngi_pipeline.conductor module.

    This will create the corresponting directory structure and trigger
    the analysis based on the configuration file.

    :param: run_dir: Run directory to analyze
    """
    conductor.process_demultiplexed_flowcells([run_dir])
