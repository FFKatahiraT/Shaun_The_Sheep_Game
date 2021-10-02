import pygame
import random
import math

class mission1():
	#Прописывание сюжета
	def __init__(self):
		self.checkpoints_pos_xy = []
		self.checkpoints_map_xy = []
		self.checkpoint_counter= 0
		self.tips = []
		self.event = [1,1,1,1,1,1,1,1]			#Заполняем event нулями
		self.mission_done = False
		#Чекпоинт 0
		self.checkpoints_pos_xy.append([Lama_Jennie.pos_x, Lama_Jennie.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Надо поговорить с ламой.')
		#Чекпоинт 1
		self.checkpoints_pos_xy.append([Cow_Marcus.pos_x, Cow_Marcus.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Надо поговорить с коровой Маркусом.')
		#Чекпоинт 2
		self.checkpoints_pos_xy.append([Pig_Petr.pos_x, Pig_Petr.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Надо поговорить со свиньей Петр.')
		#Чекпоинт 3
		self.checkpoints_pos_xy.append([Pig_Petr.pos_x, Pig_Petr.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y+1])
		self.tips.append('Надо отправиться на север, на другие поля')
		#Чекпоинт 4
		self.checkpoints_pos_xy.append([Cow_Marcus.pos_x, Cow_Marcus.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Надо вернуться к корове Маркусу')
		#Чекпоинт 5
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x+1, map_y])
		self.tips.append('Надо отправиться на восток, на другие поля')
		#Чекпоинт 6
		self.checkpoints_pos_xy.append([Cow_Marcus.pos_x, Cow_Marcus.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Нужно вернуться к своим')
		#Чекпоинт 7
		self.checkpoints_pos_xy.append([Cow_Marcus.pos_x, Cow_Marcus.pos_y])
		self.checkpoints_map_xy.append([map_x+1, map_y])
		self.tips.append('Нужно пойти на поле к востоку')

	def checkpoint_reached(self):
		global AI_neutral_list, AI_friends_list, neutral_moving_sprites, friends_moving_sprites
		global max_plants_Q
		if self.checkpoint_counter == 0:
			max_plants_Q = 20
			dialogs(Lama_Jennie, 'Привет! Меня зовут Дженни, помнишь меня?')
			dialogs(Lama_Jennie, 'Мы были на одном пастбище, пока его не снес ураган позавчера')
			dialogs(Lama_Jennie, 'Корова Маркус наш лидер, вчера совсем сошел с катушек')
			dialogs(Lama_Jennie, 'Надеюсь, ты впорядке после вчерашнего избиения')
			dialogs(Lama_Jennie, 'Сейчас все адекватные, нужна твоя помощь. Подойди к корове Маркусу.')
		elif self.checkpoint_counter == 1:
			dialogs(Cow_Marcus, 'Привет. Как состояние?')
			dialogs(Cow_Marcus, 'Свинья Петр до сих пор не оклемался от позавчерашнего')
			dialogs(Cow_Marcus, 'Выпил ту мутную жижу из разбитой бочки. Вчера было хорошо, а сейчас...')
			dialogs(Cow_Marcus, 'Сходи к нему, выгуляй на свежем воздухе этого алкаша')
			dialogs(Cow_Marcus, 'Потом приходи сюда. Будет собрание')
		elif self.checkpoint_counter == 2:
			dialogs(Pig_Petr, 'Эээй, ты! Тебе мало?')
			dialogs(Pig_Petr, 'Ой. На полях к северу я видел растения. Пошли поедим')
			del AI_neutral_list[AI_neutral_list.index(Pig_Petr)]
			AI_friends_list.append(Pig_Petr)
			friends_moving_sprites = spawn_animals(AI_friends_list)
			neutral_moving_sprites = spawn_animals(AI_neutral_list)
			Pig_Petr.health = 1
		elif self.checkpoint_counter == 3:
			dialogs(Pig_Petr, 'Отлично! Сейчас я нажрусь!')
			dialogs(Pig_Petr, 'Ой, то есть поем...')
		elif self.checkpoint_counter == 4:
			max_plants_Q = 30
			dialogs(Cow_Marcus, 'Итак, собрание начинается!')
			dialogs(Cow_Marcus, 'Людей не видно. Будто испарились')
			dialogs(Cow_Marcus, 'Теперь мы сами по себе')
			dialogs(Cow_Marcus, 'Если чувствуете, что слабы, ешьте растения')
			dialogs(Cow_Marcus, 'Они восстановят ваши силы')
			dialogs(Lama_Jennie, 'Здесь очень много кур, что с ними делать?')
			dialogs(Cow_Marcus, 'НИЧЕГО, они что тебе мешают?')
			dialogs(Lama_Jennie, 'Из-за них могут придти волки')
			dialogs(Cow_Marcus, 'В гробу я видел твоих волков')
			dialogs(Cow_Marcus, 'Овца, иди на восток, разведай обстановку')
			dialogs(Cow_Marcus, 'Нам пора мигрировать. Собрание окончено')
			del AI_friends_list[AI_friends_list.index(Pig_Petr)]
			AI_neutral_list.append(Pig_Petr)
			friends_moving_sprites = spawn_animals(AI_friends_list)
			neutral_moving_sprites = spawn_animals(AI_neutral_list)
		elif self.checkpoint_counter == 5:	
			dialogs(Sheep_player, 'Кажется, местечко что надо')
			dialogs(Sheep_player, 'Пора возвращаться к своим')
		elif self.checkpoint_counter == 6:	
			dialogs(Cow_Marcus, 'Как там место?')
			dialogs(Sheep_player, 'Волков нет, еды много')
			dialogs(Cow_Marcus, 'Тогда выдвигаемся')
			dialogs(Cow_Marcus, 'Веди нас!')
			del AI_neutral_list[AI_neutral_list.index(Pig_Petr)]
			del AI_neutral_list[AI_neutral_list.index(Cow_Marcus)]
			del AI_neutral_list[AI_neutral_list.index(Lama_Jennie)]
			AI_friends_list.append(Pig_Petr)
			AI_friends_list.append(Cow_Marcus)
			AI_friends_list.append(Lama_Jennie)
			friends_moving_sprites = spawn_animals(AI_friends_list)
			neutral_moving_sprites = spawn_animals(AI_neutral_list)
		elif self.checkpoint_counter == 7:
			dialogs(Cow_Marcus, 'Отлично! Располагаемся!')
			AI_friends_list = []
			AI_neutral_list.append(Pig_Petr)
			AI_neutral_list.append(Cow_Marcus)
			AI_neutral_list.append(Lama_Jennie)
			friends_moving_sprites = spawn_animals(AI_friends_list)
			neutral_moving_sprites = spawn_animals(AI_neutral_list)	
			splash_screen(mission1_complete_img)

		if self.checkpoint_counter < len(self.checkpoints_pos_xy) - 1:
			self.checkpoint_counter += 1
		else:
			#Миссия выполнена
			self.mission_done = True

	def update(self):
		self.checkpoints_pos_xy[0] = [Lama_Jennie.pos_x, Lama_Jennie.pos_y]
		self.checkpoints_pos_xy[1] = [Cow_Marcus.pos_x, Cow_Marcus.pos_y]
		self.checkpoints_pos_xy[2] = [Pig_Petr.pos_x, Pig_Petr.pos_y]
		self.checkpoints_pos_xy[3] = [Pig_Petr.pos_x, Pig_Petr.pos_y]
		self.checkpoints_pos_xy[4] = [Cow_Marcus.pos_x, Cow_Marcus.pos_y]
		self.checkpoints_pos_xy[5] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_pos_xy[6] = [Cow_Marcus.pos_x, Cow_Marcus.pos_y]
		self.checkpoints_pos_xy[7] = [Cow_Marcus.pos_x, Cow_Marcus.pos_y]


class mission2():
	#Прописывание сюжета
	def __init__(self):
		global AI_neutral_list, neutral_moving_sprites, player_moving_sprite, map_x, map_y
		map_x = 4
		map_y = 3
		Cow_Marcus.pos_x, Cow_Marcus.pos_y = random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100)
		Cow_Marcus.map_pos_x, Cow_Marcus.map_pos_y = 4, 3
		Lama_Jennie.pos_x, Lama_Jennie.pos_y = random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100)
		Lama_Jennie.map_pos_x, Lama_Jennie.map_pos_y = 4, 3
		Pig_Petr.pos_x, Pig_Petr.pos_y = random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100)
		Pig_Petr.map_pos_x, Pig_Petr.map_pos_y = 4, 3
		Sheep_player.pos_x, Sheep_player.pos_y = random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100)
		Sheep_player.map_pos_x, Sheep_player.map_pos_y = 4, 3
		player_moving_sprite = spawn_animals([Sheep_player])
		neutral_moving_sprites = spawn_animals(AI_neutral_list)
		self.checkpoints_pos_xy = []
		self.checkpoints_map_xy = []
		self.checkpoint_counter= 0
		self.tips = []
		self.event = [1,1,1,1,1,1,1,0,1]			#Заполняем event нулями
		self.mission_done = False
		#Чекпоинт 0
		self.checkpoints_pos_xy.append([Lama_Jennie.pos_x, Lama_Jennie.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Навестить бы ламу Дженни')
		#Чекпоинт 1
		self.checkpoints_pos_xy.append([Cow_Marcus.pos_x, Cow_Marcus.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Интересно, как там Маркус')
		#Чекпоинт 2
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y+2])
		self.tips.append('Надо пройти 2 поля на север')
		#Чекпоинт 3
		self.checkpoints_pos_xy.append([Cow_Marcus.pos_x, Cow_Marcus.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Пора вернуться к Маркусу')
		#Чекпоинт 4
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Пройду ка 2 поля на север')
		#Чекпоинт 5
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y+2])
		self.tips.append('Пройду ка 2 поля на север')
		#Чекпоинт 6
		self.checkpoints_pos_xy.append([Cow_Marcus.pos_x, Cow_Marcus.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Вернусь на базу к Маркусу')
		#Чекпоинт 7
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Можно и прогуляться вокруг')
		#Чекпоинт 8
		self.checkpoints_pos_xy.append([Cow_Marcus.pos_x, Cow_Marcus.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Нужно сказать Маркусу, что тут волки')
	
	def checkpoint_reached(self):
		global AI_neutral_list, AI_friends_list, neutral_moving_sprites, friends_moving_sprites
		global max_plants_Q, Chicken1
		if self.checkpoint_counter == 0:
			max_plants_Q = 20
			dialogs(Lama_Jennie, 'Доброе утро!')
			dialogs(Lama_Jennie, 'Корова Маркус что-то говорил про план')
			dialogs(Lama_Jennie, 'Подойди к нему')
		elif self.checkpoint_counter == 1:
			dialogs(Cow_Marcus, 'Привет! А вот и ты проснулся')
			dialogs(Cow_Marcus, 'Итак, первым делом нам нужно разведать местность')
			dialogs(Cow_Marcus, 'Если вокруг нет волков, то мы останемся тут')
			dialogs(Cow_Marcus, 'Петр, пройди пару полей на юг')
			dialogs(Pig_Petr, 'Без проблем')
			dialogs(Cow_Marcus, 'Дженни пройди 2 поля на восток')
			dialogs(Lama_Jennie, 'Хорошо')
			dialogs(Cow_Marcus, 'Овца, тебе придется пойти на север')
			dialogs(Sheep_player, 'Ок')
			dialogs(Cow_Marcus, 'Я пойду на запад')
		elif self.checkpoint_counter == 2:
			dialogs(Sheep_player, 'Кажется, все чисто')
			dialogs(Sheep_player, 'Пора возвращаться')
		elif self.checkpoint_counter == 3:
			dialogs(Cow_Marcus, 'Все вернулись')
			dialogs(Cow_Marcus, 'Петр, все чисто?')
			dialogs(Pig_Petr, 'Очевидно да, раз я живой')
			dialogs(Cow_Marcus, 'Дженни?')
			dialogs(Lama_Jennie, 'Волков нет')
			dialogs(Sheep_player, 'На севере все чисто')
			dialogs(Cow_Marcus, 'Отлично. Отдыхаем')
			dialogs(Cow_Marcus, 'Как в округе кончится еда, уйдем в другое место')
			Chicken1 = animal('chicken', random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100))
			Chicken1.map_pos_x = Sheep_player.map_pos_x
			Chicken1.map_pos_y = Sheep_player.map_pos_y
			AI_neutral_list.append(Chicken1)
			neutral_moving_sprites.add(Chicken1)
		elif self.checkpoint_counter == 4:
			dialogs(Chicken1, 'ВОЛКИ!!! Я ВИДЕЛА ВОЛКОВ!')
			dialogs(Cow_Marcus, 'Что?!')
			dialogs(Cow_Marcus, 'Мы же все проверили, нет волков')
			dialogs(Chicken1, 'Они близко! К северу от нас')
			dialogs(Cow_Marcus, 'Овца, проверь есть ли волки на севере')
			dialogs(Sheep_player, 'Я? Ну... ладно')
			dialogs(Sheep_player, 'Все равно хотел прогуляться')
			dialogs(Cow_Marcus, 'Кура, ты пойдешь с ним')
			dialogs(Chicken1, 'Я туда ни ногой!')
			dialogs(Sheep_player, '....')
			dialogs(Sheep_player, 'Пойду я')
		elif self.checkpoint_counter == 5:
			dialogs(Sheep_player, 'Странно. Волков нет')
			dialogs(Sheep_player, 'Может кура наврала')
			dialogs(Sheep_player, 'Чтож вернусь на базу')
		elif self.checkpoint_counter == 6:
			dialogs(Sheep_player, 'Итак. Официально заявляю')
			dialogs(Sheep_player, 'Что волков там нет')
			dialogs(Cow_Marcus, 'Кура нас ообманула?')
			dialogs(Chicken1, 'Волки к югу! ТАМ МОЯ СЕМЬЯ! Спасите!')
			dialogs(Pig_Petr, 'Этих кур что-то развелось')
			dialogs(Lama_Jennie, 'Растений от них больше не становится')
			dialogs(Cow_Marcus, 'Кура, почему ты не с семьей тогда?')
			dialogs(Cow_Marcus, 'Вот иди их и спасай')
			del AI_neutral_list[AI_neutral_list.index(Chicken1)]
			generate_npc(0, 20)
			dialogs(Sheep_player, 'Ну а я прогуляюсь')
		elif self.checkpoint_counter == 7:	
			dialogs(Sheep_player, 'Волки?')
			dialogs(Sheep_player, 'ВОЛКИ!!!')
			dialogs(Sheep_player, 'Откуда они тут взялись?')
			dialogs(Sheep_player, 'Может, кура и не врала')
			dialogs(Sheep_player, 'Надо срочно бежать к Маркусу и сообщить')
		elif self.checkpoint_counter == 8:	
			dialogs(Sheep_player, 'Маркус! Волки действительно здесь!')
			dialogs(Cow_Marcus, 'Хмм. Какие волки?')
			dialogs(Lama_Jennie, 'Куры заполнили эти поля, на них и пришли волки')
			dialogs(Cow_Marcus, 'Давайте нажремся впрок')
			dialogs(Cow_Marcus, 'У волков есть куры, им не до нас')
			splash_screen(mission2_complete_img)

		if self.checkpoint_counter < len(self.checkpoints_pos_xy) - 1:
			self.checkpoint_counter += 1
		else:
			#Миссия выполнена
			self.mission_done = True	

	def update(self):
		self.checkpoints_pos_xy[0] = [Lama_Jennie.pos_x, Lama_Jennie.pos_y]
		self.checkpoints_pos_xy[1] = [Cow_Marcus.pos_x, Cow_Marcus.pos_y]
		self.checkpoints_pos_xy[2] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_pos_xy[3] = [Cow_Marcus.pos_x, Cow_Marcus.pos_y]
		self.checkpoints_pos_xy[4] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_pos_xy[5] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_pos_xy[6] = [Cow_Marcus.pos_x, Cow_Marcus.pos_y]
		self.checkpoints_pos_xy[7] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_map_xy[7] = [Sheep_player.map_pos_x, Sheep_player.map_pos_y]
		self.event[7] = bool(len(enemy_moving_sprites))
		self.checkpoints_pos_xy[8] = [Cow_Marcus.pos_x, Cow_Marcus.pos_y]


class mission3():
	#Прописывание сюжета
	def __init__(self):
		global AI_neutral_list, neutral_moving_sprites, player_moving_sprite, map_x, map_y
		map_x = 4
		map_y = 3
		Cow_Marcus.pos_x, Cow_Marcus.pos_y = random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100)
		Cow_Marcus.map_pos_x, Cow_Marcus.map_pos_y = 4, 3
		Lama_Jennie.pos_x, Lama_Jennie.pos_y = random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100)
		Lama_Jennie.map_pos_x, Lama_Jennie.map_pos_y = 4, 3
		Pig_Petr.pos_x, Pig_Petr.pos_y = random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100)
		Pig_Petr.map_pos_x, Pig_Petr.map_pos_y = 4, 3
		Sheep_player.pos_x, Sheep_player.pos_y = random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100)
		Sheep_player.map_pos_x, Sheep_player.map_pos_y = 4, 3
		player_moving_sprite = spawn_animals([Sheep_player])
		neutral_moving_sprites = spawn_animals(AI_neutral_list)
		Lama_Jennie.health = 5
		generate_npc(0, 30)
		max_plants_Q = 10
		self.checkpoints_pos_xy = []
		self.checkpoints_map_xy = []
		self.checkpoint_counter= 0
		self.tips = []
		self.event = [1,1,0,1,1,1,0,1,1]			#Заполняем event еденицами
		self.mission_done = False
		#Чекпоинт 0
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('******** была ночка')
		#Чекпоинт 1
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Вот бы с Дженни погулять')
		#Чекпоинт 2
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([Sheep_player.map_pos_x, Sheep_player.map_pos_y])
		self.tips.append('Пора уходить')
		#Чекпоинт 3
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('')
		#Чекпоинт 4
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Бежать?')
		#Чекпоинт 5
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Дженни метрва?')
		#Чекпоинт 6
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([Sheep_player.map_pos_x, Sheep_player.map_pos_y])
		self.tips.append('Нужно найти безопасное место')
		#Чекпоинт 7
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Нужно найти безопасное место')
		#Чекпоинт 8
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('Нужно найти безопасное место')
	
	
	def checkpoint_reached(self):
		global AI_neutral_list, AI_friends_list, AI_enemy_list, neutral_moving_sprites, friends_moving_sprites, enemy_moving_sprites
		global max_plants_Q, Wolf1, Pig_Petr, berserk_mode
		if self.checkpoint_counter == 0:
			Sheep_player.health = 5	
			dialogs(Sheep_player, 'Какой прекрасный день!')
			for i in range(2):
				Wolf_temp =  animal('wolf', random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100))
				Wolf_temp.map_pos_x = Sheep_player.map_pos_x
				Wolf_temp.map_pos_y = Sheep_player.map_pos_y
				AI_enemy_list.append(Wolf_temp)
				enemy_moving_sprites.add(Wolf_temp)
			Wolf1 =  animal('wolf', random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100))
			Wolf1.map_pos_x = Sheep_player.map_pos_x
			Wolf1.map_pos_y = Sheep_player.map_pos_y
			AI_enemy_list.append(Wolf1)
			enemy_moving_sprites.add(Wolf1)
		elif self.checkpoint_counter == 1:
			background_music('enemy') #Включаем фоновую музыку
			dialogs(Wolf1, 'Добыча покрупнее')
			dialogs(Wolf1, 'Взять их!')
			dialogs(Pig_Petr, 'Я съебую отсюда')
			del AI_neutral_list[AI_neutral_list.index(Pig_Petr)]
			Pig_Petr = animal('petr_pig', Pig_Petr.pos_x, Pig_Petr.pos_y)
			AI_neutral_list.append(Pig_Petr)
			del AI_neutral_list[AI_neutral_list.index(Lama_Jennie)]
			AI_friends_list.append(Lama_Jennie)
			friends_moving_sprites = spawn_animals(AI_friends_list)
			neutral_moving_sprites = spawn_animals(AI_neutral_list)
		elif self.checkpoint_counter == 2:
			dialogs(Lama_Jennie, 'Куда же мы теперь пойдем?')
			dialogs(Sheep_player, 'Не надоело вечно убегать?')
			Wolf1.map_pos_x = Sheep_player.map_pos_x
			Wolf1.map_pos_y = Sheep_player.map_pos_y
			AI_enemy_list.append(Wolf1)
			enemy_moving_sprites.add(Wolf1)
		elif self.checkpoint_counter == 3:
			dialogs(Wolf1, 'Я нашел их!')
		elif self.checkpoint_counter == 4:
			dialogs(Lama_Jennie, 'Неет!')
			dialogs(Lama_Jennie, 'Беги!')
			del AI_friends_list[AI_friends_list.index(Lama_Jennie)]
			AI_neutral_list.append(Lama_Jennie)
			friends_moving_sprites = spawn_animals(AI_friends_list)
			neutral_moving_sprites = spawn_animals(AI_neutral_list)
			for i in range(7):
				Wolf_temp =  animal('wolf',random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100))
				Wolf_temp.map_pos_x = Sheep_player.map_pos_x
				Wolf_temp.map_pos_y = Sheep_player.map_pos_y
				AI_enemy_list.append(Wolf_temp)
				enemy_moving_sprites.add(Wolf_temp)
		elif self.checkpoint_counter == 5:
			dialogs(Sheep_player, 'Дженни!')
			dialogs(Wolf1, 'Уведите ее!')
			dialogs(Sheep_player, 'Я вас всех убью!')
			Lama_Jennie.map_pos_x, Lama_Jennie.map_pos_y = 0, map_size_y
			neutral_moving_sprites = spawn_animals(AI_neutral_list)
			berserk_mode = True
		elif self.checkpoint_counter == 6:
			dialogs(Sheep_player, 'Это место кажется безопасным')
			dialogs(Sheep_player, 'Куда они увели Дженни?')
			dialogs(Sheep_player, 'Она жива, я знаю')
			Lama_Jennie.map_pos_x, Lama_Jennie.map_pos_y = Sheep_player.map_pos_x, Sheep_player.map_pos_y
			neutral_moving_sprites = spawn_animals(AI_neutral_list)
		elif self.checkpoint_counter == 7:
			dialogs(Lama_Jennie, 'Хах конечно жива. Ищи большую воду')
			dialogs(Sheep_player, 'Ты жива!')
			dialogs(Lama_Jennie, 'Там и я')
			dialogs(Sheep_player,'Что?')
			Lama_Jennie.map_pos_x, Lama_Jennie.map_pos_y = 1, map_size_y
			neutral_moving_sprites = spawn_animals(AI_neutral_list)
		elif self.checkpoint_counter == 8:
			dialogs(Sheep_player, 'Дженни!')
			dialogs(Sheep_player, 'Где же большая вода?')
			max_plants_Q = 3
			splash_screen(mission3_complete_img)
			# i=0
			# while i < len(AI_enemy_list):
			# 	if AI_enemy_list[i].map_pos_x == 0 and AI_enemy_list[i].map_pos_y == 0:
			# 		del AI_enemy_list[i]
			# 	else:
			# 		i+=1


		if self.checkpoint_counter < len(self.checkpoints_pos_xy) - 1:
			self.checkpoint_counter += 1
		else:
			#Миссия выполнена
			self.mission_done = True

	def update(self):
		self.checkpoints_pos_xy[0] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_pos_xy[1] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_pos_xy[2] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_map_xy[2] = [Sheep_player.map_pos_x, Sheep_player.map_pos_y]
		self.event[2] = not bool(len(enemy_moving_sprites))
		self.checkpoints_pos_xy[3] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_map_xy[3] = [Sheep_player.map_pos_x, Sheep_player.map_pos_y]
		self.checkpoints_pos_xy[4] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_map_xy[4] = [Sheep_player.map_pos_x, Sheep_player.map_pos_y]
		self.checkpoints_pos_xy[5] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_map_xy[5] = [Sheep_player.map_pos_x, Sheep_player.map_pos_y]
		self.checkpoints_pos_xy[6] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_map_xy[6] = [Sheep_player.map_pos_x, Sheep_player.map_pos_y]
		self.event[6] = not bool(len(enemy_moving_sprites))
		self.checkpoints_pos_xy[7] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_map_xy[7] = [Sheep_player.map_pos_x, Sheep_player.map_pos_y]
		self.checkpoints_pos_xy[8] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_map_xy[8] = [Sheep_player.map_pos_x, Sheep_player.map_pos_y]
		
class mission4():
	#Прописывание сюжета
	def __init__(self):
		global AI_neutral_list, neutral_moving_sprites, player_moving_sprite
		Sheep_player.pos_x, Sheep_player.pos_y = random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100)
		Lama_Jennie.map_pos_x, Lama_Jennie.map_pos_y = 1, map_size_y
		Cow_Marcus.map_pos_x, Cow_Marcus.map_pos_y = -1, map_size_y
		Pig_Petr.map_pos_x, Pig_Petr.map_pos_y = map_size_x+1, map_size_y
		player_moving_sprite = spawn_animals([Sheep_player])
		generate_npc(0, 10)
		max_plants_Q = 3
		self.checkpoints_pos_xy = []
		self.checkpoints_map_xy = []
		self.checkpoint_counter= 0
		self.tips = []
		self.event = [1,1,0,1,0,0]			#Заполняем event еденицами
		self.mission_done = False
		#Чекпоинт 0
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_x, map_y])
		self.tips.append('')
		#Чекпоинт 1
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([1, map_size_y])
		self.tips.append('Нужно найти большую воду')
		#Чекпоинт 2
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([1, map_size_y])
		self.tips.append('Необходимо безопасное место')
		#Чекпоинт 3
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([Sheep_player.map_pos_x, Sheep_player.map_pos_y])
		self.tips.append('')
		#Чекпоинт 4
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([Sheep_player.map_pos_x, Sheep_player.map_pos_y])
		self.tips.append('Есть ли хоть ОДНА локация без волков?')
		#Чекпоинт 5
		self.checkpoints_pos_xy.append([Sheep_player.pos_x, Sheep_player.pos_y])
		self.checkpoints_map_xy.append([map_size_x, 0])
		self.tips.append('Надо уходить на восток')
	
	def checkpoint_reached(self):
		global AI_neutral_list, AI_friends_list, AI_enemy_list, neutral_moving_sprites, friends_moving_sprites, enemy_moving_sprites
		global max_plants_Q, Wolf1, Pig_Petr, berserk_mode
		if self.checkpoint_counter == 0:
			berserk_mode = True
			Sheep_player.health = 5	
			dialogs(Sheep_player, 'Нужно найти большую воду')
			Lama_Jennie.map_pos_x, Lama_Jennie.map_pos_y = 1, map_size_y
			Lama_Jennie.health = 5
		elif self.checkpoint_counter == 1:
			dialogs(Sheep_player, 'Дженни!')
			dialogs(Lama_Jennie, 'Нам нужно убираться подальше отсюда')
			dialogs(Lama_Jennie, 'СКОРЕЕ!')
			del AI_neutral_list[AI_neutral_list.index(Lama_Jennie)]	#Добавляем Ламу в список напарников
			AI_friends_list.append(Lama_Jennie)
			friends_moving_sprites = spawn_animals(AI_friends_list)
			neutral_moving_sprites = spawn_animals(AI_neutral_list)
			for i in range(2):	
				Wolf_temp =  animal('wolf', random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100))
				Wolf_temp.map_pos_x = Sheep_player.map_pos_x
				Wolf_temp.map_pos_y = Sheep_player.map_pos_y
				AI_enemy_list.append(Wolf_temp)
				enemy_moving_sprites.add(Wolf_temp)
		elif self.checkpoint_counter == 2:
			dialogs(Sheep_player, 'Как ты там оказалась?')
			dialogs(Lama_Jennie, 'Слушай, тебе не надо было меня искать')
			dialogs(Sheep_player, 'Что?')
			Wolf1 =  animal('wolf', random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100))
			Wolf1.map_pos_x = Sheep_player.map_pos_x
			Wolf1.map_pos_y = Sheep_player.map_pos_y
			AI_enemy_list.append(Wolf1)
			enemy_moving_sprites.add(Wolf1)
		elif  self.checkpoint_counter == 3:
			dialogs(Wolf1, 'Возможно')
			dialogs(Wolf1, 'Лама, ты привела к нам еще одну дичь')
			dialogs(Wolf1, 'Спасибо.')
			dialogs(Wolf1, 'Всегда приятно съесть 2 тушки вместо одной')
			generate_npc(0, 50)
			for i in range(7):	
				Wolf_temp =  animal('wolf', random.randint(10,display_size[0]-100), random.randint(10,display_size[1]-100))
				Wolf_temp.map_pos_x = Sheep_player.map_pos_x
				Wolf_temp.map_pos_y = Sheep_player.map_pos_y
				AI_enemy_list.append(Wolf_temp)
				enemy_moving_sprites.add(Wolf_temp)
		elif  self.checkpoint_counter == 4:
			dialogs(Lama_Jennie, 'Мы вырвались!')
			dialogs(Sheep_player, 'Поверить невозможно')
			dialogs(Lama_Jennie, 'Нам нужно покинуть эти места, слышишь?')
			dialogs(Lama_Jennie, 'Нам нужно идти на юго-восток')
		elif  self.checkpoint_counter == 5:
			dialogs(Lama_Jennie, 'Спасибо тебе. Я чуть не стала чьим то обедом')
			dialogs(Lama_Jennie, 'Пора покинуть это место раз и навсегда')
			splash_screen(mission4_complete_img)

		if self.checkpoint_counter < len(self.checkpoints_pos_xy) - 1:
			self.checkpoint_counter += 1
		else:
			#Миссия выполнена
			self.mission_done = True

	def update(self):
		self.checkpoints_pos_xy[0] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_pos_xy[1] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_pos_xy[2] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_map_xy[2] = [Sheep_player.map_pos_x, Sheep_player.map_pos_y]
		self.event[2] = not bool(len(enemy_moving_sprites))
		self.checkpoints_pos_xy[3] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_map_xy[3] = [Sheep_player.map_pos_x, Sheep_player.map_pos_y]
		self.checkpoints_pos_xy[4] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_map_xy[4] = [Sheep_player.map_pos_x, Sheep_player.map_pos_y]
		self.event[4] = not bool(len(enemy_moving_sprites))
		self.checkpoints_pos_xy[5] = [Sheep_player.pos_x, Sheep_player.pos_y]
		self.checkpoints_map_xy[5] = [map_size_x, 0]
		self.event[5] = not bool(len(enemy_moving_sprites))
		


class game_state():
	def __init__(self):
		self.state = 'game'
		# file = open('progress.dat', 'r')
		# self.mission_counter = int(file.read())
		# self.load_mission()
		self.mission_tics = 0	#Нужен для того, чтобы  окружение успело отрисоваться перед чекпоинтом
		self.state = 'menu'

	def game(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			############################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					Sheep_player.walk_left()				
				elif event.key == pygame.K_d:
					Sheep_player.walk_right()				
				elif event.key == pygame.K_w:
					Sheep_player.walk_back()
				elif event.key == pygame.K_s:
					Sheep_player.walk_front()
				elif event.key == pygame.K_SPACE:
					Sheep_player.eat()
				elif event.key == pygame.K_f:
					Sheep_player.talk()
				elif event.key == pygame.K_TAB:
					self.tips_menu()
				elif event.key == pygame.K_ESCAPE:
					self.state = 'pause'
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a or event.key == pygame.K_d:
					Sheep_player.stop()
				elif event.key == pygame.K_w or event.key == pygame.K_s:
					Sheep_player.stop()
			############################
		map()
		randomizer()
		#Управление искусственным интеллектом
		for friend in AI_friends_list:
			AI_friend(friend)
		for neutral in AI_neutral_list:
			if neutral.map_pos_x == map_x and neutral.map_pos_y == map_y:
				AI_neutral(neutral)
		for enemy in AI_enemy_list:
			if enemy.map_pos_x == map_x and enemy.map_pos_y == map_y:
				AI_enemy(enemy)
		#Проверка выполнения чекпоинтов
		self.mission.update()
		if self.mission.checkpoints_map_xy[self.mission.checkpoint_counter] == [Sheep_player.map_pos_x, Sheep_player.map_pos_y]:
			if abs(self.mission.checkpoints_pos_xy[self.mission.checkpoint_counter][0] - Sheep_player.pos_x) < 2*action_radius and abs(self.mission.checkpoints_pos_xy[self.mission.checkpoint_counter][1] - Sheep_player.pos_y) < 2*action_radius and self.mission.event[self.mission.checkpoint_counter] == True:
				if self.mission_tics > 2:
					self.mission.checkpoint_reached()
					self.mission_tics = 0
				else:
					self.mission_tics += 1
		#Проверка смерти напарников
		for friend in AI_friends_list:
			if friend.health <= 0:
				self.mission_failed()
		if len(enemy_moving_sprites) == 0:	#Если враги повержены, выставляем спокойную музыку
			background_music('neutral')
		#Расчет компаса-стрелки
		if self.mission.checkpoints_map_xy[self.mission.checkpoint_counter] == [Sheep_player.map_pos_x, Sheep_player.map_pos_y]:
			sign = (self.mission.checkpoints_pos_xy[self.mission.checkpoint_counter][0]-Sheep_player.pos_x)	#Получаем знак для постройки угла до 180 (узнаем какая коорддината больше)
			length = ((self.mission.checkpoints_pos_xy[self.mission.checkpoint_counter][1]-Sheep_player.pos_y)**2+(self.mission.checkpoints_pos_xy[self.mission.checkpoint_counter][0]-Sheep_player.pos_x+10**-6)**2)**0.5	#Расчет гипотенузы
			angle = sign/(abs(sign)+10**-6)*180/3.14*math.asin((Sheep_player.pos_y-self.mission.checkpoints_pos_xy[self.mission.checkpoint_counter][1])/(length+10**-6))	#Расчет угла
		else:
			sign = (self.mission.checkpoints_map_xy[self.mission.checkpoint_counter][0]-Sheep_player.map_pos_x+10**-4)
			length = ((self.mission.checkpoints_map_xy[self.mission.checkpoint_counter][1]-Sheep_player.map_pos_y)**2+(self.mission.checkpoints_map_xy[self.mission.checkpoint_counter][0]-Sheep_player.map_pos_x+10**-6)**2)**0.5
			angle = sign/(abs(sign)+10**-6)*180/3.14*math.asin((self.mission.checkpoints_map_xy[self.mission.checkpoint_counter][1]-Sheep_player.map_pos_y)/(length+10**-6))
		if self.mission.mission_done == True:
			self.mission_counter += 1
			file = open('progress.dat', 'w')
			file.write(str(self.mission_counter))
			file.close()
			self.load_mission()
			# self.state = 'mission_complete'

		#Отрисовка
		blit(sign<0, angle)
		pygame.display.update()

	# def mission_complete(self, title):
	# 	#Сохраняем прогресс:
	# 	# file = open('progress.dat', 'w')
	# 	# file.write(str(self.mission_counter+1))
	# 	# file.close()
	# 	# button_next_xy = [display_size[0]*0.5,display_size[1]*0.9]
	# 	# next_textsurface = myfont.render('Далее', False, light_yellow)
	# 	quit = False
	# 	while not quit:
	# 		mouse = pygame.mouse.get_pos()
	# 		for event in pygame.event.get():
	# 			if event.type == pygame.QUIT:
	# 				pygame.quit()
	# 			if event.type == pygame.MOUSEBUTTONDOWN:
	# 				if -button_size[0]/2<=mouse[0]-button_next_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_next_xy[1]<=button_size[1]/2:
	# 					self.mission_counter += 1
	# 					self.load_mission()
	# 					self.state = 'game'
	# 					quit = True

	# 		pygame.draw.rect(gameDisplay,green,[display_size[0]*0.5-120,display_size[1]*0.2]+[240, 50])	
	# 		button_hovered(button_next_xy, next_textsurface)
	# 		pygame.display.update()	#обновляем экран
	# 		clock.tick(FPS)

	def mission_failed(self):
		text = myfont.render('Напарник погиб!', False, light_yellow)
		button_quit_xy = [display_size[0]*0.5,display_size[1]*0.9]
		quit_textsurface = myfont.render('Заново', False, light_yellow)
		quit = False
		while not quit:
			mouse = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if -button_size[0]/2<=mouse[0]-button_quit_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_quit_xy[1]<=button_size[1]/2:
						pygame.quit()
						quit = True

			pygame.draw.rect(gameDisplay,green,[display_size[0]*0.5-120,display_size[1]*0.2]+[240, 50])	
			gameDisplay.blit(text, [display_size[0]*0.5-120,display_size[1]*0.2])
			button_hovered(button_quit_xy, quit_textsurface)
			pygame.display.update()	#обновляем экран
			clock.tick(FPS)

	def load_mission(self):
		file = open('progress.dat', 'r')
		self.mission_counter = int(file.read())
		if self.mission_counter == 0:
			self.mission = mission1()
		elif self.mission_counter == 1:
			splash_screen(mission2_start_img)
			self.mission = mission2()
		elif self.mission_counter == 2:
			splash_screen(mission3_start_img)
			self.mission = mission3()
		elif self.mission_counter == 3:
			splash_screen(mission4_start_img)
			self.mission = mission4()
		else:
			self.mission = mission1()

	def pause(self):
		running=True
		button_resume_xy = [display_size[0]*0.5,display_size[1]*0.3]
		button_quit_xy = [display_size[0]*0.5,display_size[1]*0.9]
		resume_textsurface = myfont.render('ПРОДОЛЖИТЬ', False, light_yellow)
		quit_textsurface = myfont.render('ВЫХОД', False, light_yellow)
		while running:
			mouse = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:	#выход из программы
					pygame.quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if -button_size[0]/2<=mouse[0]-button_resume_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_resume_xy[1]<=button_size[1]/2:
						self.state = 'game'
						running = False
					elif -button_size[0]/2<=mouse[0]-button_quit_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_quit_xy[1]<=button_size[1]/2:
						self.state = 'menu'
						running = False
			button_hovered(button_resume_xy,resume_textsurface)
			button_hovered(button_quit_xy, quit_textsurface)
			pygame.display.update()	#обновляем экран

	def menu(self):
		running=True
		button_start_xy = [display_size[0]*0.5,display_size[1]*0.3]
		button_resume_xy = [display_size[0]*0.5,display_size[1]*0.5]
		button_author_xy = [display_size[0]*0.5,display_size[1]*0.7]
		button_quit_xy = [display_size[0]*0.5,display_size[1]*0.9]
		
		start_textsurface = myfont.render('НОВАЯ ИГРА', False, light_yellow)
		resume_textsurface = myfont.render('ПРОДОЛЖИТЬ ИГРУ', False, light_yellow)
		author_textsurface = myfont.render('АВТОРЫ', False, light_yellow)
		quit_textsurface = myfont.render('ВЫХОД', False, light_yellow)

		while running:
			mouse = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:	#выход из программы
					pygame.quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if -button_size[0]/2<=mouse[0]-button_start_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_start_xy[1]<=button_size[1]/2:
						self.state = 'game'
						self.mission_counter = 0
						file = open('progress.dat', 'w')
						file.write(str(self.mission_counter))
						file.close()
						self.load_mission()
						splash_screen(welcome_msg_img)
						running = False
					elif -button_size[0]/2<=mouse[0]-button_resume_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_resume_xy[1]<=button_size[1]:
						self.state = 'game'
						self.load_mission()
						running = False
					elif -button_size[0]/2<=mouse[0]-button_author_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_author_xy[1]<=button_size[1]/2:
						self.state = 'author'
						running = False
					elif -button_size[0]/2<=mouse[0]-button_quit_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_quit_xy[1]<=button_size[1]/2:
						pygame.quit()
			
			gameDisplay.blit(menu_background_img, (display_size[0]*0.5-menu_bg_size[0]//2,display_size[1]-menu_bg_size[1]))
			# gameDisplay.blit(logo, (display_width*0.5-300,display_height*0.1-32))
			button_hovered(button_start_xy,start_textsurface)
			button_hovered(button_resume_xy,resume_textsurface)
			button_hovered(button_author_xy,author_textsurface)
			button_hovered(button_quit_xy, quit_textsurface)
			pygame.display.update()	#обновляем экран

	def author(self):
		button_back_xy = [display_size[0]*0.2,display_size[1]*0.9]
		back_textsurface = myfont.render('НАЗАД', False, light_yellow)
		running=True
		while running:
			mouse = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:	#выход из программы
					pygame.quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
						if -button_size[0]/2<=mouse[0]-button_back_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_back_xy[1]<=button_size[1]/2:
							self.state = 'menu'
							running = False
			gameDisplay.blit(author_img, (display_size[0]*0.5-254,display_size[1]*0.5-250))
			button_hovered(button_back_xy, back_textsurface)
			pygame.display.update()	#обновляем экран

	def state_manager(self):
		if self.state == 'game':
			self.game()
		elif self.state == 'mission_complete':
			self.mission_complete()
		elif self.state == 'pause':
			self.pause()
		elif self.state == 'menu':
			self.menu()
		elif self.state == 'author':
			self.author()
		
	def tips_menu(self):
		dialogs(Sheep_player, self.mission.tips[self.mission.checkpoint_counter])

class fireball():
	def __init__(self, direction, pos_x, pos_y):
		self.speed = 10
		self.direction = direction	#directiin [speed x,speed y]
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.disappear = False
		self.image = pygame.image.load('plant_ball.png')
	def update(self):
		global AI_enemy_list, enemy_moving_sprites
		health_temp = 10	#Костыль
		if self.pos_x > 0 and self.pos_x < display_size[0] and self.pos_y > 0 and self.pos_y < display_size[1]:
			self.pos_x += self.direction[0]*self.speed
			self.pos_y += self.direction[1]*self.speed
		else:
			self.disappear = True
		health_temp, enemy_moving_sprites, AI_enemy_list = animal_eaten(self.pos_x, self.pos_y, health_temp, AI_enemy_list)
		gameDisplay.blit(self.image, (self.pos_x,self.pos_y))
		if health_temp > 10:
			self.disappear = True


class animal(pygame.sprite.Sprite):
	def __init__(self, animal_type, pos_x, pos_y):
		super().__init__()
		self.walk_back_animation = False
		self.walk_front_animation = False
		self.walk_right_animation = False
		self.walk_left_animation = False
		self.eat_animation = False
		self.x_speed = 0
		self.y_speed = 0
		self.speed = 3
		self.health = 2
		self.pos_x = pos_x
		self.pos_y = pos_y 	#Положение на игровом поле
		self.map_pos_x = map_x	#Положение на карте
		self.map_pos_y = map_y
		self.animal_type = animal_type
		self.action_tics = pygame.time.get_ticks() #Таймер поедания
		self.action = False	#Флаг действия
		self.destination = [0,1]	#Направление
		self.aim_flag = False	#Цель объекта
		self.aim_index = 0	#Индекс цели

		self.walk_back_sprites, self.walk_front_sprites = [], []
		self.walk_right_sprites, self.walk_left_sprites = [], []
		self.eat_back_sprites, self.eat_front_sprites = [], []
		self.eat_right_sprites, self.eat_left_sprites = [], []
		for i in range(4):
			self.walk_back_sprites.append(pygame.image.load(self.animal_type+'/'+self.animal_type+'_walk_back'+str(i+1)+'.png'))
			self.walk_front_sprites.append(pygame.image.load(self.animal_type+'/'+self.animal_type+'_walk_front'+str(i+1)+'.png'))
			self.walk_right_sprites.append(pygame.image.load(self.animal_type+'/'+self.animal_type+'_walk_right'+str(i+1)+'.png'))
			self.walk_left_sprites.append(pygame.image.load(self.animal_type+'/'+self.animal_type+'_walk_left'+str(i+1)+'.png'))
		for i in reversed(range(4)):
			self.eat_front_sprites.append(pygame.image.load(self.animal_type+'/'+self.animal_type+'_eat_front'+str(i+1)+'.png'))

		self.current_sprite = 0
		self.image = self.walk_front_sprites[self.current_sprite]
		self.image_size = self.image.get_size()

		self.rect = self.image.get_rect()
		self.rect.topleft = [self.pos_x,self.pos_y]

	def talk(self):
		self.action = True

	def eat(self):
		self.eat_animation = True
		self.stop()	#Останавливаем персонажа, чтобы он поел

	def walk_back(self):
		self.walk_back_animation = True
		self.y_speed = -self.speed

	def walk_front(self):
		self.walk_front_animation = True
		self.y_speed = self.speed

	def walk_right(self):
		self.walk_right_animation = True
		self.x_speed = self.speed
	def walk_left(self):
		self.walk_left_animation = True
		self.x_speed = -self.speed

	def stop(self):
		self.walk_back_animation = False
		self.walk_front_animation = False
		self.walk_right_animation = False
		self.walk_left_animation = False
		self.y_speed = 0
		self.x_speed = 0
	
	def update(self,upd_speed):
		global neutral_moving_sprites, friends_moving_sprites, enemy_moving_sprites, player_moving_sprite
		global AI_neutral_list, AI_friends_list, Sheep_player, AI_enemy_list
		if self.walk_left_animation == True:
			self.destination = [-1,0]
		elif self.walk_right_animation == True:
			self.destination = [1,0]
		elif self. walk_back_animation == True:
			self.destination = [0,-1]
		elif self. walk_front_animation == True:
			self.destination = [0,1]
		if self.walk_back_animation or self.walk_front_animation or self.walk_right_animation or self.walk_left_animation == True:
			self.current_sprite += upd_speed
			if int(self.current_sprite) >= len(self.walk_back_sprites):
				self.current_sprite = 0
		if self.eat_animation == True:
			self.current_sprite += upd_speed*0.5
			if int(self.current_sprite) >= len(self.eat_front_sprites):
				self.current_sprite = 0
				self.eat_animation = False
		if self.walk_back_animation == True:
			self.image = self.walk_back_sprites[int(self.current_sprite)]
		elif self.walk_front_animation == True:
			self.image = self.walk_front_sprites[int(self.current_sprite)]
		elif self.walk_right_animation == True:
			self.image = self.walk_right_sprites[int(self.current_sprite)]
		elif self.walk_left_animation == True:
			self.image = self.walk_left_sprites[int(self.current_sprite)]
		elif self.eat_animation == True:
			self.image = self.eat_front_sprites[int(self.current_sprite)]
			if self.animal_type == 'wolf' and (pygame.time.get_ticks() - self.action_tics) > 2000:
				self.action_tics = pygame.time.get_ticks()
				self.health, neutral_moving_sprites, AI_neutral_list = animal_eaten(self.pos_x, self.pos_y, self.health, AI_neutral_list)
				self.health, friends_moving_sprites, AI_friends_list = animal_eaten(self.pos_x, self.pos_y, self.health, AI_friends_list)
				self.health, player_moving_sprite, [Sheep_player] = animal_eaten(self.pos_x, self.pos_y, self.health, [Sheep_player])	#Проверка поедания игрока хищником
			elif self.animal_type != 'wolf' and (pygame.time.get_ticks() - self.action_tics) > 1000:
				self.action_tics = pygame.time.get_ticks()
				self.health = plant_eaten(self.pos_x, self.pos_y, self.health)
				if berserk_mode == True and self.animal_type == 'sheep':
					self.health, enemy_moving_sprites, AI_enemy_list = animal_eaten(self.pos_x, self.pos_y, self.health, AI_enemy_list)
					fire(self.destination, self.pos_x, self.pos_y)
		self.image_size = self.image.get_size()
		#Обновление местоположения животного
		self.position_upd()
		self.rect.topleft = [self.pos_x, self.pos_y]

	def position_upd(self):
		#Взаимодействие с ландшафтом
		water_movement_fine = 1
		forest_movement_fine = 1
		try:
			color = background_img.get_at((self.pos_x+self.image_size[0]//2, self.pos_y+self.image_size[1]//2))
		except:
			color = (200, 200, 200)
		if color == (114, 114, 149):	#Движение по воде
			water_movement_fine = 3
		elif sum(color) < 200:	#Движение по густой растительности
			forest_movement_fine = 2
		#Новое местоположение
		self.pos_x += int(self.x_speed*(1+0.2*self.health)/water_movement_fine/forest_movement_fine)
		self.pos_y += int(self.y_speed*(1+0.2*self.health)/water_movement_fine/forest_movement_fine)
		#Взаимодействие с границами
		if self.pos_x >= display_size[0] - self.image_size[0]:
			self.pos_x = display_size[0] - self.image_size[0]
		if self.pos_x <= 0:
			self.pos_x = 0
		if self.pos_y >= display_size[1] - self.image_size[1]:
			self.pos_y = display_size[1] - self.image_size[1]
		if self.pos_y <= 0:
			self.pos_y = 0
		
def map(change_map=False):
	global plant_x_pos, plant_y_pos, types_of_plants, background_img
	global map_x, map_y
	global neutral_moving_sprites, enemy_moving_sprites
	global player_found
	image_size = Sheep_player.image.get_size()
	#Взаимодействие с границами
	if Sheep_player.pos_x >= display_size[0] - image_size[0] -1:
		if map_x == map_size_x:
			Sheep_player.pos_x = display_size[0] - image_size[0]
		else:
			map_x += 1
			Sheep_player.pos_x = 2
			change_map = True
	elif Sheep_player.pos_x <= 1:
		if map_x == 0:
			Sheep_player.pos_x = 0
		else:
			map_x -= 1
			Sheep_player.pos_x = display_size[0] - image_size[0] - 2
			change_map = True
	elif Sheep_player.pos_y >= display_size[1] - image_size[1] -1:
		if map_y == 0:
			Sheep_player.pos_y = display_size[1] - image_size[1]
		else:
			map_y -= 1
			Sheep_player.pos_y = 2
			change_map = True
	elif Sheep_player.pos_y <= 1:
		if map_y == map_size_y:
			Sheep_player.pos_y = 0
		else:
			map_y += 1
			Sheep_player.pos_y = display_size[1] - image_size[1] - 2
			change_map = True
	if change_map == True:
		#Подгружаем картинки
		background_img=pygame.image.load('map/map_'+str(map_x)+'_'+str(map_y)+'.png')	
		#Получаем размеры картинок
		plant_size = plants_img[0].get_size()
		#Подгоняем размеры изображений под размеры экрана
		background_img = pygame.transform.scale(background_img, display_size)
		#Спавним растения
		plant_x_pos, plant_y_pos, types_of_plants = spawn_plants(plant_size)
		change_map = False
		#Спавним дружественных персонажей рядом с нами
		for friends in AI_friends_list:
			friends.pos_x = Sheep_player.pos_x
			friends.pos_y = Sheep_player.pos_y
			friends.map_pos_x = map_x
			friends.map_pos_y = map_y
		Sheep_player.map_pos_x = map_x
		Sheep_player.map_pos_y = map_y
		#Спавним живность
		neutral_moving_sprites = spawn_animals(AI_neutral_list)
		enemy_moving_sprites = spawn_animals(AI_enemy_list)
		player_found = False #Изначально игорк не обнаружен противником
		if len(enemy_moving_sprites) > 0:
			background_music('enemy') #Включаем фоновую музыку
		else:
			background_music('neutral')
		
def spawn_animals(AI_list):
	animal_moving_sprites = pygame.sprite.Group()
	#Проверка на наличие других персонажей на карте
	for animal in AI_list:
		if animal.map_pos_x == map_x and animal.map_pos_y == map_y:
			animal_moving_sprites.add(animal)
	return animal_moving_sprites

def spawn_plants(plant_size):
	plant_x_pos, plant_y_pos = [], []
	types_of_plants = []
	Quantity_of_plants = random.randint(0,max_plants_Q)
	for i in range(Quantity_of_plants):
		plant_x_pos.append(random.randint(plant_size[0],int(display_size[0] - plant_size[0])))
		plant_y_pos.append(random.randint(plant_size[1],int(display_size[1] - plant_size[1])))
		types_of_plants.append(random.randint(0, len(plants_img)-1))
	i=0
	while i<len(types_of_plants):
		color = background_img.get_at((plant_x_pos[i], plant_y_pos[i]))
		if color == (114, 114, 149, 255) or color == (193, 193, 210) and i<len(types_of_plants):
			del plant_x_pos[i]
			del plant_y_pos[i]
			del types_of_plants[i]
		elif i>=len(types_of_plants):
			break
		else:
			i+=1
	return plant_x_pos, plant_y_pos, types_of_plants

def plant_eaten(pos_x, pos_y, health):
	global plant_x_pos, plant_y_pos, types_of_plants
	if len(types_of_plants)>0:
		for i in range(len(types_of_plants)):
			if abs(pos_x - plant_x_pos[i])< action_radius and abs(pos_y - plant_y_pos[i]) < action_radius:
				del plant_x_pos[i]
				del plant_y_pos[i]
				del types_of_plants[i]
				if health < 5:
					health += 1
				break
	return health

def animal_eaten(pos_x, pos_y, health, AI_list):
	for animal in AI_list:
		if animal.map_pos_x == map_x and animal.map_pos_y == map_y:
			if abs(pos_x - animal.pos_x) <= action_radius and abs(pos_y - animal.pos_y) <= action_radius:
				if animal.health >= 1:
					animal.health -= 1	#У жертвы отнимается 1 xp
				else:
					index = AI_list.index(animal)
					animal.health -= 1
					del AI_list[index] 	#Если xp нет, то жертва умирает, а хищник получает очко здоровья
					health += 1
					if Sheep_player.health <= 0:	#В случае смерти игрока
						gameover()
				break
	animal_moving_sprites = spawn_animals(AI_list)
	return health, animal_moving_sprites, AI_list

def fire(destination, pos_x, pos_y):
	global fireball_list
	fireball_list.append(fireball(destination,pos_x, pos_y))

def button_hovered(button_xy, textsurface):
	button_xy_centered=[]
	for i in range(len(button_xy)):
		button_xy_centered.append(button_xy[i]-button_size[i]/2)
	mouse = pygame.mouse.get_pos()
	if 0<=mouse[0]-button_xy_centered[0]<=button_size[0] and 0<=mouse[1]-button_xy_centered[1]<=button_size[1]:
		pygame.draw.rect(gameDisplay,green,button_xy_centered+button_size)
	else:
		pygame.draw.rect(gameDisplay,dark_green,button_xy_centered+button_size)	
	gameDisplay.blit(textsurface, button_xy_centered)

def gameover():
	gameover_text = myfont.render('Вы мертвы!', False, light_yellow)
	button_quit_xy = [display_size[0]*0.5,display_size[1]*0.9]
	quit_textsurface = myfont.render('Выход', False, light_yellow)
	background_music('dead')
	quit = False
	while not quit:
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if -button_size[0]/2<=mouse[0]-button_quit_xy[0]<=button_size[0]/2 and -button_size[1]/2<=mouse[1]-button_quit_xy[1]<=button_size[1]/2:
					pygame.quit()

		pygame.draw.rect(gameDisplay,red,[display_size[0]*0.5-120,display_size[1]*0.2]+[240, 50])	
		gameDisplay.blit(gameover_text, [display_size[0]*0.5-120,display_size[1]*0.2])
		button_hovered(button_quit_xy, quit_textsurface)
		pygame.display.update()	#обновляем экран
		clock.tick(FPS)	#FPS	

def find_aim(animal_object, aim_x, aim_y):
	deltax, deltay, length = [], [], []
	for i in range(len(aim_x)):
		deltax.append(abs(animal_object.pos_x - aim_x[i]))
		deltay.append(abs(animal_object.pos_y - aim_y[i]))
		length.append((deltax[i]**2+deltay[i]**2)**0.5)
	aim_index = length.index(min(length))
	return length, aim_index

def AI_friend(animal_object):
	if len(plant_x_pos) > 0 and animal_object.health < 5:
		find_food_AI(animal_object, plant_x_pos, plant_y_pos)
	elif len(enemy_moving_sprites) > 0:
		enemy_x_pos, enemy_y_pos = [], []
		for enemy in AI_enemy_list:
			if enemy.map_pos_x == map_x and enemy.map_pos_y == map_y:
				enemy_x_pos.append(enemy.pos_x)
				enemy_y_pos.append(enemy.pos_y)
		if len(enemy_x_pos) > 0:
			runaway_AI(animal_object, enemy_x_pos, enemy_y_pos)
	else:
		follow_player_AI(animal_object, [Sheep_player.pos_x], [Sheep_player.pos_y])

def AI_neutral(animal_object):
	if len(plant_x_pos) > 0 and animal_object.health < 5:
		find_food_AI(animal_object, plant_x_pos, plant_y_pos)
	elif len(enemy_moving_sprites) > 0:
		enemy_x_pos, enemy_y_pos = [], []
		for enemy in AI_enemy_list:
			if enemy.map_pos_x == map_x and enemy.map_pos_y == map_y:
				enemy_x_pos.append(enemy.pos_x)
				enemy_y_pos.append(enemy.pos_y)
		if len(enemy_x_pos) > 0:
			runaway_AI(animal_object, enemy_x_pos, enemy_y_pos)
	elif len(random_aim_x) > 0:
		walk_around(animal_object, random_aim_x, random_aim_y)	

def AI_enemy(animal_object):
	if len(AI_neutral_list) > 0:
		food_x_pos, food_y_pos = [], []
		for food in AI_neutral_list+AI_friends_list+[Sheep_player]:
			if food.map_pos_x == map_x and food.map_pos_y == map_y:
				food_x_pos.append(food.pos_x)
				food_y_pos.append(food.pos_y)
	if len(food_x_pos) > 0:
		find_food_AI(animal_object, food_x_pos, food_y_pos)
	elif len(random_aim_x) > 0:
		walk_around(animal_object, random_aim_x, random_aim_y)	

def runaway_AI(animal_object, aim_x, aim_y):
	length, aim_index = find_aim(animal_object, aim_x, aim_y)
	if animal_object.pos_x - aim_x[aim_index] > action_radius and animal_object.pos_x < display_size[0]*0.9:
		animal_object.walk_right()
	elif animal_object.pos_x - aim_x[aim_index] < -action_radius and animal_object.pos_x > display_size[0]*0.1:
		animal_object.walk_left()
	elif animal_object.pos_y - aim_y[aim_index] > action_radius and animal_object.pos_y < display_size[1]*0.9:
		animal_object.walk_front()
	elif animal_object.pos_y - aim_y[aim_index] < -action_radius and animal_object.pos_y > display_size[1]*0.1:
		animal_object.walk_back()
	else:
		movement = [animal_object.walk_right(), animal_object.walk_left(), 
		animal_object.walk_front(), animal_object.walk_back()]
		movement[random.randint(0, 3)]		

def find_food_AI(animal_object, aim_x, aim_y):
	global player_found
	length, aim_index = find_aim(animal_object, aim_x, aim_y)
	if Sheep_player.pos_x == aim_x[aim_index] and Sheep_player.pos_y == aim_y[aim_index] and player_found == False:
		play_sound('player_found')
		player_found = True
	if length[aim_index] < action_radius:
		animal_object.eat()
	elif animal_object.pos_x - aim_x[aim_index] > action_radius:
		animal_object.walk_left()
	elif animal_object.pos_x - aim_x[aim_index] < -action_radius:
		animal_object.walk_right()
	elif animal_object.pos_y - aim_y[aim_index] > action_radius:
		animal_object.walk_back()
	elif animal_object.pos_y - aim_y[aim_index] < -action_radius:
		animal_object.walk_front()

def follow_player_AI(animal_object, aim_x, aim_y):
	length, aim_index = find_aim(animal_object, aim_x, aim_y)
	if length[aim_index] < 5*action_radius:
		animal_object.stop()
	elif animal_object.pos_x - aim_x[aim_index] > 5*action_radius:
		animal_object.walk_left()
	elif animal_object.pos_x - aim_x[aim_index] < -5*action_radius:
		animal_object.walk_right()
	elif animal_object.pos_y - aim_y[aim_index] > 5*action_radius:
		animal_object.walk_back()
	elif animal_object.pos_y - aim_y[aim_index] < -5*action_radius:
		animal_object.walk_front()

def walk_around(animal_object, aim_x, aim_y):
	deltax, deltay, length = [], [], []
	for i in range(len(aim_x)):
		deltax.append(abs(animal_object.pos_x - aim_x[i]))
		deltay.append(abs(animal_object.pos_y - aim_y[i]))
		length.append((deltax[i]**2+deltay[i]**2)**0.5)
	if animal_object.aim_flag == False or animal_object.aim_index>=len(length):	#Если цели нет, выбираем ее
		animal_object.aim_index = random.randint(0,len(length)-1)	#Выбираем случайную цель
		animal_object.aim_flag = True
	if length[animal_object.aim_index] <= 5*action_radius: 
		if int((pygame.time.get_ticks()-start_ticks)%3000) < 100:
			animal_object.aim_flag = False
		animal_object.stop()
	elif animal_object.pos_x - aim_x[animal_object.aim_index] > 5*action_radius:
		animal_object.walk_left()
	elif animal_object.pos_x - aim_x[animal_object.aim_index] < -5*action_radius:
		animal_object.walk_right()
	elif animal_object.pos_y - aim_y[animal_object.aim_index] > 5*action_radius:
		animal_object.walk_back()
	elif animal_object.pos_y - aim_y[animal_object.aim_index] < -5*action_radius:
		animal_object.walk_front()

def randomizer():
	global random_aim_x, random_aim_y
	if random.randint(0,100) < 4 and int((pygame.time.get_ticks()-start_ticks)%3000) < 100:
		random_aim_x, random_aim_y = [], []
		for i in range(random.randint(1,40)):
			random_aim_x.append(random.randint(action_radius, display_size[0]-action_radius))
			random_aim_y.append(random.randint(action_radius, display_size[1]-action_radius))

def background_music(theme_type):
	global music_tics
	if theme_type == 'dead':
		pygame.mixer.music.load('music/Gameover.wav')
		pygame.mixer.music.play(-1)
	elif theme_type == 'enemy':
		title = alert_music_list[random.randint(0,len(alert_music_list)-1)]
		pygame.mixer.music.load(title)
		pygame.mixer.music.play(-1)
		music_tics = -5*10**3*60
	elif theme_type == 'neutral' and pygame.time.get_ticks() - music_tics > 5*10**3*60: #Включаем фоновую музыку если нет врагов
		music_tics = pygame.time.get_ticks()
		title = music_list[random.randint(0,len(music_list)-1)]
		pygame.mixer.music.load(title)
		pygame.mixer.music.play(0)
	
def play_sound(trigger):
	if trigger == 'player_found':
		pygame.mixer.Sound.play(player_found_sound)

def splash_screen(message):
	message_size = message.get_size()
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			############################
			if event.type == pygame.KEYDOWN:
				running = False
		gameDisplay.blit(message, (display_size[0]*0.5-message_size[0]//2,display_size[1]*0.5-message_size[1]//2))
		pygame.display.update()	#обновляем экран
		clock.tick(FPS)

def dialogs(animal_object,text):
	Sheep_player.stop()
	letters_in_line = 12
	textsurface_list = []
	if len(text) >= letters_in_line:
		text_list=[]
		while len(text)>letters_in_line:
			text_list.append(text[:letters_in_line-1])
			text=text[letters_in_line-1:]
		else:
			text_list.append(text)
	else:
		text_list=[text]
	for element in text_list:
		textsurface_list.append(textfont.render(element, False, black))
	close = False
	while not close:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					close = True

		if animal_object.pos_x + dbox_size[0] > display_size[0]:	#Проверка не будет ли выходить окно за правую границу экрана
			if animal_object.pos_y - dbox_size[1] <= 0:	#Проверка на выход границ экрана за верхнюю границу экрана
				dialog_pos = [animal_object.pos_x, animal_object.pos_y+animal_object.image_size[1]]
				gameDisplay.blit(dbox_left_down_img, dialog_pos)
				for i in range(len(textsurface_list)):
					gameDisplay.blit(textsurface_list[i], [dialog_pos[0]+20, dialog_pos[1]+40+i*20])	#Отступ по y, чтобы оказаться в текстовом окне
			else:
				dialog_pos = [animal_object.pos_x, animal_object.pos_y-dbox_size[1]]
				gameDisplay.blit(dbox_left_up_img, dialog_pos)
				for i in range(len(textsurface_list)):
					gameDisplay.blit(textsurface_list[i], [dialog_pos[0]+20,dialog_pos[1]+20+i*20])
		else:
			if animal_object.pos_y - dbox_size[1] <= 0:	#Проверка на выход границ экрана за верхнюю границу экрана
				dialog_pos = [animal_object.pos_x+animal_object.image_size[0], animal_object.pos_y+animal_object.image_size[1]]
				gameDisplay.blit(dbox_right_down_img, dialog_pos)
				for i in range(len(textsurface_list)):
					gameDisplay.blit(textsurface_list[i], [dialog_pos[0]+20, dialog_pos[1]+40+i*20])
			else:
				dialog_pos = [animal_object.pos_x+animal_object.image_size[0], animal_object.pos_y-dbox_size[1]]
				gameDisplay.blit(dbox_right_up_img, dialog_pos)
				for i in range(len(textsurface_list)):
					gameDisplay.blit(textsurface_list[i], [dialog_pos[0]+20,dialog_pos[1]+20+i*20])

		pygame.display.update()	#обновляем экран
		clock.tick(FPS)	#FPS	

def generate_npc(neutal_Q, enemy_Q):
	global AI_neutral_list, AI_enemy_list
	for i in range(neutal_Q):	#Спавним нейтральных персонажей по всей карте
		Chicken_temp = animal('chicken', random.randint(10,display_size[0]), random.randint(10,display_size[1]))
		Chicken_temp.map_pos_x = random.randint(0,map_size_x)
		Chicken_temp.map_pos_y = random.randint(0,map_size_y)
		if Sheep_player.map_pos_x == Chicken_temp.map_pos_x and Sheep_player.map_pos_y == Chicken_temp.map_pos_y:	#Не спавним волков на месте игрока
			pass	#Кроме местоположения игрока
		else:
			AI_neutral_list.append(Chicken_temp)
	for i in range(enemy_Q):	#Спавним вражеских персонажей по всей карте
		Wolf_temp = animal('wolf', random.randint(10,display_size[0]), random.randint(10,display_size[1]))
		Wolf_temp.map_pos_x = random.randint(0,map_size_x)
		Wolf_temp.map_pos_y = random.randint(0,map_size_y)
		if Sheep_player.map_pos_x == Wolf_temp.map_pos_x and Sheep_player.map_pos_y == Wolf_temp.map_pos_y:	#Не спавним волков на месте игрока
			pass
		else:
			AI_enemy_list.append(Wolf_temp)

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
    return rotated_image, new_rect

def blit(sign, angle):
	#Отображение элементов
	gameDisplay.blit(background_img, (0,0))
	for i in range(len(types_of_plants)):
		gameDisplay.blit(plants_img[types_of_plants[i]], (plant_x_pos[i],plant_y_pos[i]))
	player_moving_sprite.draw(gameDisplay)
	player_moving_sprite.update(0.3)
	friends_moving_sprites.draw(gameDisplay)
	friends_moving_sprites.update(0.3)
	neutral_moving_sprites.draw(gameDisplay)
	neutral_moving_sprites.update(0.2)
	enemy_moving_sprites.draw(gameDisplay)
	enemy_moving_sprites.update(0.22)
	i=0
	while i<len(fireball_list):
		if fireball_list[i].disappear == False:
			fireball_list[i].update()
			i+=1
		else:
			del fireball_list[i]
	gameDisplay.blit(healthar_img, (40,40))
	for i in range(Sheep_player.health):
		gameDisplay.blit(health_img, (50+50*i,50))

	rotated_image, new_rect = rot_center(arrow_img[sign], angle, display_size[0]*0.9, display_size[1]*0.1)
	gameDisplay.blit(rotated_image, new_rect)
	
###################Инициализация###################
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 36)
textfont = pygame.font.SysFont('Comic Sans MS', 30)

display_size = (int(1280/1.1), int(720/1.1))
gameDisplay = pygame.display.set_mode(display_size)

pygame.display.set_caption('game')
clock = pygame.time.Clock()

black = (0,0,0)
light_yellow = (250,240,173)
dark_green = (80, 120, 0)
red = (255, 0, 0)
green = (120, 160, 0)
blue = (0, 0, 255)

AI_neutral_list, AI_friends_list, AI_enemy_list = [], [], []
random_aim_x, random_aim_y = [], []
plants_img=[]
for i in range(3):
		plants_img.append(pygame.image.load('plants/plant'+str(i+1)+'.png'))
health_img = pygame.image.load('health.png')
healthar_img = pygame.image.load('healthbar.png')
dbox_left_down_img = pygame.image.load('dboxes/dbox_left_down.png')
dbox_left_up_img = pygame.image.load('dboxes/dbox_left_up.png')
dbox_right_down_img = pygame.image.load('dboxes/dbox_right_down.png')
dbox_right_up_img = pygame.image.load('dboxes/dbox_right_up.png')
dbox_size = dbox_left_up_img.get_size()
arrow_img = [pygame.image.load('arrow_right.png'), pygame.image.load('arrow_left.png')]
author_img = pygame.image.load('hackerman.jpg')
menu_background_img = pygame.image.load('bg_menu.png')
menu_bg_size = menu_background_img.get_size()
welcome_msg_img =  pygame.image.load('welcome_msg.png')
mission2_start_img = pygame.image.load('mission2_start.png')
mission3_start_img = pygame.image.load('mission3_start.png')
mission4_start_img = pygame.image.load('mission4_start.png')
mission1_complete_img = pygame.image.load('mission1_complete.png')
mission2_complete_img = pygame.image.load('mission2_complete.png')
mission3_complete_img = pygame.image.load('mission3_complete.png')
mission4_complete_img = pygame.image.load('mission4_complete.png')


music_list, alert_music_list = [], []
music_list.append("music/Beginning_2.wav")
music_list.append("music/Clark.wav")
music_list.append("music/Concrete_Halls.wav")
music_list.append("music/Dry_Hands.wav")
music_list.append("music/Floating_Trees.wav")
music_list.append("music/Haggstorm.wav")
music_list.append("music/Key.wav")
music_list.append("music/Mice_on_Venus.wav")
music_list.append("music/Sweden.wav")
alert_music_list.append("music/Alert1.wav")
player_found_sound = pygame.mixer.Sound("music/Player_found.ogg")


FPS = 60
map_x = 3
map_y = 3
map_size_x = 4
map_size_y = 9
player_found = False
action_radius = 50
music_tics = -5*10**3*60
button_size = [300, 50]
start_ticks=pygame.time.get_ticks()

# Создаем спрайты и группируем их
Sheep_player = animal('sheep', display_size[0]//2, display_size[1]//2)
Lama_Jennie = animal('lama', display_size[0]*0.1, display_size[1]*0.1)
Cow_Marcus = animal('cow', random.randint(10,display_size[0]), random.randint(10,display_size[1]))
Pig_Petr = animal('pig', random.randint(10,display_size[0]), random.randint(10,display_size[1]))

generate_npc(50, 0)
max_plants_Q = 10	#Максимальное количество растений на поле
AI_neutral_list.append(Lama_Jennie)
AI_neutral_list.append(Cow_Marcus)
AI_neutral_list.append(Pig_Petr)
player_moving_sprite = pygame.sprite.Group()
friends_moving_sprites = pygame.sprite.Group()
neutral_moving_sprites = pygame.sprite.Group()
enemy_moving_sprites = pygame.sprite.Group()
player_moving_sprite.add(Sheep_player)

game_state1 = game_state()
#########################################################

#Начало игры
fireball_list = []
berserk_mode = False
map(True)
running = True
while running:
	game_state1.state_manager()
	
	clock.tick(FPS)