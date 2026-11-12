#import
import math
import datetime as dt
import random as rd
import os
# global変数
glo = 0
glo1 = 0
glo_point =0
# input関数
def inp():
    while True:
        try:
            num = int(input(" >>"))
            return num
        except ValueError:
            print("不正な入力値です")
# str input関数
def strinp():
    while True:
        try:
            num = str(input(" >>"))
            return num
        except ValueError:
            print("不正な入力値です") 

# hittto&blow
def hitblow():
    def strat():
        global glo_point
        print("ゲームを始めます。")
        print("新しく始める:1 | セーブデータを読み込んで始める:2")
        gameset = inp()
        if gameset == 1:
            while True:
                print("あなたの名前を教えてください")
                name = strinp()
                if os.path.isfile(f"{str(name)}.txt") == True:
                    print("その名前は既に存在しています")
                    continue
                elif os.path.isfile(f"{str(name)}.txt") == False:
                    break
            while True:
                print(f"名前は{name}でよろしいですか?\nOK!! : 1 | 考え直す : 2")
                namelock = inp()
                if namelock == 1:
                    return name
                elif namelock == 2:
                    print("あなたの名前を教えてください")
                    name = strinp()
                    continue
                else:
                    print("不正な入力値です")
                    continue
        elif gameset == 2:
            while True:
                print("セーブした名前を教えてください(メニューへ戻る>>end)")
                name = strinp()
                if name == "end":
                    print("メニューに戻ります")
                    gameset = 0
                    strat()
                    break
                elif os.path.isfile(f"{name}.txt") == True:
                    with open(f"{name}.txt", "r", encoding="UTF-8") as r_file:
                        playerdata = r_file.read()
                        glo_point = glo_point + int(playerdata) 
                        return name
                else:
                    print("データが存在しません")
                    continue
        else:
            print("不正な入力値です")
            strat()
       

    anser_list = []
    npc_list = []
    # ノーマルモード
    def npc_nomal():
        num = rd.randint(1,9)
        npc_list.append(num) 
        for i in range(2):
            num = rd.randint(0,9)
            npc_list.append(num) 
    # ノーマルモード処理
    def hantei():
        global glo_point
        ans = str(npc_list[0])+str(npc_list[1])+str(npc_list[2])
        npc_ans = int(ans)
        count = 0
        print("ランダムに選ばれた数字３桁を当ててください\n当てると1ポイントゲットできます")
        while True:
            count += 1
            seikai = 0
            matigai = 0
            print("数字３桁を入力してください")
            p_anser = inp()
            if len(str(p_anser)) >= 4:
                print("不正な入力値です")
            elif len(str(p_anser)) <= 2:
                print("不正な入力値です")
            elif p_anser == npc_ans:
                glo_point += 1
                print(f"{count}目で正解しました")
                print(f"正解は{npc_ans}でした!!\n1ポイントゲット\n現在のポイントは{glo_point}")
                break
            elif p_anser != npc_ans:
                print("不正解")
                anser_list.append(p_anser)
                anser_num = p_anser
                p_anser1 = anser_num%10
                anser_num//=10
                p_anser10 = anser_num%10
                anser_num//=10
                p_anser100=anser_num%10
                ans_num = npc_ans
                npc_ans1 = ans_num%10
                ans_num//=10
                npc_ans10 = ans_num%10
                ans_num//=10
                npc_ans100=ans_num%10
                if p_anser1 ==npc_ans1:
                    seikai += 1
                if p_anser10 == npc_ans10:
                    seikai += 1
                if p_anser100 == npc_ans100:
                    seikai += 1
                print(f"3桁のうち{seikai}個正解です。")
                print(f"現在の回答{anser_list}")
    #ハードモード 
    def npc_hard():
        num = rd.randint(1,9)
        npc_list.append(num) 
        for i in range(4):
            num = rd.randint(0,9)
            npc_list.append(num) 
    #ハードモード処理
    def hard():
        global glo_point
        ans = str(npc_list[0])+str(npc_list[1])+str(npc_list[2])+str(npc_list[3])+str(npc_list[4])
        npc_ans = int(ans)
        print("ランダムに選ばれた数字5桁を当ててください\n当てると2ポイントゲットできます")
        while True:
            seikai = 0
            matigai = 0
            print("数字5桁を入力してください")
            p_anser = inp()
            if len(str(p_anser)) >= 6:
                print("不正な入力値です")
            elif len(str(p_anser)) <= 4:
                print("不正な入力値です")
            elif p_anser == npc_ans:
                glo_point += 2
                print(f"正解!!正解は{npc_ans}でした!!\n2ポイントゲット\n現在のポイントは{glo_point}")
                break
            elif p_anser != npc_ans:
                print("不正解")
                anser_list.append(p_anser)
                anser_num = p_anser
                # 1桁目
                p_anser1 = anser_num%10
                anser_num//=10
                # 2桁目
                p_anser10 = anser_num%10
                anser_num//=10
                # 3桁目
                p_anser100=anser_num%10
                ans_num = npc_ans
                # 4桁目
                p_anser1000 = anser_num%10
                anser_num//=10
                # 5桁目
                p_anser10000 = anser_num%10
                anser_num//=10
                # 1桁目
                npc_ans1 = ans_num%10
                ans_num//=10
                # 1桁目
                npc_ans10 = ans_num%10
                ans_num//=10
                # 3桁目
                npc_ans100=ans_num%10
                ans_num = npc_ans
                # 4桁目
                npc_ans1000 = ans_num%10
                anser_num//=10
                # 5桁目
                npc_ans10000 = anser_num%10
                anser_num//=10
                if p_anser1 ==npc_ans1:
                    seikai += 1
                if p_anser10 == npc_ans10:
                    seikai += 1
                if p_anser100 == npc_ans100:
                    seikai += 1
                if p_anser1000 == npc_ans1000:
                    seikai += 1
                if p_anser10000 == npc_ans10000:
                    seikai += 1
                print(f"5桁のうち{seikai}個正解です。")
                print(f"現在の回答{anser_list}")
        

        

    
    


# HIT&BLOW main処理
    def main():
        anser_list = []
        npc_list = []
        global glo_point
        data = strat()
        while True:
            print(f"現在のポイント{glo_point}")
            print("難易度を選択してください。\n普通 : 1 | 難しい(挑戦には5point必要) : 2")
            nan = inp()
            if nan == 1:
                npc_nomal()
                hantei()
            elif nan == 2:
                    if glo_point >= 5:
                        npc_hard()
                        hard()
                    else:
                        print("ポイントが足りません")
                        continue
            else:
                print("不正な入力値です")
                continue
            print("セーブして終了 : 1 | セーブせず終了 : 2 | コンテニュー : 3 ")
            end = inp()
            if end == 1:
                with open(f"{data}.txt" , "w" , encoding="UTF-8") as w_file:
                    w_file.write(str(glo_point))
                    print("セーブが完了しました\n終了します")
                    break
            elif end == 2:
                print("終了します")
                break
            elif end == 3:
                continue
            else:
                print("不正な入力値です")
    main()




# ox game 対人 or CPU
def ox_game():
    with open("taizin.txt", "w", encoding="UTF-8") as read_file:
        read_file.truncate(0)
    with open("cpu.txt", "w", encoding="UTF-8") as read1_file:
        read1_file.truncate(0)
        taizin = 0
        cpu = 0
    while True:
        print("モードを選んでください >> 1: 対人 1VS1 | 2: VS CPU | 3: 終了")
        mode = inp()
        if mode == 1:
            taizin += 1
            game1()
        elif mode == 2:
            cpu += 1
            ox_game2()
        elif mode == 3:
            with open("taizin.txt", "r", encoding="UTF-8") as read_file:
                file1 = read_file.read()
            print(f"対人戦の対戦回数は{taizin}回。\n結果は\n{file1.strip()}")
            with open("cpu.txt", "r", encoding="UTF-8") as read1_file:
                file = read1_file.read()
            print(f"CPU戦の対戦回数は{cpu}回。\n結果は\n{file.strip()}")
            print("メインメニューに戻ります")
            break
        else:
            print("不正な入力値です")
            continue

    


def ox_game2():
    
        # 表示関数
        def disp():
            for i in hyo:
                print(i)

        hyo =[
            ["1" ,"2" ,"3"],
            ["4" ,"5" ,"6"],
            ["7" ,"8" ,"9"],
        ]

        def random1():
                num = rd.randint(1,2)
                return num

        list1 = [0, 0, 0]
        list2 = [0, 0, 0]
        list3 = [0, 0, 0]
        list =[list1, list2, list3]

        # player1
        def p1():
            try:
                count = 0
                nyu = inp()
                if 0 >= nyu or nyu >= 10:
                    print("不正な入力値です")
                    p1()
                for hidari in range(3):
                    for migi in range(3):
                        count += 1
                        if nyu == count:
                            if list[hidari][migi] ==10 or list[hidari][migi] == 100:
                                print("使用済み")
                                p1()
                            else:
                                hyo[hidari][migi]=("〇")
                                list[hidari][migi] = 100
            except ValueError:
                print("不正な入力値です")
                p1()
        # NPC
        def npc():
            try:
                count = 0
                nyu = rd.randint(1,9)
                for hidari in range(3):
                    for migi in range(3):
                        count += 1
                        if nyu == count:
                            if list[hidari][migi] ==10 or list[hidari][migi] == 100:
                                npc()
                            else:
                                print(f"NPCは{nyu}を選びました。")
                                hyo[hidari][migi]=("×")
                                list[hidari][migi] = 10
            except ValueError:
                print("不正な入力値です")
                npc()

        def farst(num):
            print("〇×ゲームをはじめます")
            if num == 1:
                disp()
                print("player1が先行です")
                zyunban = 0
                zyunban += 1
                p1()
                disp()
            elif num == 2:
                disp()
                print("NPCが先行です")
                npc()
                disp()
        # メイン処理
        def main():
            finish =False
            zyunban = 0
            zyunban = random1()
            farst(zyunban)
            counter = 0
            ans = 0
            while True:
                counter += 1
                zyunban += 1
                if zyunban % 2 == 1:
                    print("プレイヤーのターンです")
                    p1()
                elif zyunban % 2 == 0:
                    print("NPCのターンです")
                    npc()
                disp()
                for tate in range(3): 
                    ans = 0 
                    ans2 = 0
                    if finish == True:
                        break
                    for yoko in range(3):
                        ans += list[tate][yoko]
                        ans2 += list[yoko][tate]
                        if ans ==30 or ans2 ==30 or ans ==300 or ans2== 300:
                            finish = True
                            break
                ans = 0
                for i in range(3):
                    ans += list[i][i]
                if ans == 30 or ans == 300:
                    break
                ans = 0
                if  list[0][2]+list[1][1]+list[2][0]==30 or list[0][2]+list[1][1]+list[2][0]==300:
                    break
                if finish == True:
                    break
                elif counter == 8:
                    counter = 100
                    break
            global glo
            glo += 1
            if counter == 100:
                print("引き分け")
                with open("cpu.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{glo}回目:引き分け\n")
            elif zyunban % 2 == 1:    
                print("player1の勝ち")
                with open("cpu.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{glo}回目:player1の勝ち\n")
            elif zyunban % 2 ==0:
                print("NPCの勝ち")
                with open("cpu.txt", "a", encoding="UTF-8") as r_file:
                    r_file.write(f"{glo}回目:NPCの勝ち\n")

        main()
        
 


    
# 対人戦
def game1():
    count = 0
    counter = 0
    list1 = [1, 2, 3]
    list2 = [4, 5 ,6]
    list3 = [7, 8, 9]
    list=[list1,list2,list3]
# player1処理
    def p1():
        print("1~9を入力してください")
        nyu = inp()
        if 0 >= nyu or nyu >= 10:
            print("不正な入力値です")
            p1()
        elif nyu == 1:
            if list[0][0] == "×":
                print("使用済み")
                p1()
            else:
                list[0][0]=str("〇")
        elif nyu == 2:
            if list[0][1] == "×":
                print("使用済み")
                p1()
            else:
                list[0][1]=str("〇")
        elif nyu == 3:
            if list[0][2] == "×":
                print("使用済み")
                p1()
            else:
                list[0][2]=str("〇")
        elif nyu == 4:
            if list[1][0] == "×":
                print("使用済み")
                p1()
            else:
                list[1][0]=str("〇")
        elif nyu == 5:
            if list[1][1] == "×":
                print("使用済み")
                p1()
            else:
                list[1][1]=str("〇")
        elif nyu == 6:
            if list[1][2] == "×":
                print("使用済み")
                p1()
            else:
                list[1][2]=str("〇")
        elif nyu == 7:
            if list[2][0] == "×":
                print("使用済み")
                p1()
            else:
                list[2][0]=str("〇")
        elif nyu == 8:
            if list[2][1] == "×":
                print("使用済み")
                p1()
            else:
                list[2][1]=str("〇")
        elif nyu == 9:
            if list[2][2] == "×":
                print("使用済み")
                p1()
            else:
                list[2][2]=str("〇")

# player2処理
    def p2():
        print("1~9を入力してください")
        nyu = inp()
        if 0 >= nyu or nyu >= 10:
            print("不正な入力値です") 
            p2()
        elif nyu == 1:
            if list[0][0] == "〇":
                print("使用済み")
                p2()
            else:
                list[0][0]=str("×")
        elif nyu == 2:
            if list[0][1] == "〇":
                print("使用済み")
                p2()
            else:
                list[0][1]=str("×")
        elif nyu == 3:
            if list[0][2] == "〇":
                print("使用済み")
                p2()
            else:
                list[0][2]=str("×")
        elif nyu == 4:
            if list[1][0] == "〇":
                print("使用済み")
                p2()
            else:
                list[1][0]=str("×")
        elif nyu == 5:
            if list[1][1] == "〇":
                print("使用済み")
                p2()
            else:
                list[1][1]=str("×")
        elif nyu == 6:
            if list[1][2] == "〇":
                print("使用済み")
                p2()
            else:
                list[1][2]=str("×")
        elif nyu == 7:
            if list[2][0] == "〇":
                print("使用済み")
                p2()
            else:
                list[2][0]=str("×")
        elif nyu == 8:
            if list[2][1] == "〇":
                print("使用済み")
                p2()
            else:
                list[2][1]=str("×")
        elif nyu == 9:
            if list[2][2] == "〇":
                print("使用済み")
                p2()
            else:
                list[2][2]=str("×")
    def random1():
        num = rd.randint(1,2)
        return num
# 先行決め
    def farst(num):
        print("〇×ゲームをはじめます")
        if num == 1:
            print("player1が先行です")
            for i  in range(len(list)):
                 print(list[i])
            p1()
            for i  in range(len(list)):
                 print(list[i])
            return num
        elif num == 2:
            print("player2が先行です")
            for i  in range(len(list)):
                 print(list[i])
            count = 1
            p2()
            for i  in range(len(list)):
                print(list[i])
            return num
# 対人main処理
    def main():
        try:
            count = random1()
            counter = 0
            farst(count)
            while True:
                count += 1
                counter += 1
                if list[0][0] =="〇" and list[0][1] =="〇" and list[0][2] =="〇"or list[0][0] =="×" and list[0][1] =="×" and list[0][2] =="×":
                    break # yoko
                elif list[1][0] =="〇" and list[1][1] =="〇" and list[1][2] =="〇"or list[1][0] =="×" and list[1][1] =="×" and list[1][2] =="×":

                    break # yoko
                elif list[2][0] =="〇" and list[2][1] =="〇" and list[2][2] =="〇"or list[2][0] =="×" and list[2][1] =="×" and list[2][2] =="×":

                    break # yoko
                elif list[0][0] =="〇" and list[1][0] =="〇" and list[2][0] =="〇"or list[0][0] =="×" and list[1][0] =="×" and list[2][0] =="×":

                    break # tate
                elif list[0][2] =="〇" and list[1][2] =="〇" and list[2][2] =="〇"or list[0][2] =="×" and list[1][2] =="×" and list[2][2] =="×":

                    break # tate
                elif list[0][1] =="〇" and list[1][1] =="〇" and list[2][1] =="〇"or list[0][1] =="×" and list[1][1] =="×" and list[2][1] =="×":

                    break # tate
                elif list[0][0] =="〇" and list[1][1] =="〇" and list[2][2] =="〇"or list[0][0] =="×" and list[1][1] =="×" and list[2][2] =="×":

                    break
                elif list[0][2] =="〇" and list[1][1] =="〇" and list[2][0] =="〇"or list[0][2] =="×" and list[1][1] =="×" and list[2][0] =="×":

                    break
                if counter == 9:
                    counter = 100
                    break
                elif count % 2 == 1:
                    print("プレイヤー1のターンです")
                    p1() 
                elif count % 2 == 0:
                    print("プレイヤー2のターンです")
                    p2()
                for i  in range(len(list)):
                    print(list[i])
            global glo1
            glo1 += 1
            if counter == 100:
                print("引き分け")
                with open("taizin.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{glo1}回目:引き分け\n")
            elif count % 2 == 0:    
                print("player1の勝ち")
                with open("taizin.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{glo1}回目:player1の勝ち\n")
            elif count % 2 ==1:
                print("player2の勝ち")
                with open("taizin.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{glo1}回目:player2の勝ち\n")
        except:
            print("エラーが発生しました。モード選択に戻ります。")
            ox_game()
    main()
    
# 明日の運勢
def unsei():
    num = rd.randint(1,4)
    num2 = rd.randint(1,4)
    unsei1(num)
    cloer(num2)
def unsei1(num):
    if num == 1:
        print("明日の運勢 :絶好調")
    elif num == 2:
        print("明日の運勢 :好調")  
    elif num == 3:
        print("明日の運勢 :不調")  
    elif num == 4:
        print("明日の運勢 :絶不調")
def cloer(num2):
    if num2 == 1:
          print("明日のラッキーカラーは黒")
    elif num2 == 2:
          print("明日のラッキーカラーは白")
    elif num2 == 3:
          print("明日のラッキーカラーは青")
    elif num2 == 4:
          print("明日のラッキーカラーは赤")
     

# 現在時刻
def zikoku():
    while True:
        print("確認したい場所の現在時刻を表示します\n1:日本 | 2:アメリカ | 3:終了")
        num = inp()
        if num == 1:
            zikoku1()
        elif num == 2:
            zikoku2()
        elif num == 3:
            print("メインメニューに戻ります")
            break
        else:
            print("不正な入力値です")
            continue
def zikoku1():
    print(f"日本の現在時刻は{dt.datetime.now().day}日{dt.datetime.now().hour}時です")
def zikoku2():
    if dt.datetime.now().hour < 14:
        day = dt.datetime.now().day - 1
        hozon = dt.datetime.now().hour
        hour = dt.datetime.now().hour - dt.datetime.now().hour +24
        hour = hour - (14 -hozon)
    else:
        day = dt.datetime.now().day
        hour =dt.datetime.now().hour - 14
    print(f"アメリカの現在時刻は{day}日{hour}時です")

# 電卓
def seisaku1():
    while True:
        print("電卓の機能から1つ選んでください\n1:足し算 | 2:引き算 | 3:掛け算 | 4:割り算 | 5:平方根\n6:乗算 | 7:階乗 | 8:最小公倍数 | 9:最大公約数 | 10:終了")   
        num =inp()
        if num == 1:
            kei1()
        elif num == 2:
            kei2()
        elif num == 3:
            kei3()
        elif num == 4:
            kei4()
        elif num == 5:
            kei5()
        elif num == 6:
            kei6()
        elif num == 7:
            kei7()
        elif num == 8:
            kei8()
        elif num == 9:
            kei9()
        elif num == 10:
            print("メインメニューに戻ります")
            break
        else:
            print("不正な入力値です")
            continue
def kei1():
    print("1つ目の整数を入力してください:")
    num1 = inp()
    print("2つ目の整数を入力してください:")
    num2 = inp()
    print(f"{num1}+{num2}={num1+num2}")
def kei2():
    print("1つ目の整数を入力してください:")
    num1 = inp()
    print("2つ目の整数を入力してください:")
    num2 = inp()
    print(f"{num1}-{num2}={num1-num2}")
def kei3():
    print("1つ目の整数を入力してください:")
    num1 = inp()
    print("2つ目の整数を入力してください:")
    num2 = inp()
    print(f"{num1}×{num2}={num1*num2}")
def kei4():
    try:
        print("1つ目の整数を入力してください:")
        num1 = inp()
        print("2つ目の整数を入力してください:")
        num2 = inp()
        print(f"{num1}÷{num2}={num1/num2}")
    except ZeroDivisionError:
        print("0により除算は実行できません。")
def kei5():
    print("1つ目の整数を入力してください:")
    num1 = inp()
    print(f"{num1}の平方根は{math.sqrt(num1)}です")
def kei6():
    print("1つ目の整数を入力してください:")
    num1 = inp()
    print("2つ目の整数を入力してください:")
    num2 = inp()
    print(f"{num1}と{num2}の乗算は{math.pow(num1 ,num2)}です")
def kei7():
    print("1つ目の整数を入力してください:")
    num1 = inp()
    print(f"{num1}の階乗は{math.pow(num1 ,2)}です")
def kei8():
    print("1つ目の整数を入力してください:")
    num1 = inp()
    print("2つ目の整数を入力してください:")
    num2 = inp()
    print(f"{num1}と{num2}の最小公倍数は{math.lcm(num1, num2)}です")
def kei9():
    print("1つ目の整数を入力してください:")
    num1 = inp()
    print("2つ目の整数を入力してください:")
    num2 = inp()
    print(f"{num1}と{num2}の最大公約数は{math.gcd(num1 ,num2)}です")


# メインメニュー
def mainmenyu():
    while True:
        print("メインメニュー1: 電卓 | 2:現在時刻時刻 | 3: 明日の運勢 | 4: ox game(対人 or cpu) | 5: HIT&BLOW | 6: 終了")
        num =inp()
        if num == 1:
            seisaku1()
        elif num == 2:
            zikoku()
        elif num == 3:
            unsei()
        elif num == 4:
            ox_game()
        elif num == 5:
            hitblow()
        elif num == 6:
            print("終了します")
            break
        else:
            print("不正な入力値です")
            continue

mainmenyu()

