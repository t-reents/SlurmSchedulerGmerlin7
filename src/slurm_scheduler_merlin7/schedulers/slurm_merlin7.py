from aiida.schedulers.plugins.slurm import SlurmScheduler


class CustomSlurmScheduler(SlurmScheduler):
    
    def _get_joblist_command(self, jobs=None, user=None):
        """The command to report full information on existing jobs.

        Separate the fields with the _field_separator string order:
        jobnum, state, walltime, queue[=partition], user, numnodes, numcores, title
        """
        command = super()._get_joblist_command(jobs=jobs, user=user)
        command = f"{command} --clusters=all"
        return command

    def _get_kill_command(self, jobid: str) -> str:
        """Return the command to kill the job with specified jobid."""
        kill_command = super()._get_kill_command(
            jobid=jobid
        )

        return f'{kill_command} --clusters=all'