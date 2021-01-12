# robosys_ros

入力した数字を素数かどうか判定し合成数の場合素因数分解して出力します.

# 動作環境

- Ubuntu 20.04 LTS
- ROS Noetic

# 使用したもの

- Raspberry Pi 4 Model B

# デモ動画のリンク

# インストール方法

以下のコマンドを入力してください.

```
cd ~/catkin_ws/src
git clone https://github.com/HoshinoMasafumi/robosys_ros.git
cd ..
catkin_make
source ~/.bashrc
```

# 使用方法

まず以下のコマンドを入力してください.
```
cd ~/catkin_ws/src/robosys_ros/scripts
chmod +x imput.py
chmod +x prime_number.py
```

次に,端末を3つ開きそれぞれの端末で以下のコマンドを入力してください.

1つ目

```
roscore
```

2つ目

```
rosrun robosys_ros imput.py
```

3つ目

```
rosrun robosys_ros prime_number.py
```

2つ目の端末に数字を入力すると,3つ目の端末に結果が出力されます.

# ライセンス

[BSD 3-Clause "New" or "Revised" License](https://github.com/HoshinoMasafumi/robosys_ros/blob/master/LICENSE)
