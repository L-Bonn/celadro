#!/bin/bash
#SBATCH --job-name=celte
#SBATCH --partition=astro3_long
#SBATCH --nodes=1
#SBATCH --mem=56G
#SBATCH --account=astro
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=56
export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK

srun /groups/astro/rsx187/celadro/build/celadro /groups/astro/rsx187/celadro/runcard.dat --R=8 --omega=0.005 --gamma=0.05 --zetaS=0.0001 --Rnew=4 --time_Rnew=20000 --nsteps=40000 --nphases=112 --LX=150 --LY=150 --xi=1 -t 112 --output="/lustre/astro/rsx187/celadrodata/tryRchangezSchange/" >> out/slurm-$SLURM_JOB_ID.out 
#srun /groups/astro/rsx187/celadro/build/celadro /groups/astro/rsx187/celadro/runcard.dat --R=8 --omega=0.005 --gamma=0.05 --zetaS=0.0001 --Rnew=4 --time_Rnew=100 --nsteps=200 --nphases=112 --LX=150 --LY=150 --xi=1 -t 112 --output="/lustre/astro/rsx187/celadrodata/tryRchange250825short/" >> out/slurm-$SLURM_JOB_ID.out 
#srun /groups/astro/rsx187/celadro/build/celadro /groups/astro/rsx187/celadro/runcard.dat --R=8 --omega=0.005 --gamma=0.05 --zetaS=0.0001 --Rnew=4 --time_Rnew=7000 --nsteps=10000 --nphases=10 --LX=50 --LY=50 --xi=1 -t 112 --output="/lustre/astro/rsx187/celadrodata/tryRchange250825small/" >> out/slurm-$SLURM_JOB_ID.out 
