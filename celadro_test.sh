#!/bin/bash
#SBATCH --job-name=cel
#SBATCH --partition=astro3_short
#SBATCH --nodes=1
#SBATCH --mem=50G
#SBATCH --account=astro
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK

srun ./build/celadro examples/bend/bend.dat -o test -t 32
