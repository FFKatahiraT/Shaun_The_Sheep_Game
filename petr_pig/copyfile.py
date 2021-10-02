from shutil import copy

for i in range(4):
	copy('petr_pig.png', 'petr_pig_walk_back'+str(i+1)+'.png')
	copy('petr_pig.png', 'petr_pig_walk_front'+str(i+1)+'.png')
	copy('petr_pig.png', 'petr_pig_walk_right'+str(i+1)+'.png')
	copy('petr_pig.png', 'petr_pig_walk_left'+str(i+1)+'.png')
	copy('petr_pig.png', 'petr_pig_eat_front'+str(i+1)+'.png')