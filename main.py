import sys
from bisect import bisect_left

def input_parser(args):
    try:
        l1,l2,l3,l4,enemy_hp=map(float,args[1].split(" "))
    except ValueError:
        l1 = float(args[1])
        l2 = float(args[2])
        l3 = float(args[3])
        l4 = float(args[4])
        enemy_hp = float(args[5])
    except IndexError:
        print("一撃目のダメージ（乱数1）を入力してください：",end="")
        l1 = float(input().strip())
        print("二撃目のダメージ（乱数1）を入力してください：",end="")
        l2 = float(input().strip())
        print("三撃目のダメージ（乱数1）を入力してください：",end="")
        l3 = float(input().strip())
        print("四撃目のダメージ（乱数1）を入力してください：",end="")
        l4 = float(input().strip())
        print("敵のHPを入力してください：",end="")
        enemy_hp = float(input().strip())
        print("=====入力完了=====")
    return (l1,l2,l3,l4,enemy_hp)


def calc_prob(args):
    l1, l2, l3, l4, enemy_hp = input_parser(args)
    rand = [0.9+0.001*i for i in range(200)]
    print("入力された内容：")
    print("　一撃目のダメージ（乱数1）：{:.4f}".format(l1))
    print("　二撃目のダメージ（乱数1）：{:.4f}".format(l2))
    print("　三撃目のダメージ（乱数1）：{:.4f}".format(l3))
    print("　四撃目のダメージ（乱数1）：{:.4f}".format(l4))
    print("　敵のHP　　　　　　　　：{:.4f}".format(enemy_hp))
    first = []
    
    second = []
    for x in rand:
        for y in rand:
            first.append(l1*x+l2*y)
    for x in rand:
        for y in rand:
            second.append(l3*x+l4*y)
    first.sort()
    second.sort()
    ret = 0
    for x in first:
        j = 40000 - bisect_left(second,enemy_hp-x)
        ret += j/40000
    return ret/40000


if __name__=='__main__':
    print("撃破率：{:.2f}％".format(calc_prob(sys.argv)*100))