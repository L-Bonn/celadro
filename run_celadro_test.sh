#!/bin/bash
#SBATCH --job-name=cel2D
#SBATCH --partition=astro3_short
#SBATCH --nodes=1
#SBATCH --mem=50G
#SBATCH --account=astro
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=56
export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK

srun ./build/celadro examples/bend/bend.dat -o test5e-7 -t 56
