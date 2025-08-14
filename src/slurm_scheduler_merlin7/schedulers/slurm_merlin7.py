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