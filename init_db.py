from app import app, db, Topic, Concept, QuizQuestion
from datetime import datetime

def init_db():
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Clear existing data
        QuizQuestion.query.delete()
        Concept.query.delete()
        Topic.query.delete()
        
        # Create kid-friendly topics
        topics = [
            {
                'name_en': 'Robot Friends',
                'name_zh': '机器人朋友',
                'description_en': 'Meet our friendly robot helpers!',
                'description_zh': '认识我们的机器人朋友！',
                'icon': 'fas fa-robot',
                'order': 1
            },
            {
                'name_en': 'Smart Games',
                'name_zh': '智能游戏',
                'description_en': 'Play fun games with computers!',
                'description_zh': '和电脑一起玩有趣的游戏！',
                'icon': 'fas fa-gamepad',
                'order': 2
            },
            {
                'name_en': 'Magic Pictures',
                'name_zh': '神奇图片',
                'description_en': 'See how computers understand pictures!',
                'description_zh': '看看电脑如何理解图片！',
                'icon': 'fas fa-camera-retro',
                'order': 3
            },
            {
                'name_en': 'Talking Computers',
                'name_zh': '会说话的电脑',
                'description_en': 'Learn how computers understand words!',
                'description_zh': '了解电脑如何理解语言！',
                'icon': 'fas fa-comments',
                'order': 4
            },
            {
                'name_en': 'Animal Friends',
                'name_zh': '动物朋友',
                'description_en': 'Help computers recognize animals!',
                'description_zh': '帮助电脑认识动物！',
                'icon': 'fas fa-paw',
                'order': 5
            }
        ]
        
        db_topics = {}
        for topic_data in topics:
            topic = Topic(**topic_data)
            db.session.add(topic)
            db.session.flush()
            db_topics[topic.name_en] = topic
        
        # Create kid-friendly concepts for Robot Friends
        robot_concepts = [
            {
                'name_en': 'Meet Our Robot Friend',
                'name_zh': '认识机器人朋友',
                'content_en': '''
                Hello friends! Today we're going to meet a very special friend - our Robot!
                
                Our Robot friend is like a very smart toy that can:
                - Learn new things just like you!
                - Remember pictures and colors
                - Play fun games with us
                - Help us with our homework
                
                Isn't that amazing? Let's learn more about our Robot friend!
                ''',
                'content_zh': '''
                你好朋友们！今天我们要认识一个特别的朋友 - 我们的机器人！
                
                我们的机器人朋友就像一个非常聪明的玩具：
                - 可以像你一样学习新东西！
                - 记住图片和颜色
                - 和我们一起玩有趣的游戏
                - 帮助我们做作业
                
                是不是很神奇？让我们一起来了解我们的机器人朋友吧！
                ''',
                'difficulty': 'beginner',
                'estimated_time': 10,
                'topic_id': db_topics['Robot Friends'].id,
                'quiz_questions': [
                    {
                        'question_en': 'What can our Robot friend do?',
                        'question_zh': '我们的机器人朋友会做什么？',
                        'options_en': [
                            'Learn and play with us',
                            'Make ice cream',
                            'Fly to the moon',
                            'Drive a car'
                        ],
                        'options_zh': [
                            '和我们一起学习和玩耍',
                            '制作冰淇淋',
                            '飞到月球上',
                            '开车'
                        ],
                        'correct_answer': 0,
                        'explanation_en': 'Our Robot friend loves to learn and play with us!',
                        'explanation_zh': '我们的机器人朋友喜欢和我们一起学习和玩耍！'
                    }
                ]
            },
            {
                'name_en': 'Robot Dance Party',
                'name_zh': '机器人舞会',
                'content_en': '''
                Get ready to dance with Robot! Today we're having a fun dance party!
                
                Robot can:
                - Move to the music
                - Copy your dance moves
                - Make funny dance poses
                - Teach you new dance steps
                
                Let's dance and have fun with Robot!
                ''',
                'content_zh': '''
                准备和机器人一起跳舞吧！今天我们要开一个有趣的舞会！
                
                机器人可以：
                - 跟着音乐动起来
                - 模仿你的舞蹈动作
                - 做有趣的舞蹈姿势
                - 教你新的舞步
                
                让我们和机器人一起跳舞，开心玩耍吧！
                ''',
                'difficulty': 'beginner',
                'estimated_time': 15,
                'topic_id': db_topics['Robot Friends'].id,
                'quiz_questions': [
                    {
                        'question_en': 'What can Robot do at the dance party?',
                        'question_zh': '机器人在舞会上会做什么？',
                        'options_en': [
                            'Dance and copy moves',
                            'Make food',
                            'Take a nap',
                            'Read books'
                        ],
                        'options_zh': [
                            '跳舞和模仿动作',
                            '做食物',
                            '睡觉',
                            '读书'
                        ],
                        'correct_answer': 0,
                        'explanation_en': 'Robot loves to dance and copy your fun dance moves!',
                        'explanation_zh': '机器人喜欢跳舞和模仿你有趣的舞蹈动作！'
                    }
                ]
            },
            {
                'name_en': 'Robot Helper Day',
                'name_zh': '机器人助手日',
                'content_en': '''
                Today we'll learn how Robot helps us every day!
                
                Robot is a great helper who can:
                - Help clean up toys
                - Sort colors and shapes
                - Remember where things go
                - Make tasks fun and easy
                
                Let's see all the helpful things Robot can do!
                ''',
                'content_zh': '''
                今天我们来学习机器人如何帮助我们！
                
                机器人是一个很棒的助手，它可以：
                - 帮忙收拾玩具
                - 分类颜色和形状
                - 记住东西放在哪里
                - 让任务变得有趣和简单
                
                让我们看看机器人能做哪些有帮助的事情！
                ''',
                'difficulty': 'beginner',
                'estimated_time': 15,
                'topic_id': db_topics['Robot Friends'].id,
                'quiz_questions': [
                    {
                        'question_en': 'How does Robot help us?',
                        'question_zh': '机器人如何帮助我们？',
                        'options_en': [
                            'Cleans and sorts things',
                            'Makes rain',
                            'Builds houses',
                            'Cooks dinner'
                        ],
                        'options_zh': [
                            '清理和分类东西',
                            '制造下雨',
                            '建造房子',
                            '做晚餐'
                        ],
                        'correct_answer': 0,
                        'explanation_en': 'Robot helps us by cleaning up and sorting things!',
                        'explanation_zh': '机器人通过清理和分类东西来帮助我们！'
                    }
                ]
            },
            {
                'name_en': 'Robot Story Time',
                'name_zh': '机器人故事时间',
                'content_en': '''
                Gather around for story time with Robot!
                
                Robot knows lots of stories about:
                - Friendly animals
                - Magic adventures
                - Brave heroes
                - Funny situations
                
                What story would you like Robot to tell today?
                ''',
                'content_zh': '''
                让我们一起来听机器人讲故事吧！
                
                机器人知道很多故事，关于：
                - 友好的动物
                - 神奇的冒险
                - 勇敢的英雄
                - 有趣的情况
                
                今天你想听机器人讲什么故事呢？
                ''',
                'difficulty': 'beginner',
                'estimated_time': 15,
                'topic_id': db_topics['Robot Friends'].id,
                'quiz_questions': [
                    {
                        'question_en': 'What stories does Robot know?',
                        'question_zh': '机器人知道什么样的故事？',
                        'options_en': [
                            'Animal and adventure stories',
                            'Only scary stories',
                            'No stories at all',
                            'Only grown-up stories'
                        ],
                        'options_zh': [
                            '动物和冒险故事',
                            '只有可怕的故事',
                            '完全不会讲故事',
                            '只有大人的故事'
                        ],
                        'correct_answer': 0,
                        'explanation_en': 'Robot knows lots of fun stories about animals and adventures!',
                        'explanation_zh': '机器人知道很多关于动物和冒险的有趣故事！'
                    }
                ]
            }
        ]
        
        for concept_data in robot_concepts:
            quiz_questions = concept_data.pop('quiz_questions')
            concept = Concept(**concept_data)
            db.session.add(concept)
            db.session.flush()
            
            for q_data in quiz_questions:
                q = QuizQuestion(concept_id=concept.id, **q_data)
                db.session.add(q)
        
        # Create concepts for Magic Pictures
        magic_pictures_concepts = [
            {
                'name_en': 'Colors and Shapes Adventure',
                'name_zh': '颜色和形状大冒险',
                'content_en': '''
                Hello little explorers! Let's go on a magical adventure with colors and shapes!
                
                Today we will learn how Robot sees:
                - Beautiful colors like red, blue, and yellow
                - Fun shapes like circles, squares, and triangles
                - Different sizes - big and small
                
                Can you help Robot find all the colors and shapes around you?
                ''',
                'content_zh': '''
                你好小探险家！让我们和颜色形状一起去冒险吧！
                
                今天我们要学习机器人如何看到：
                - 漂亮的颜色，比如红色、蓝色和黄色
                - 有趣的形状，比如圆形、正方形和三角形
                - 不同的大小 - 大的和小的
                
                你能帮助机器人找到你周围所有的颜色和形状吗？
                ''',
                'difficulty': 'beginner',
                'estimated_time': 15,
                'topic_id': db_topics['Magic Pictures'].id,
                'quiz_questions': [
                    {
                        'question_en': 'What can Robot see?',
                        'question_zh': '机器人能看到什么？',
                        'options_en': [
                            'Colors and shapes',
                            'Only black and white',
                            'Nothing at all',
                            'Only at night'
                        ],
                        'options_zh': [
                            '颜色和形状',
                            '只有黑白色',
                            '什么都看不见',
                            '只能在晚上看见'
                        ],
                        'correct_answer': 0,
                        'explanation_en': 'Robot can see lots of beautiful colors and fun shapes!',
                        'explanation_zh': '机器人能看到很多漂亮的颜色和有趣的形状！'
                    }
                ]
            },
            {
                'name_en': 'Picture Detective Game',
                'name_zh': '图片侦探游戏',
                'content_en': '''
                Let's play detective with Robot! We'll find hidden things in pictures!
                
                Robot can help us find:
                - Happy faces in photos
                - Hidden toys in a messy room
                - Your favorite cartoon characters
                - Special treasures in pictures
                
                Are you ready to be a picture detective with Robot?
                ''',
                'content_zh': '''
                让我们和机器人一起玩侦探游戏！我们要在图片中找到藏起来的东西！
                
                机器人可以帮我们找到：
                - 照片中的笑脸
                - 凌乱房间里藏着的玩具
                - 你最喜欢的卡通人物
                - 图片中的特别宝藏
                
                准备好和机器人一起当图片侦探了吗？
                ''',
                'difficulty': 'beginner',
                'estimated_time': 15,
                'topic_id': db_topics['Magic Pictures'].id,
                'quiz_questions': [
                    {
                        'question_en': 'What can we find in pictures with Robot?',
                        'question_zh': '我们可以和机器人在图片中找到什么？',
                        'options_en': [
                            'Happy faces and toys',
                            'Only numbers',
                            'Real food',
                            'Living animals'
                        ],
                        'options_zh': [
                            '笑脸和玩具',
                            '只有数字',
                            '真的食物',
                            '活的动物'
                        ],
                        'correct_answer': 0,
                        'explanation_en': 'Robot helps us find happy faces, toys, and many other fun things in pictures!',
                        'explanation_zh': '机器人帮助我们在图片中找到笑脸、玩具和许多其他有趣的东西！'
                    }
                ]
            },
            {
                'name_en': 'Magic Photo Album',
                'name_zh': '神奇相册',
                'content_en': '''
                Today we're making a special photo album with Robot!
                
                We can:
                - Take funny pictures together
                - Add sparkly stickers
                - Draw colorful frames
                - Write fun captions
                
                Let's make our photos magical with Robot!
                ''',
                'content_zh': '''
                今天我们要和机器人一起制作特别的相册！
                
                我们可以：
                - 一起拍有趣的照片
                - 添加闪亮的贴纸
                - 画上彩色的相框
                - 写上有趣的说明
                
                让我们和机器人一起让照片变得神奇吧！
                ''',
                'difficulty': 'beginner',
                'estimated_time': 15,
                'topic_id': db_topics['Magic Pictures'].id,
                'quiz_questions': [
                    {
                        'question_en': 'What can we do with our photo album?',
                        'question_zh': '我们可以用相册做什么？',
                        'options_en': [
                            'Add stickers and draw frames',
                            'Eat it',
                            'Make it fly',
                            'Turn it into a car'
                        ],
                        'options_zh': [
                            '添加贴纸和画相框',
                            '把它吃掉',
                            '让它飞起来',
                            '把它变成汽车'
                        ],
                        'correct_answer': 0,
                        'explanation_en': 'We can make our photo album special by adding stickers and drawing pretty frames!',
                        'explanation_zh': '我们可以通过添加贴纸和画漂亮的相框来让相册变得特别！'
                    }
                ]
            }
        ]
        
        # Create concepts for Talking Computers
        talking_computers_concepts = [
            {
                'name_en': 'Robot Learns to Talk',
                'name_zh': '机器人学说话',
                'content_en': '''
                Hi friends! Today we're going to teach Robot how to talk!
                
                Robot can:
                - Say "Hello" and "Goodbye"
                - Tell fun stories
                - Sing songs with us
                - Answer our questions
                
                Let's help Robot learn new words together!
                ''',
                'content_zh': '''
                大家好！今天我们要教机器人说话！
                
                机器人可以：
                - 说"你好"和"再见"
                - 讲有趣的故事
                - 和我们一起唱歌
                - 回答我们的问题
                
                让我们一起帮助机器人学习新的词语吧！
                ''',
                'difficulty': 'beginner',
                'estimated_time': 15,
                'topic_id': db_topics['Talking Computers'].id,
                'quiz_questions': [
                    {
                        'question_en': 'What can Robot say?',
                        'question_zh': '机器人会说什么？',
                        'options_en': [
                            'Hello and stories',
                            'Only animal sounds',
                            'Nothing at all',
                            'Only numbers'
                        ],
                        'options_zh': [
                            '你好和故事',
                            '只会动物叫声',
                            '什么都不会说',
                            '只会数字'
                        ],
                        'correct_answer': 0,
                        'explanation_en': 'Robot can say hello and tell us fun stories!',
                        'explanation_zh': '机器人会说你好，还会给我们讲有趣的故事！'
                    }
                ]
            }
        ]
        
        # Create concepts for Animal Friends
        animal_friends_concepts = [
            {
                'name_en': 'Animal Picture Fun',
                'name_zh': '动物图片乐趣',
                'content_en': '''
                Welcome to the animal zoo! Let's help Robot learn about animals!
                
                We can show Robot pictures of:
                - Cute cats and dogs
                - Big elephants and giraffes
                - Colorful birds and fish
                - Fast rabbits and tigers
                
                Can you help Robot name all these animals?
                ''',
                'content_zh': '''
                欢迎来到动物园！让我们帮助机器人认识动物！
                
                我们可以给机器人看：
                - 可爱的猫和狗
                - 大象和长颈鹿
                - 彩色的鸟和鱼
                - 跑得快的兔子和老虎
                
                你能帮助机器人说出这些动物的名字吗？
                ''',
                'difficulty': 'beginner',
                'estimated_time': 15,
                'topic_id': db_topics['Animal Friends'].id,
                'quiz_questions': [
                    {
                        'question_en': 'What animals can Robot learn about?',
                        'question_zh': '机器人可以学习认识什么动物？',
                        'options_en': [
                            'Cats, dogs, and elephants',
                            'Only fish',
                            'Only insects',
                            'No animals'
                        ],
                        'options_zh': [
                            '猫、狗和大象',
                            '只有鱼',
                            '只有昆虫',
                            '没有动物'
                        ],
                        'correct_answer': 0,
                        'explanation_en': 'Robot can learn about many different animals like cats, dogs, and elephants!',
                        'explanation_zh': '机器人可以学习认识很多不同的动物，比如猫、狗和大象！'
                    }
                ]
            }
        ]
        
        # Add all concept lists to a single list for processing
        all_concepts = [
            (magic_pictures_concepts, 'Magic Pictures'),
            (talking_computers_concepts, 'Talking Computers'),
            (animal_friends_concepts, 'Animal Friends')
        ]
        
        # Process all concepts
        for concepts, topic_name in all_concepts:
            for concept_data in concepts:
                quiz_questions = concept_data.pop('quiz_questions')
                concept = Concept(**concept_data)
                db.session.add(concept)
                db.session.flush()
                
                for q_data in quiz_questions:
                    q = QuizQuestion(concept_id=concept.id, **q_data)
                    db.session.add(q)
        
        db.session.commit()
        print("Database initialized with kid-friendly content!")

if __name__ == '__main__':
    init_db()
