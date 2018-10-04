import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython.display import display, Markdown, Latex
import numpy as np



## DEFINING PARTICLES and LOADING THEIR IMAGES

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


particles_images = [u, c, t, g,
                    d, s, b, gamma,
                    nu_e, nu_mu, nu_tau, w,
                    e, mu, tau, z]


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


fig, axes = plt.subplots(n,m, figsize=(14,14))
for ax, p in zip(axes.ravel(), particles_names):
    remove_axes(ax)
    # ax.imshow(particles_dic[p])

fig.savefig("grids/complete.png")


for number_grids in range(40):
    for ax in axes.ravel():
        ax.set_visible(True)

    for k in range(m):
        i = np.random.randint(0,4)
        j=i
        while j==i:
            j = np.random.randint(0,4)
        axes[k][i].set_visible(False)
        axes[k][j].set_visible(False)
    fig.savefig("grids/{}.png".format(number_grids))
