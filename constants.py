intro_text = """
-----------------------------------------------

Welcome to the Winter Survival Exercise!

In this exercise you will test your knowledge of survival techniques and science to see if you could survive in an extreme winter environment. 

In the exercise, the narrative has a white font, lines that require your input are yellow, text from the expert is green, and any errors are red.

You may at times need to scroll up to see the beginning of each section of text (or the beginning of tables in the exercise).

Press 'Ctrl + C' at any point to quit.
"""

scenario_text = """
-----------------------------------------------

1. It is mid-January and your light airplane crashed in Northern Canada this morning at 1132am. You are the only survivor.

2. You are in a snowy wilderness area made up of thick woods broken by many lakes and rivers. The last weather report indicated that the temperature will be minus twenty-five degrees in the daytime and minus forty at night.

3. You are dressed in business clothes as you were on your way to a meeting —suit, street shoes, and overcoat.

4. While escaping from the plane you saw twelve items, but you can only manage to take five out of the plane wreck. Your task is to select five of the items and rank these five items according to their importance for your survival (1 being the most important, 2 the second most important, and so on). You can change your mind about which items to take ONLY ONCE.

5. Mid-January is the coldest time of the year where you are. The first problem you face, therefore, is to preserve body heat and to protect your body against heat loss. Your body will be using energy to stay warm, so that is another consideration. You also need to consider how you can attract the attention of search parties.
"""


score_text = """
-----------------------------------------------
Scoring

1. This exercise was created by a US Army survival expert who also ranked the items. 

2. Your 5 rankings will be compared with how he ranked the items, so if your first choice (i.e. 1) was also ranked by him as the first choice (i.e. 1), you will get 0 penalty points (expert ranking - your ranking, so 1 - 1 = 0. However, if your second choice (i.e. 2) was ranked by the expert as the 11th most important item (i.e. 11), you will get 9 penalty points (11 - 2 = 9). 

3. Your aim is to get as low a total score for the 5 items as possible. The best score is 0, and the poorest is 35.

4. Finally, there are no absolutely right answers, and in real life your ability to use the items chosen will affect their usefulness. You may therefore not agree with the exact rankings the expert has given, but the expert's rankings would unquestionably give you a chance of survival in this environment.
"""

item_descriptions = {
    1: "A ball of steel wool",
    2: "A small axe",
    3: "A loaded .45-caliber pistol",
    4: "Tin of coconut oil",
    5: "A newspaper",
    6: "Cigarette lighter (without fluid)",
    7: "Extra shirt and trousers",
    8: "A 20 x 20 ft. piece of heavy-duty canvas",
    9: "A sectional air map made of plastic",
    10: "Half a bottle of 85-proof whisky",
    11: "A compass",
    12: "A family-size chocolate bar"
}

item_list = [['1', 'A ball of steel wool'], ['2', 'A small axe'], ['3', 'A loaded .45-caliber pistol'], ['4', 'Tin of coconut oil'], ['5', 'A newspaper'], ['6', 'Cigarette lighter (without fluid)'], ['7', 'Extra shirt and trousers'], ['8', 'A 20 x 20 ft. piece of heavy-duty canvas'], ['9', 'A sectional air map made of plastic'], ['10', 'Half a bottle of 85-proof whisky'], ['11', 'A compass'], ['12', 'A family-size chocolate bar']]

expert_view = {
    1: "Cigarette lighter (without fluid)",
    2: "A ball of steel wool",
    3: "Extra shirt and trousers",
    4: "Tin of coconut oil",
    5: "A 20 x 20 ft. piece of heavy-duty canvas",
    6: "A small axe",
    7: "A family-size chocolate bar",
    8: "A newspaper",
    9: "A loaded .45-caliber pistol",
    10: "Half a bottle of 85-proof whisky",
    11: "A compass",
    12: "A sectional air map made of plastic"
}

expert_list = [['1', 'Cigarette lighter (without fluid)'], ['2', 'A ball of steel wool'], ['3', 'Extra shirt and trousers'], ['4', 'Tin of coconut oil'], ['5', 'A 20 x 20 ft. piece of heavy-duty canvas'], ['6', 'A small axe'], ['7', 'A family-size chocolate bar'], ['8', 'A newspaper'], ['9', 'A loaded .45-caliber pistol'], ['10', 'Half a bottle of 85-proof whisky'], ['11', 'A compass'], ['12', 'A sectional air map made of plastic']]

feedback_dict = {
    1 : 'A ball of steel wool: \n"To make a fire, the survivors need a means of catching he sparks made by the cigarette lighter. This is the best substance for catching a spark and supporting a flame, even if the steel wool is a little wet."\n', 
    2 : 'A small axe: \n"Survivors need a constant supply of wood in order to maintain the fire. The axe could be used for this as well as for clearing a sheltered campsite, cutting tree branches for ground insulation, and constructing a frame for the canvas tent."\n',
    3 : 'A loaded .45-caliber pistol: \n"The pistol provides a sound-signaling device. (The international distress signal is 3 shots fired in rapid succession). There have been numerous cases of survivors going undetected because they were too weak to make a loud enough noise to attract attention. The butt of the pistol could be used as a hammer, and the powder from the shells will assist in fire building. By placing a small bit of cloth in a cartridge emptied of its bullet, one can start a fire by firing the gun at dry wood on the ground. The pistol also has some serious disadvantages. Anger, frustration, impatience, irritability, and lapses of rationality may increase as the group awaits rescue. The availability of a lethal weapon is a danger to the group under these conditions. Although a pistol could be used in hunting, it would take an expert marksman to kill an animal with it. Then the animal would have to be transported to the crash site, which could prove difficult to impossible depending on its size."\n', 
    4 : 'Tin of coconut oil: \n"This has many uses. A mirror-like signaling device can be made from the lid. After shining the lid with steel wool, it will reflect sunlight and generate 5 to 7 million candlepower. This is bright enough to be seen beyond the horizon. While this could be limited somewhat by the trees, a member of the group could climb a tree and use the mirrored lid to signal search planes. If they had no other means of signaling than this, they would have a better than 80% chance of being rescued within the first day. There are other uses for this item. It can be rubbed on exposed skin for protection against the cold. The empty can is useful in melting snow for drinking water. It is much safer to drink warmed water than to eat snow, since warm water will help retain body heat. Water is important because dehydration will affect decision-making. The can is also useful as a cup."\n', 
    5 : 'A newspaper: \n"These are useful in starting a fire. They can also be used as insulation under clothing when rolled up and placed around a person’s arms and legs. A newspaper can also be used as a verbal signaling device when rolled up in a megaphone-shape. It could also provide reading material for recreation."\n', 
    6 : 'Cigarette lighter (without fluid): \n"The gravest danger facing the group is exposure to cold. The greatest need is for a source of warmth and the second greatest need is for signaling devices. This makes building a fire the first order of business. Without matches, something is needed to produce sparks, and even without fluid, a cigarette lighter can do that."\n', 
    7 : 'Extra shirt and trousers: \n"Besides adding warmth to the body, clothes can also be used for shelter, signaling, bedding, bandages, string (when unraveled), and fuel for the fire."\n', 
    8 : 'A 20 x 20 ft. piece of heavy-duty canvas: \n"The cold makes shelter necessary, and canvas would protect against wind and snow (canvas is used in making tents). Spread on a frame made of trees, it could be used as a tent or a wind screen. It might also be used as a ground cover to keep the survivors dry. It’s shape, when contrasted with the surrounding terrain, makes it a signaling device."\n', 
    9 : 'A sectional air map made of plastic: \n"This is also among the least desirable of the items because it will encourage individuals to try to walk to the nearest town. It’s only useful feature is as a ground cover to keep someone dry."\n', 
    10 : 'Half a bottle of 85-proof whisky: \n"The only uses of whiskey are as an aid in fire building and as a fuel for a torch (made by soaking a piece of clothing in the whiskey and attaching it to a tree branch). The empty bottle could be used for storing water. The danger of whiskey is that someone might drink it, thinking it would bring warmth. Alcohol takes on the temperature it is exposed to, and a drink of minus 30 degrees fahrenheit whiskey would freeze a person’s esophagus and stomach. Alcohol also dilates the blood vessels in the skin, resulting in chilled blood being carried back to the heart, resulting in a rapid loss of body heat. Thus, a drunk person is more likely to get hypothermia than a sober person is."\n', 
    11 : 'A compass: \n"Because a compass might encourage someone to try to walk to the nearest town, it is a dangerous item. It’s only redeeming feature is that it could be used as a reflector of sunlight (due to its glass top)."\n', 
    12 : 'A family-size chocolate bar: \n"Chocolate will provide some food energy. Since it contains mostly carbohydrates, it supplies the energy without making digestive demands on the body."\n'
}