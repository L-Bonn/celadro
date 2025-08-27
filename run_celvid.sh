#!/bin/bash
#SBATCH --job-name=celvid
#SBATCH --partition=astro3_short
#SBATCH --nodes=1
#SBATCH --mem=30G
#SBATCH --account=astro
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10

export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK
module load astro
module load ffmpeg/4.3.1

srun /groups/astro/rsx187/anaconda3/bin/python celvid.py --slurmd-debug=4 >> vout/slurm-$SLURM_JOB_ID.out
