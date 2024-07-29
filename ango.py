import random
import math
print("暗号化しますか?復元化しますか?a/h")
kotae = input()
spell1 = ["¿", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ",", ".", "!", "?", "-", "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "=", "~", "^", ";", ":", "[", "]", "+", "*", "/", "<", ">", "|", "@", " "]
japanese = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽゃゅょっぁぃぅぇぉアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポャュョッァィゥェォｱｲｳｴｵｶｷhｸ ｹ ｺ ｻ ｼ ｽ ｾ ｿ ﾀ ﾁ ﾂ ﾃ ﾄ ﾅ ﾆ ﾇ ﾈ ﾉ ﾊ ﾋ ﾌ ﾍ ﾎ ﾏ ﾐ ﾑ ﾒ ﾓ ﾔ ﾕ ﾖ ﾗ ﾘ ﾙ ﾚ ﾛ ﾜ ｦ ﾝｳﾞ ｶﾞ ｷﾞ ｸﾞ ｹﾞ ｺﾞ ｻﾞ ｼﾞ ｽﾞ ｾﾞ ｿﾞ ﾀﾞ ﾁﾞ ﾂﾞ ﾃﾞ ﾄﾞ ﾊﾞ ﾋﾞ ﾌﾞ ﾍﾞ ﾎﾞ ﾊﾟ ﾋﾟ ﾌﾟ ﾍﾟ ﾎﾟ ｧ ｨ ｩ ｪ ｫ ｬ ｭ ｮ ｯ。、ー～「」！”＃＄％＆’（）!\"#$%&\'()"
chinese_character = "亜哀愛悪握圧扱安暗案以位依偉囲委威尉意慰易為異移維緯胃衣違遺医井域育一壱逸稲芋印員因姻引飲院陰隠韻右宇羽雨渦浦運雲営影映栄永泳英衛詠鋭液疫益駅悦謁越閲円園宴延援沿演炎煙猿縁遠鉛塩汚凹央奥往応押横欧殴王翁黄沖億屋憶乙卸恩温穏音下化仮何価佳加可夏嫁家寡科暇果架歌河火禍稼箇花荷華菓課貨過蚊我画芽賀雅餓介会解回塊壊快怪悔懐戒拐改械海灰界皆絵開階貝劾外害慨概涯街該垣嚇各拡格核殻獲確穫覚角較郭閣隔革学岳楽額掛潟割喝括活渇滑褐轄且株刈乾冠寒刊勘勧巻喚堪完官寛干幹患感慣憾換敢棺款歓汗漢環甘監看管簡緩缶肝艦観貫還鑑間閑関陥館丸含岸眼岩頑顔願企危喜器基奇寄岐希幾忌揮机旗既期棋棄機帰気汽祈季紀規記貴起軌輝飢騎鬼偽儀宜戯技擬欺犠疑義議菊吉喫詰却客脚虐逆丘久休及吸宮弓急救朽求泣球究窮級糾給旧牛去居巨拒拠挙虚許距漁魚享京供競共凶協叫境峡強恐恭挟教橋況狂狭矯胸脅興郷鏡響驚仰凝暁業局曲極玉勤均斤琴禁筋緊菌襟謹近金吟銀九句区苦駆具愚虞空偶遇隅屈掘靴繰桑勲君薫訓群軍郡係傾刑兄啓型契形径恵慶憩掲携敬景渓系経継茎蛍計警軽鶏芸迎鯨劇撃激傑欠決潔穴結血月件倹健兼券剣圏堅嫌建憲懸検権犬献研絹県肩見謙賢軒遣険顕験元原厳幻弦減源玄現言限個古呼固孤己庫弧戸故枯湖誇雇顧鼓五互午呉娯後御悟碁語誤護交侯候光公功効厚口向后坑好孔孝工巧幸広康恒慌抗拘控攻更校構江洪港溝甲皇硬稿紅絞綱耕考肯航荒行衡講貢購郊酵鉱鋼降項香高剛号合拷豪克刻告国穀酷黒獄腰骨込今困墾婚恨懇昆根混紺魂佐唆左差査砂詐鎖座債催再最妻宰彩才採栽歳済災砕祭斎細菜裁載際剤在材罪財坂咲崎作削搾昨策索錯桜冊刷察撮擦札殺雑皿三傘参山惨散桟産算蚕賛酸暫残仕伺使刺司史嗣四士始姉姿子市師志思指支施旨枝止死氏祉私糸紙紫肢脂至視詞詩試誌諮資賜雌飼歯事似侍児字寺慈持時次滋治璽磁示耳自辞式識軸七執失室湿漆疾質実芝舎写射捨赦斜煮社者謝車遮蛇邪借勺尺爵酌釈若寂弱主取守手朱殊狩珠種趣酒首儒受寿授樹需囚収周宗就州修愁拾秀秋終習臭舟衆襲週酬集醜住充十従柔汁渋獣縦重銃叔宿淑祝縮粛塾熟出術述俊春瞬准循旬殉準潤盾純巡遵順処初所暑庶緒署書諸助叙女序徐除傷償勝匠升召商唱奨宵将小少尚床彰承抄招掌昇昭晶松沼消渉焼焦照症省硝礁祥称章笑粧紹肖衝訟証詔詳象賞鐘障上丈乗冗剰城場壌嬢常情条浄状畳蒸譲醸錠嘱飾植殖織職色触食辱伸信侵唇娠寝審心慎振新森浸深申真神紳臣薪親診身辛進針震人仁刃尋甚尽迅陣酢図吹垂帥推水炊睡粋衰遂酔錘随髄崇数枢据杉澄寸世瀬畝是制勢姓征性成政整星晴正清牲生盛精聖声製西誠誓請逝青静斉税隻席惜斥昔析石積籍績責赤跡切拙接摂折設窃節説雪絶舌仙先千占宣専川戦扇栓泉浅洗染潜旋線繊船薦践選遷銭銑鮮前善漸然全禅繕塑措疎礎祖租粗素組訴阻僧創双倉喪壮奏層想捜掃挿操早曹巣槽燥争相窓総草荘葬藻装走送遭霜騒像増憎臓蔵贈造促側則即息束測足速俗属賊族続卒存孫尊損村他多太堕妥惰打駄体対耐帯待怠態替泰滞胎袋貸退逮隊代台大第題滝卓宅択拓沢濯託濁諾但達奪脱棚谷丹単嘆担探淡炭短端胆誕鍛団壇弾断暖段男談値知地恥池痴稚置致遅築畜竹蓄逐秩窒茶嫡着中仲宙忠抽昼柱注虫衷鋳駐著貯丁兆帳庁弔張彫徴懲挑朝潮町眺聴脹腸調超跳長頂鳥勅直朕沈珍賃鎮陳津墜追痛通塚漬坪釣亭低停偵貞呈堤定帝底庭廷弟抵提程締艇訂逓邸泥摘敵滴的笛適哲徹撤迭鉄典天展店添転点伝殿田電吐塗徒斗渡登途都努度土奴怒倒党冬凍刀唐塔島悼投搭東桃棟盗湯灯当痘等答筒糖統到討謄豆踏逃透陶頭騰闘働動同堂導洞童胴道銅峠匿得徳特督篤毒独読凸突届屯豚曇鈍内縄南軟難二尼弐肉日乳入如尿任妊忍認寧猫熱年念燃粘悩濃納能脳農把覇波派破婆馬俳廃拝排敗杯背肺輩配倍培媒梅買売賠陪伯博拍泊白舶薄迫漠爆縛麦箱肌畑八鉢発髪伐罰抜閥伴判半反帆搬板版犯班畔繁般藩販範煩頒飯晩番盤蛮卑否妃彼悲扉批披比泌疲皮碑秘罷肥被費避非飛備尾微美鼻匹必筆姫百俵標氷漂票表評描病秒苗品浜貧賓頻敏瓶不付夫婦富布府怖扶敷普浮父符腐膚譜負賦赴附侮武舞部封風伏副復幅服福腹複覆払沸仏物分噴墳憤奮粉紛雰文聞丙併兵塀幣平弊柄並閉陛米壁癖別偏変片編辺返遍便勉弁保舗捕歩補穂募墓慕暮母簿倣俸包報奉宝峰崩抱放方法泡砲縫胞芳褒訪豊邦飽乏亡傍剖坊妨帽忘忙房暴望某棒冒紡肪膨謀貿防北僕墨撲朴牧没堀奔本翻凡盆摩磨魔麻埋妹枚毎幕膜又抹末繭万慢満漫味未魅岬密脈妙民眠務夢無矛霧婿娘名命明盟迷銘鳴滅免綿面模茂妄毛猛盲網耗木黙目戻問紋門匁夜野矢厄役約薬訳躍柳愉油癒諭輸唯優勇友幽悠憂有猶由裕誘遊郵雄融夕予余与誉預幼容庸揚揺擁曜様洋溶用窯羊葉要謡踊陽養抑欲浴翌翼羅裸来頼雷絡落酪乱卵欄濫覧利吏履理痢裏里離陸律率立略流留硫粒隆竜慮旅虜了僚両寮料涼猟療糧良量陵領力緑倫厘林臨輪隣塁涙累類令例冷励礼鈴隷零霊麗齢暦歴列劣烈裂廉恋練連錬炉路露労廊朗楼浪漏老郎六録論和話賄惑枠湾腕 　　 ⊃ ♪ Ｏ ｒ さ ひ わ ス ブ ン β Ё в ю ┝ ≒ ∫ ∠ ∩ 　 、 ‐ 【 ＊ ∪ † Ｐ ｓ ざ び ゐ ズ プ ヴ γ Ж г я ┰ ≡ ⊥ ∵ ∪ 　 。 ／ 】 ＠ ∩ ‡ Ｑ ｔ し ぴ ゑ セ ヘ ヵ δ З д ─ ┥ 　 ， ＼ ＋ § ∧ ¶ Ｒ ｕ じ ふ を ゼ ベ ヶ ε И е │ ┸ ! : S l ． ～ － ☆ ∨ ◯ Ｓ ｖ す ぶ ん ソ ペ Α ζ Й ё ┌ ╂  ; T m ・ ∥ ± ★ ￢ 0 Ｔ ｗ ず ぷ ァ ゾ ホ Β η К ж ┐ < U n ： ｜ × ○ ⇒ 1 Ｕ ｘ せ へ ア タ ボ Γ θ Л з ┘ $ = V o ； … ÷ ● ⇔ 2 Ｖ ｙ ぜ べ ィ ダ ポ Δ ι М и └ % > W p ？ ‥ ＝ ◎ ∀ 3 Ｗ ｚ そ ぺ イ チ マ Ε κ Н й ├ & ? X q ！ ‘ ≠ ◇ ∃ 4 Ｘ ぁ ぞ ほ ゥ ヂ ミ Ζ λ О к ┬ ' @ Y r ゛ ’ ＜ ◆ ∠ 5 Ｙ あ た ぼ ウ ッ ム Η μ П л ┤ ( A Z s ゜ “ ＞ □ ⊥ 6 Ｚ ぃ だ ぽ ェ ツ メ Θ ν Р м ┴ ) B [ t ´ ” ≦ ■ ⌒ 7 ａ い ち ま エ ヅ モ Ι ξ С н ┼ * C \ u ｀ （ ≧ △ ∂ 8 ｂ ぅ ぢ み ォ テ ャ Κ ο Т о ━ + D ] v ¨ ） ∞ ▲ ∇ 9 ｃ う っ む オ デ ヤ Λ π У п ┃ , E ^ w ＾ 〔 ∴ ▽ ≡ Ａ ｄ ぇ つ め カ ト ュ Μ ρ Ф р ┏ - F _ x ￣ 〕 ♂ ▼ ≒ Ｂ ｅ え づ も ガ ド ユ Ν σ Х с ┓ . G ` y ＿ ［ ♀ ※ ≪ Ｃ ｆ ぉ て ゃ キ ナ ョ Ξ τ Ц т ┛ / H a z ヽ ］ ° 〒 ≫ Ｄ ｇ お で や ギ ニ ヨ Ο υ Ч у ┗ 0 I b { ヾ ｛ ′ → √ Ｅ ｈ か と ゅ ク ヌ ラ Π φ Ш ф ┣ 1 J c | ゝ ｝ ″ ← ∽ Ｆ ｉ が ど ゆ グ ネ リ Ρ χ Щ х ┳ 2 K d } ゞ 〈 ℃ ↑ ∝ Ｇ ｊ き な ょ ケ ノ ル Σ ψ Ъ ц ┫ 3 L e ~ 〃 〉 ￥ ↓ ∵ Ｈ ｋ ぎ に よ ゲ ハ レ Τ ω Ы ч ┻ 4 M f 仝 《 ＄ 〓 ∫ Ｉ ｌ く ぬ ら コ バ ロ Υ А Ь ш ╋ 5 N g 々 》 ￠ ∈ ∬ Ｊ ｍ ぐ ね り ゴ パ ヮ Φ Б Э щ ┠ 6 O h 〆 「 ￡ ∋ Å Ｋ ｎ け の る サ ヒ ワ Χ В Ю ъ ┯ 7 P i 〇 」 ％ ⊆ ‰ Ｌ ｏ げ は れ ザ ビ ヰ Ψ Г Я ы ┨ 8 Q j ー 『 ＃ ⊇ ♯ Ｍ ｐ こ ば ろ シ ピ ヱ Ω Д а ь ┷ 9 R k ― 』 ＆ ⊂ ♭ Ｎ ｑ ご ぱ ゎ ジ フ ヲ α Е б э ┿"
for i in range(len(spell1)):
    spell1.append(spell1[i].lower())
for i in range(len(japanese)):
    if not japanese[i] in spell1:
        spell1.append(chinese_character[i])
for i in range(len(chinese_character)):
    if not chinese_character[i] in spell1:
        spell1.append(chinese_character[i])
spell = []
spell1_len = len(spell1)
for i in range(spell1_len - 1):
    spell.append(spell1[(i * 100) % (len(spell1) - 1)])
    spell1.pop((i * 100) % (len(spell1) - 1))
spell.append(spell1[0])
if kotae == "a":
    rand = random.randint(2, 5)
    rand2 = random.randint(2, 3)
    print("暗号化する文章を入れてください。(だいたい全部変換できます。)")
    bunsyou = input()
    angounum = []
    ango = ""
    for i in range(len(bunsyou)):
        j = 0
        while bunsyou[i] != spell[j]:
            j += 1
            if j == len(spell):
                break
        angounum.append(j)
    for i in range(len(bunsyou)):
        angounum[i] = angounum[i] + rand + rand2 * i
        angounum[i] = angounum[i] % len(spell)
    for i in range(len(bunsyou)):
        ango = ango + spell[angounum[i]]
    ango = ango + spell[rand]
    ango = ango + spell[rand2]
    print(ango)
elif kotae == "h":
    print("復元化する文章を入れてください。(変換不能文字は「¿」として出ます。)")
    bunsyou = input()
    angounum = []
    ango = ""
    for i in range(len(bunsyou)):
        j = 0
        while bunsyou[i] != spell[j]:
            j += 1
        angounum.append((j + len(spell) * 1000000))
    for i in range(len(bunsyou) - 2):
        angounum[i] = (angounum[i] - int(angounum[-2]) - int(angounum[-1]) * i) % len(spell)
    for i in range(len(bunsyou) - 2):
        ango = ango + spell[angounum[i]]
    print(ango)
else:
    print("aかhでの回答をお願いします。")