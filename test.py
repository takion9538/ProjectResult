import glob
import os

names = ['golden_pothos', 'Muehlenbeckia_complexa', 'happy_plant',
        'Bunnyearscactus', 'rosmarinus', 'Dracaena',
        'chlorophytum', 'monstera', 'chamaedorea_elegans', 'Bengal_Fig',
        'stuckyi', 'pachira', 'ardisia_crenata', 'zamia_plant',
        'staghorn_fern', 'Philodendron_Birkin', 'Wilma']

for name in names :

    for num in range(1, 301) :
        file = glob.glob(f'label/{name}_{num:03d}.txt')
        print(f'{file} file moved train')
        os.rename(file[0], f'label/train/{name}_{num:03d}.txt')

    for num in range(301, 401) :
        file = glob.glob(f'label/{name}_{num:03d}.txt')
        print(f'{file} file moved valid')
        os.rename(file[0], f'label/valid/{name}_{num:03d}.txt')
