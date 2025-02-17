#!/bin/bash
#SBATCH --job-name=cel2D
#SBATCH --partition=astro3_short
#SBATCH --nodes=1
#SBATCH --mem=50G
#SBATCH --account=astro
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=28
export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK

srun ./build/celadro examples/bend_lowlowvolnoS/bend.dat -o /lustre/astro/rsx187/celadrodata/lowlowvolnoStest -t 28
