import sys
import os
from multiprocessing import Pool
import matplotlib.pyplot as plt 
import subprocess
import glob


sys.path.insert(0, "/groups/astro/rsx187/celadro/plot/")

import plot
import archive
import animation

##################################################
# Init

# if len(sys.argv) == 1:
#     print("Please provide an input file.")
#     exit(1)

# # load archive from file
# ar = archive.loadarchive(sys.argv[1])

# oname = ""
# if len(sys.argv) == 3:
#     oname = "movie_" + sys.argv[2]
#     print("Output name is", sys.argv[2])

### plot

def frame_im(tup):

    i, ar = tup
    print(i)
    frame = ar.read_frame(i) 

    fig = plt.figure(dpi=300)

    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    plot.cells(frame, ax1)
    plot.nematic(frame, ax1)

    plot.nematic_field(frame, engine=ax2, avg=2, show_def=True)

    for ax in [ax1, ax2]:
        ax.axes.set_aspect("equal", adjustable="box")
        ax.set_xlim([0, frame.parameters["Size"][0] - 1])
        ax.set_ylim([0, frame.parameters["Size"][1] - 1])
        ax.axis("off")
    iframe = i*ar.ninfo + ar.nstart
    ax.set_title(f'frame: {iframe:06}, R = {ar.R}')

    fig.savefig("tempsavepngs/file%02d.png" % i)
    plt.close(fig)


def vid(pname, ntasks=1):
    try:
        ar = archive.loadarchive(pname+'/')
        Nideal = int((ar.nsteps-ar.nstart)/ar.ninfo)
        Nreal = len(glob.glob(pname+'/*'))-1
        print(f'Nideal = {Nideal}, Nreal = {Nreal}')
        N = min(Nreal, Nideal)
        print('start making vid', flush=True)
        with Pool(ntasks) as p:
            mylist = [(i, ar) for i in range(N)]
            csize = int(len(mylist)/ntasks)+1
            p.map(frame_im, mylist, chunksize=csize)
    #for i, frame in enumerate(ar.read_frames()):
    except FileNotFoundError:
        print(f"file not found!, {pname} likely didn't finish")
        return
        
    os.chdir("tempsavepngs")

    name = pname.split('/')[-1]
    print(f"pname: {pname}, name: {name}")
    subprocess.call(['ffmpeg','-y', '-framerate', '8', '-i', 'file%02d.png', '-r', '30', '-pix_fmt', 'yuv420p',
                f'../vids/{name}celadrovid.mp4'
            ])
    for file_name in glob.glob("*.png"):
        os.remove(file_name)

    os.chdir('../')
    del ar
    print(f'done {pname}')


if __name__ == '__main__':

    #path = '/lustre/astro/rsx187/celadrodata/test_events/*'
    #path = '/lustre/astro/rsx187/celadrodata/low*'
    #path = '/lustre/astro/rsx187/celadrodata/test_omega/*'
    #path = '/lustre/astro/rsx187/celadrodata/test_gamma/*'
    #path = '/lustre/astro/rsx187/celadrodata/test_xi_big/*'
    #path = '/lustre/astro/rsx187/celadrodata/test_zS_big/*'#test_omega_zS_big
    #path = '/lustre/astro/rsx187/celadrodata/test_omega_zS_big/*'#
    path = '/lustre/astro/rsx187/celadrodata/tryRchangez*omega*'#

    #path = sys.argv[1]
    names = glob.glob(path)
    #names = [name for name in names if 'zeta' not in name]
    print(names)
    ntasks = int(os.environ['SLURM_CPUS_PER_TASK'])
    #ntasks = 40
    print('ntasks:', ntasks, type(ntasks))
    
    #sys.exit()

    if 'parameters.json' in names: # is it already the path to the archive
        vid(path, ntasks)
    else:
        pnames = names
        [print(name) for name in pnames]
        #sys.exit()
        for pname in pnames:
            vid(pname, ntasks)
