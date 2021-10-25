# UnderDark规则书

[TOC]

## 前言

## 1 快速创建角色
这一章将会引导你们快速创建一个角色，每节都会给出一个示范，如果对术语有疑惑的话清阅读后续章节。

### 1.1 设计形象
首先我们需要构思一个角色形象，然后分三段文字进行说明，你可以边写边想，反复修改得到最终的形象。
- 核心：用最简明扼要的文字概括你的角色。
- 背景：外在和过去，介绍角色的外貌和处境，外部面临的困难，影响最深的经历等。
- 信念：内在和未来，介绍角色的信念和矛盾，内心挣扎的矛盾，对自己未来的期望等。

此处我们给出一个简单的例子：
- 核心：精益求精的精灵女弓手姬塔。
- 背景：姬塔师承一名伟大的精灵弓手，她遵守师父的教诲在大陆上旅行，增长自己的见识。
- 信念：姬塔对弓的一切都很感兴趣，她渴望能够进一步磨练自己的技术并传承下去。

### 1.2 分配属性
六项属性分别表示角色在不同方面的基本能力，创建角色时直接把+3/+2/+2/+1/+1/+0自由分配到六项属性上。
- 力量：肌肉强度与身体素质。
- 敏捷：反应速度和协调能力。
- 智力：逻辑思考能力和记忆力。
- 感知：感官和直觉。
- 魅力：社交能力和外貌气质。
- 资源：财富和人脉。

分配属性时可以根据自己预先设计的角色形象进行，下面给出一个智力的例子：
- +0：未受训，你是平庸的大多数。
- +1：受训，你经常进行体力劳动，或许是个农民。
- +2：熟练，你经常进行高强度的体力训练，应该是个士兵。
- +3：专家，你强壮得像头牛，只有极少数人能达到这个水平。
- +4：大师，你的强壮达到了人类的极限，不论善恶，你都将在历史上留名。

下面是一个属性分配范例：姬塔作为一名优秀的弓手，敏捷应该是她最高的属性（+3），由于长期在外旅行，缺乏稳定的收入来源，资源应该是她较低的属性（+0），精灵一般都拥有敏锐的感官和优雅的姿态，所以姬塔的感知和魅力十分出众（+2），姬塔师承武术名门，基本的体能训练和知识教育是少不了的，所以力量和智力也尚可（+1）。

### 1.3 设计特技
特技表示角色的特殊能力，可以用下面的两个模板自行设计两个有趣的能力。
1. 擅长模板：你在某种条件下，使用一项属性，进行一项行动时，获得一定加值。
2. 能力模板：你能够做一件很酷的事情，次数限制视情况而定。

对于擅长模板来说，条件越苛刻，加值就越高：
- +1：条件极易满足，几乎能覆盖所有游戏时间。
- +2：条件容易满足，但也很容易打破。
- +3：条件较难满足，偶尔能触发几次。
- +4：条件极难满足，几乎不能满足条件。

对于能力模板来说，能做的事情越强，次数限制也越严格。
- 无限制：较为普通的能力，不会对游戏产生较大的影响。
- 每场景：非常实用的能力，能对游戏产生一定影响。
- 每聚会：令人印象深刻的能力，会对游戏产生巨大影响。
- 每冒险：一锤定音的能力，会对游戏产生决定性的影响。

PS：如果是最初创建人物，不建议使用擅长模板（+4）和能力模板（每冒险），因为这种能力整个游戏过程中也不会用到几次，而你最初只拥有两个特技。此外如果你没有什么好的灵感，可以参考第"4 设计特技"一章给出的特技。

### 1.4 补充状态
状态有4种，命运点会在每次聚会开始时恢复，体力和理智会在场景结束后恢复。
- 命运：默认值2，消耗命运点可以引用形象获得加值。
- 生命：默认值2+力量，受到现实的伤害会损失生命。
- 理智：默认值2+感知，受到精神的冲击会损失理智。

### 1.5 范例角色
```txt
角色：姬塔
核心：精益求精的精灵女弓手
背景：姬塔师承一名伟大的精灵弓手，她遵守师父的教诲在大陆上旅行，增长自己的见识。
信念：姬塔对弓的一切都很感兴趣，她渴望能够进一步磨练自己的技术并传承下去。
状态：命运2/2，生命3/3，理智4/4
属性：力量+1，敏捷+3，智力+1，感知+2，魅力+2，资源+0
特技：
    弓箭手：用弓进行敏捷攻击获得+2加值。
    动物之友：能够与动物交流。
装备：
```

## 2 进行游戏
游戏中的一场冒险，就像电影一样是由一个又一个场景组成的，我们

### 2.1 命运骰和检定
*“听说你在家骰出了6个18？”（疑惑脸）*

命运骰是一种特殊的六面骰，它的六个面分别是‘+1’、‘+1’、‘0’、‘0’、‘-1’、‘-1’。在游戏中我们会遇到非常多的检定，每次检定需要投掷四个命运骰，把命运骰的结果和各种加值累加起来，和GM预设的难度或者其他人的检定结果进行比较，决定我们行动带来的结果。

### 2.2 使用形象
*形象是个筐，什么都能往里装，这回看谁还不写背景。*

存在两种使用形象的方法：
- 引用形象：如果你发现你的形象对你的检定结果有利，你可以花费一点命运点，给你的检定带来+2加值。
- 强迫形象：如果你或者其他人发现你的形象对你的检定结果不利，他们可以提出来并要求你获得-2减值，不过作为补偿你可以补充一点命运点。

在上面我们已经提到过，每个玩家控制的角色都拥有三个形象。但其实形象是一个很宽泛的概念。在场景中你也可以通过“创造形象”动作（见2.4节），动用你的想象力，给你自己、你的敌人、甚至环境中的物品，附加一些临时形象。

### 2.3 行动轮
*“年轻人不讲武德，来骗，来偷袭，我这个三百岁的老同志，这好吗？这不好。”——在决斗中被恩崔立喷了一脸污水的崔斯特。*

在每个场景开始时，需要进行敏捷检定来决定行动顺序，一个人行动一次称作一回合，所有人都依次行动一次称作一轮。如果有一方进行偷袭，那么第一轮只有偷袭方可以行动。

### 2.4 四种动作
*“你一回合能做一个标准动作，一个移动动作，和一个即时动作；你可以放弃你的标准动作得到另一个移动动作；你也可以放弃你的标准动作和移动动作进行全回合攻击。回合外你可以做一个反应动作。此外根据扩展规则，你也可以在回合中增加一个迅捷动作。。。”——一位正在解读龙与地下城三版规则的城主。*

在回合内你可以做一个动作：
- 克服困难：这是最基本的动作类型，通过属性检定对抗预设的难度，如果成功则克服困难达成目的。
- 创造形象：你可以给场景中的一个对象创造一个临时形象，并获得该形象的一次免费引用，如果感觉自己遇到了较大的困难，就运用想象力，创造一些优势吧。
- 攻击：攻击与防御相对抗，如果成功，则造成差值的伤害。

在回合外你可以做不限次数的防御动作：
- 防御：对攻击的被动回应。

克服困难的难度设置一般有如下标准：
- 0：简单，普通人也能解决的困难。
- 1：较易，受过一些训练就能解决的困难。
- 2：普通，总算有些挑战的困难。
- 3：较难，需要专家才能解决的困难。
- 4：极难，普通人几乎无法解决的困难。

### 2.5 负伤和休整
在游戏中我们可能会受到物理伤害和精神伤害。如果

## 3 使用属性
### 3.1 力量
### 3.2 敏捷
### 3.3 智力
### 3.4 感知
### 3.5 魅力
### 3.6 资源

## 4 设计特技

### 4.1 战士特技
|武术特技|
|:-|
|弓箭熟练：你熟练于使用弓箭，使用弓进行敏捷攻击有+2加值。|

### 4.2 巫师特技
|巫师特技|
|:-|
|火球术：你可以投掷会爆炸的火球，对场景中的所有角色进行1次智力攻击，每场景1次。|

### 4.3 盗贼特技
|盗贼特技|
|:-|
|背刺：你是背后捅人刀子的专家，使用匕首进行偷袭的敏捷攻击有+3加值。|

### 5 装备