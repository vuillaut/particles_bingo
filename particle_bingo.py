t matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython.display import display, Markdown, Latex
import numpy as np
import copy



particles_names = ['u', 'c', 't', 'g',
                   'd', 's', 'b', 'gamma',
                   'nu_e', 'nu_mu', 'nu_tau', 'w',
                   'e', 'mu', 'tau', 'z']


src_dir = 'particles/'



u = mpimg.imread(src_dir + 'u.png')
c = mpimg.imread(src_dir + 'c.png')
t = mpimg.imread(src_dir + 't.png')
g = mpimg.imread(src_dir + 'g.png')
d = mpimg.imread(src_dir + 'd.png')
s = mpimg.imread(src_dir + 's.png')
b = mpimg.imread(src_dir + 'b.png')
gamma = mpimg.imread(src_dir + 'gamma.png')
nu_e = mpimg.imread(src_dir + 'nu_e.png')
nu_mu = mpimg.imread(src_dir + 'nu_mu.png')
nu_tau = mpimg.imread(src_dir + 'nu_tau.png')
w = mpimg.imread(src_dir + 'w.png')
e = mpimg.imread(src_dir + 'e.png')
mu = mpimg.imread(src_dir + 'mu.png')
tau = mpimg.imread(src_dir + 'tau.png')
z = mpimg.imread(src_dir + 'z.png')
h = mpimg.imread(src_dir + 'h.png')
red = mpimg.imread(src_dir + 'red_square.png')
blue = mpimg.imread(src_dir + 'blue_square.png')
green = mpimg.imread(src_dir + 'green_square.png')
yellow = mpimg.imread(src_dir + 'yellow_square.png')



particles_images = [u, c, t, g,
                    d, s, b, gamma,
                    nu_e, nu_mu, nu_tau, w,
                    e, mu, tau, z]

quarks = [u, c, t, d, b, s]
leptons = [nu_e, nu_mu, nu_tau, e, mu, tau]
bosons = [g, gamma, w, z, red, h]



particles_dic = {}
for i,p in enumerate(particles_names):
    particles_dic[p] = particles_images[i]




def remove_axes(ax):
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])



nn = 3
mm = 6
fig, axes = plt.subplots(nn, mm, figsize=(18,9))
for ax in axes.ravel():
    remove_axes(ax)
    # ax.imshow(particles_dic[p])
for i, ax in enumerate(axes[0]):
    ax.imshow(quarks[i])
for i, ax in enumerate(axes[1]):
    ax.imshow(leptons[i])
for i, ax in enumerate(axes[2]):
    ax.imshow(bosons[i])



fig.savefig("grids/complete.png", dpi=200)



family_names = [quarks, leptons, bosons]
family_colors = [blue, green, red]



empty_fig, empty_axes = plt.subplots(nn, mm, figsize=(18, 9))
for n in range(nn):
    for m in range(mm):
        ax = empty_axes[n, m]
        remove_axes(ax)
        ax.imshow(family_colors[n])



number_of_grids = 50
for grid in range(number_of_grids):
    nn, mm = empty_axes.shape
    for n in range(nn):
        for m in range(mm):
            ax = empty_axes[n][m]
            ax.clear()
            remove_axes(ax)
            ax.imshow(family_colors[n])
        i = np.random.randint(0,6)
        j = i
        while j==i:
            j = np.random.randint(0,6)
        for k in range(mm):
            if k!=i and k!=j:
                empty_axes[n][k].imshow(family_names[n][k])

    # display(empty_fig)
    empty_fig.savefig("grids/{}.png".format(grid), dpi=100)
