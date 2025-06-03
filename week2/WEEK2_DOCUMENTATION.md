# Documentation for Week2 Challenges
### Author: Mimo Shirasaka

## Challenge 1
最も良いプログラム：hash_table4.py（再ハッシュと collision対策入りの hash table）<br>
その他プログラム：hash_table.py（ベーシックな hash table）, hash_table3.py（再ハッシュ入りの hash table）<br>

* 以下の説明は hash_table4.pyについて書きます。
1. Delete()関数の実装
    1. マップ内の探す箱（bucket）の住所を算出：
        削除したい単語`key`に対し、ハッシュ値を計算。次にマップの長さ`bucket_size`で modをとる。
    2. 探す箱の中に`key`と一致する単語（アイテム）があるかを探す：

        - 見つかったら<br>
            -> 1つ前のマス`prev`が指すポインタ`prev.next`を、今いるマス`item`ではなく、今いる次のマス`item.next`を指すようにすることで今いるマスを実質的に削除(delete)する<br>
            -> `return True`<br>
        - 見つからなかったら<br>
            -> 次を確認<br>
        - 最後まで見つからなかったら<br>
            -> `return False`<br>
2. 再ハッシュの実装<br>
    1. 再ハッシュの条件をつける：<br>
        要素数がテーブルサイズの 70% を上回ったら、テーブルサイズを 2 倍に拡張、要素数がテーブルサイズの 30% を下回ったら、テーブルサイズを半分に縮小<br>
    2. ハッシュテーブルを resize する：<br>
        新しいテーブル`new_buckets`を resize するサイズで用意し、元のテーブルを参照。bucketごとに見ていき、連結リストで繋がれた各アイテムについて`new_buckets`用の住所を算出する。
        各アイテムについて`Item()`を用いてリフォオーマットし、新しいテーブルに格納する。<br>
    3. 再ハッシュ済みの新しいテーブル`new_buckets`を、現在のテーブル`self.buckets`として定義する。<br>

3. Collision 対策<br>
    サンプルコードにおけるハッシュ値算出の課題は、AliceとElicaなど、文字の組み合わせが同じものが存在する時に、bucket住所が同じになり、衝突(collision) が発生する、というものであった。
    サンプルコードでは、名前に含まれる文字のASCIIコードの和をハッシュ値として計算しており、文字の登場順番が考慮されていなかった。
    そこで、Collision対策として、文字の登場順番を考慮したハッシュ値を算出すればより計算効率が速くなるのではないかと考えた。
    実装としては、最初の文字を`i=0`番目として、`(i + 1) * \<文字のASCIIコード\>` の和をハッシュ値とすることにより順番が違うと違う bucket住所になるようにした。






