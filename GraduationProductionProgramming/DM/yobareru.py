from flask import Flask, Blueprint,render_template,redirect,url_for,request

def test():
    print('Hello World')

if __name__ == '__main__':
    test()

print('モジュール名: {}'.format(__name__))


#DMはBlueprintをいれる必要なし
#呼ばれる関数を記述する
#最終的にはreturnでController側に返すのも忘れずに

    #DBの照合を行うif分の作成
