# TODO Найдите количество книг, которое можно разместить на дискете
k_str = 100
k_stro = 50
k_sim = 25
sim = 4
knigabit = k_str * k_stro * k_sim * sim
disk = 1.44
diskkb = disk * 1024
diskbit = diskkb * 1024
full_kniga = diskbit // knigabit
full_kniga = round(full_kniga)

print("Количество книг, помещающихся на дискету:", full_kniga)
