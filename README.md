# 常在型作業効率化ソフト HyperPrompt

by Gokiburian 2024/07/05 (2020/03/20)

## 1. 概要

これは私が高校生の頃に作ったソフトの一つである．

機能としてはpygameを利用したキー入力にコマンド実行を紐付けるだけである．例えばEを押せば好きなフォルダを開き，Cを押せば特定のソフトを起動するなどができる．
シンプルながらbatファイルを組み合わせることで複雑な操作を単純化でき，私の作成したソフトの中ではぶっちぎりでお世話になっている．

プログラムの改良することで，特定の数列に反応するようにしたり，時間差実行したりなども可能．これは最低限の実装のみだが，ぜひ自分好みにカスタマイズしてほしい．

## 2. インストール方法

`__hyperprompt.py`の他，python環境とpygameが必要である．pythonがインストールされていれば，
```bash
pip install pygame
```
を実行すればよい．

## 3. 使用方法

これをそのままクリックするだけで起動することができるが，スタートアップに設定しておくとなお便利である．
フォーカスされていない状態ではほとんど計算していないはずなので，一度起動させたら放置でダイジョブ．

このウィンドウがフォーカスされている状態でキー入力を行うとソースコード6行目のKEY_DICTに従ってコマンドが実行される．

続く`BACK_COLOR`, `TEXT_COLOR`, `FONT_SIZE`, `WIDTH`, `HEIGHT`の値を操作すれば見た目も変えられる．
デフォルトでは操作時にSEがなるようになっているが，`PLAY_SOUND`をFalseにすれば鳴らなくなる．



## 4. アンインストール方法

`__hyperprompt.py`はファイルの生成はしない．これを消すことで完全に元の状態に戻る．

## 5. バグの発見、意見、その他

`moto.allergyholder@gmail.com` にメールをください
