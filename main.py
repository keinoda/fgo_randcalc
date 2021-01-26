import sys
from bisect import bisect_left

def input_parser(args):
    try:
        # Wandboxのように引数をまとめた形式
        l1,s1,l2,s2,l3,s3,l4,s4,enemy_hp=map(float,args[1].split(" "))
        enemy_hp = int(enemy_hp)
    except ValueError:
        # 引数に列挙した形式
        l1 = float(args[1])
        s1 = float(args[2])
        l2 = float(args[3])
        s2 = float(args[4])
        l3 = float(args[5])
        s3 = float(args[6])
        l4 = float(args[7])
        s4 = float(args[8])
        enemy_hp = int(args[9])
    except IndexError:
        # 標準入力形式
        print("1枚目のダメージ（乱数1）を入力してください：",end="")
        l1 = float(input().strip())
        print("1枚目の固定ダメージを入力してください：",end="")
        s1 = float(input().strip())
        print("2枚目のダメージ（乱数1）を入力してください：",end="")
        l2 = float(input().strip())
        print("2枚目の固定ダメージを入力してください：",end="")
        s2 = float(input().strip())
        print("3枚目のダメージ（乱数1）を入力してください：",end="")
        l3 = float(input().strip())
        print("3枚目の固定ダメージを入力してください：",end="")
        s3 = float(input().strip())
        print("4枚目のダメージ（乱数1）を入力してください：",end="")
        l4 = float(input().strip())
        print("4枚目の固定ダメージを入力してください：",end="")
        s4 = float(input().strip())
        print("敵のHPを入力してください：",end="")
        enemy_hp = int(input().strip())
        print("=======入力完了=======")
    return (l1,s1,l2,s2,l3,s3,l4,s4,enemy_hp)


def calc_damage(l1,s1,l2,s2,l3,s3,l4,s4,rand):
    return int((l1-s1)*rand+s1)+int((l2-s2)*rand+s2)+int((l3-s3)*rand+s3)+int((l4-s4)*rand+s4)


def calc_prob(args):
    l1,s1, l2,s2, l3,s3, l4,s4, enemy_hp = input_parser(args)
    rand = [0.9+0.001*i for i in range(200)]
    print("入力された内容：")
    print("　1枚目のダメージ（乱数1）：{:.4f}，固定ダメージ：{:.1f}".format(l1,s1))
    print("　2枚目のダメージ（乱数1）：{:.4f}，固定ダメージ：{:.1f}".format(l2,s2))
    print("　3枚目のダメージ（乱数1）：{:.4f}，固定ダメージ：{:.1f}".format(l3,s3))
    print("　4枚目のダメージ（乱数1）：{:.4f}，固定ダメージ：{:.1f}".format(l4,s4))
    print("　敵のHP：{}".format(enemy_hp))
    first = []
    print("最低ダメージ：{}　最高ダメージ：{}".format(calc_damage(l1,s1,l2,s2,l3,s3,l4,s4,0.9),calc_damage(l1,s1,l2,s2,l3,s3,l4,s4,1.099)))
    second = []
    for x in rand:
        for y in rand:
            first.append(calc_damage(l1,s1,0,0,0,0,0,0,x)+calc_damage(0,0,l2,s2,0,0,0,0,y))
    for x in rand:
        for y in rand:
            second.append(calc_damage(0,0,0,0,l3,s3,0,0,x)+calc_damage(0,0,0,0,0,0,l4,s4,y))
    first.sort()
    second.sort()
    ret = 0
    for x in first:
        j = len(second) - bisect_left(second,enemy_hp-x)
        ret += j/len(second)
    return ret/len(first)


if __name__=='__main__':
    print("撃破率：{:.2f}％".format(calc_prob(sys.argv)*100))
