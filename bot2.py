import telebot
commands = {  
    'start'       : 'приветствие',
    'help'        : 'информация',
    'glass'        : 'ты узнаешь как долго разлагается стекло',
    'boots'        : 'ты узнаешь как долго разлагается выброшенная обувь',
    'rubbertires'        : 'ты узнаешь как долго разлагаются резиновые покрышки',
    'food'        : 'ты узнаешь как долго разлагаются пищевые отходы',
    'batteries'        : 'ты узнаешь как долго разлагаются электрические батарейки',
    'newspaper'        : 'ты узнаешь как долго разлагаются газеты',
    'foil'        : 'ты узнаешь как долго разлагается фольга',
    'cardboard'        : 'ты узнаешь сколько разлагаются картонные коробки',
    'plastic'     : 'ты узнаешь как долго разлагаются пластмассовые изделия',
    'Aluminumcans'    : 'ты узнаешь как долго разлагаются Алюминиевые банки',
    'people'        : 'как люди еще загрязняют природу?',
    'water'        : 'загрязнение воды',
    'soil'        : 'загрязнение почвы',
    'atmosphere'        : 'загрязнение атмосферы',
    'how'        : 'как же частично защитить природу от загрязнения?',
    'how2'        : 'как сортировать мусор?'
}

bot = telebot.TeleBot("token")

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message, "Привет! Я бот , который поможет тебе узнать, как долго разлагаются предметы и что нужно делать, чтобы не засорять природу! Введи команду help и посмотри, что ты можешь узнать")

@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "имеющиеся комманды: \n"
    for key in commands: 
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)

@bot.message_handler(commands=['glass'])
def send_glass(message):
    bot.reply_to(message, "Срок разложения стекла более 1000 лет.Является одним из самых распространенных видов отходов. Разлагается целое тысячелетие! Еще много будущих поколений будут наслаждаться нашими осколками....Стекло никогда не теряет своих свойств и может подвергаться переработке бесконечное количество раз без каких-либо потерь качества производимой продукции.")

@bot.message_handler(commands=['rubbertires'])
def send_rubbertires(message):
    bot.reply_to(message, "Срок разложения резиновых покрышек 120-140 лет.Резина относится к одному из самых стойких материалов. Вторичная переработка этого отхода уже достаточно развита, к примеру, измельченные покрышки используют для покрытия спортивных площадок.")

@bot.message_handler(commands=['newspaper'])
def send_newspaper(message):
    bot.reply_to(message, "Срок разложения 1-4 месяца. Прежде чем выкинуть газету на дорогу, подумайте, что еще целых 4 месяца она будет лежать под вашими ногами.")

@bot.message_handler(commands=['food'])
def send_food(message):
    bot.reply_to(message, "Срок разложения 30 дней. К этому виду отхода можно отнести остатки пищи, овощные очистки, просроченные продукты питания и т.д. Такие отходы не представляют серьезной угрозы для окружающей среды.")

@bot.message_handler(commands=['batteries'])
def send_batteries(message):
    bot.reply_to(message, "Срок разложения 110 лет. Здесь роль играет не только Срок разложения, но и вред окружающей среде, который наносит батарейка, когда происходит процесс окисления.")

@bot.message_handler(commands=['foil'])
def send_foil(message):
    bot.reply_to(message, "Срок разложения более 100 лет. Даже если отходы фольги не преобладают на нашей планете, не стоит забывать о том, что каждый выброшенный лист будет разлагаться более 100 лет.")

@bot.message_handler(commands=['cardboard'])
def send_cardboard(message):
    bot.reply_to(message, "Срок разложения 3 месяца. Безвредный отход, если выкидывать его в мусорные баки или сдавать на вторичную переработку.")

@bot.message_handler(commands=['plastic'])
def send_plastic(message):
    bot.reply_to(message, "Срок разложения 180-200 лет. Одной из самых глобальных экологических проблем является загрязнение окружающей среды различными пластиками и полиэтиленовыми пакетами. Только представьте, что каждый год в океан попадает около 13 миллионов тонн пластиковых отходов! Заводы, выпускающие пластиковые изделия, выделяют в атмосферу до 400 миллионов тонн углекислого газа в год и примерно 800 видов животных сегодня находятся под угрозой вымирания из-за поедания и отравления пластиком.")

@bot.message_handler(commands=['Aluminumcans'])
def send_Aluminumcans(message):
    bot.reply_to(message, "Срок разложения 500 лет. Очень долго разлагаются, выделяет вредные вещества при окислении, присутствует в большом количестве на нашей планете.")

@bot.message_handler(commands=['boots'])
def send_boots(message):
    bot.reply_to(message, "Срок разложения обуви из натурального сырья 10 лет, из синтетического - 80 лет.")

@bot.message_handler(commands=['people'])
def send_people(message):
    bot.reply_to(message, "Ученые уже несколько десятилетий подряд бьют тревогу о близкой экологической катастрофе. Проведенные исследования в разных областях приводят к выводу, что мы уже сталкиваемся с глобальными изменениями климата и внешней среды под воздействием деятельности человека. Загрязнение океанов из-за утечек нефти и нефтепродуктов, а также мусора дошло до огромных масштабов, что влияет на сокращение популяций многих видов животных и экосистему в целом. Растущее число машин каждый год приводит к большому выбросу углекислого газа в атмосферу, что, в свою очередь, ведет к осушению земли, обильным осадкам на материках, уменьшению количества кислорода в воздухе.")

@bot.message_handler(commands=['water'])
def send_water(message):
    bot.reply_to(message, "Люди, прошедшие долгий путь в пустыне, наверняка смогут называть цену каждой капли воды. Хотя скорее всего эти капли будут бесценны, ведь от них зависит жизнь человека. В обычной жизни, мы, увы, придаем воде не такое большое значение, поскольку ее у нас много, и доступна она в любое время. Только в перспективе это не совсем так. В процентном соотношении незагрязненными остались только 3% от всего мирового запаса пресной воды. Понимание важности воды для людей не мешает человеку загрязнять важный источник жизни нефтью и нефтепродуктами, тяжелыми металлами, радиоактивными веществами, неорганическими загрязнениями, канализационными стоками и синтетическими удобрениями")

@bot.message_handler(commands=['soil'])
def send_soil(message):
    bot.reply_to(message, "Пожалуй, не имеет смысла объяснять, насколько почва является важной частью жизни человека. Большую часть еды, которой питается человек, приносит почва: от злаковых культур до редких видов фруктов и овощей. Чтобы так продолжалось и дальше, необходимо поддерживать состояние грунта на должном уровне для нормального круговорота воды. Но антропогенное загрязнение уже привело к тому, что 27% земель планеты подвержены эрозии.")

@bot.message_handler(commands=['atmosphere'])
def send_atmosphere(message):
    bot.reply_to(message, "Атмосфера в виде газообразной оболочки Земли имеет большую ценность, поскольку защищает планету от космической радиации, воздействует на рельеф, определяет климат Земли и ее тепловой фон. Нельзя сказать, что состав атмосферы был однородным и только с появлением человека начал меняться. Но именно после начала активной деятельности людей неоднородный состав «обогатился» опасными примесями. Основными загрязнителями в данном случае выступают химические заводы, топливно-энергетический комплекс, сельское хозяйство и автомобили. Они приводят к появлению в составе воздуха меди, ртути, свинца и других металлов. Разумеется, в промышленных зонах загрязнение воздуха чувствуется больше всего. Современные автомобили достаточно хороши по дизайну и техническим характеристикам, но проблему с выбросом токсинов от выхлопа в атмосферу решить до сих пор не удалось. Зола и продукты переработки топлива не только портят атмосферу городов, но и оседают на почве и приводят к ее негодности.")

@bot.message_handler(commands=['how'])
def send_how(message):
    bot.reply_to(message, "Чем ты можешь помочь природе, шаги для улучшения экологии на планете: 1.Отказ от пластика. Проблема загрязнения природы пластиком стоит очень остро на сегодняшний день. От него страдает океан, животные и в целом вся экология. Итак, есть несколько способов отказа от пластика: замена обычных пакетов на многоразовые сумки-шопперы или другие экологичные варианты; использовать не пластиковую одноразовую посуду, а картонную, так как она быстрее разлагается; отдать предпочтение многоразовой бутылке для воды. 2.Сортировка мусора. Первым делом следует сократить количество выбрасываемого мусора. Например, старые вещи можно отдавать на благотворительность, а бумагу копить и сдавать в пункты приема макулатуры. За это можно даже получить небольшое, но приятное вознаграждение. Если решение о том, чтобы пойти по экологичному пути, пришло совсем недавно, можно начать с малого: правильно утилизировать пластик, лампочки и батарейки. Пункты приема найти не проблема: их можно сдать во многих магазинах и государственных учреждениях. Когда уже опыта будет достаточно, нужно узнать о расположении специальных контейнеров в своем населенном пункте, куда можно относить стекло, металл, пластик и другие отходы. 3.Отказаться от пакетированного чая. Казалось бы, какой может быть вред от маленького пакетика чая? Если посмотреть на этот вопрос более глобально, можно понять, что ежедневно по всему миру утилизируется огромное количество чайных пакетиков, которые в свою очередь полностью не разлагаются. Они остаются в почве надолго, нанося ей серьезный вред. Чтобы сберечь природу, лучше отдать предпочтение листовому чаю. 4.Убирать за собой после пикника. Семейный отдых на природе – прекрасный вариант времяпровождения, но важно не забывать забирать с собой собственный мусор. На пикники зачастую везут с собой одноразовую посуду, пластиковые пакеты и бутылки. Помимо того, что это засоряет почву, мусор попадает еще и в водоемы. После отдыха не сложно потратить 10 минут, чтобы всей семьей или компанией друзей убрать мусор. Таким образом получится не только помочь планете, но и подать детям правильный пример. 5.Участвовать в экологических движениях. Существуют различные волонтерские движения, направленные на сохранение природы. Все желающие собираются в группы и идут убирать в лесах, парках и других загрязненных зонах. Можно участвовать в таких мероприятиях хотя бы иногда, поскольку даже небольшой вклад будет значимым. 6.Принять участие в озеленении. Посадить дерево – значит внести неоценимый вклад в сохранение планеты. Конечно, живя в многоквартирном доме, посадить дерево не получится, да и на своем участке много не уместишь. При этом существует множество мероприятий по озеленению парков и скверов, в которых можно принять участие. Если в регионе не проводится таких акций, можно обратиться в фонд, который собирает средства на покупку саженцев для посадки в общественных местах... Есть еще много способов внести свой вклад в убережении природы от загрязнения, гдавное иметь желание!")

@bot.message_handler(commands=['how2'])
def send_how2(message):
    bot.reply_to(message, "Как начать сортировать мусор? 1.Найдите ближайшие к вам точки сбора вторичных ресурсов. 2.Определите виды отходов, которые будете сдавать в переработку. 3.Подготовьте сырье для сдачи в переработку.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
