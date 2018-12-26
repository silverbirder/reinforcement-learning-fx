# -*- coding: utf-8 -*-
import gym
import numpy as np

# 目標とする報酬
goal_average_steps = 195
# エピソードのタイムステップの最大の長さ
max_number_of_steps = 200
# エピソード数
num_episodes = 5000
# 保存しておく連続したエピソードの数
num_consecutive_iterations = 100
# 最後のエピソードの報酬
last_time_steps = np.zeros(num_consecutive_iterations)

def bins(clip_min, clip_max, num):
    """
    ヒストグラム-ビン
    """
    return np.linspace(clip_min, clip_max, num + 1)[1:-1]

def digitize_state(observation):
    """
    デジタイズ: observationを離散値に変換する
    """
    # 各値を4個の離散値に変換
    #
    # cart_pos: カートの位置 (-2.4 ~ 2.4)
    # cart_v: カートの速度 (-inf ~ inf) ※よく分からない
    # pole_angle: ポールの角度 (-41.8度 ~ 41.8度)
    # pole_v: ポールの速度 (-inf ~ inf) ※よく分からない
    cart_pos, cart_v, pole_angle, pole_v = observation
    digitized = [np.digitize(cart_pos, bins=bins(-2.4, 2.4, 4)),
                 np.digitize(cart_v, bins=bins(-3.0, 3.0, 4)),
                 np.digitize(pole_angle, bins=bins(-0.5, 0.5, 4)),
                 np.digitize(pole_v, bins=bins(-2.0, 2.0, 4))]
    # 0~255に変換
    return sum([x * (4 ** i) for i, x in enumerate(digitized)])

def get_action(state, action, observation, reward, episode):
    """
    行動の選択を行う
    """
    next_state = digitize_state(observation)

    # e-greedy
    # epsilon = 0.2 # 一定の確率でランダムに次の行動を選択する
    epsilon = 0.5 * (0.99 ** episode) # 学習が進むにつれて経験を利用する
    if epsilon <= np.random.uniform(0, 1):
        # 経験
        next_action = np.argmax(q_table[next_state])
    else:
        # 探索
        next_action = np.random.choice([0, 1])

    # Q-learning: 学習係数
    alpha = 0.2
    # Q-learning: 割引報酬和の為の割引率
    #             時間が経つほど報酬は少なくなる？
    gamma = 0.99
    # Qテーブルの更新
    q_table[state, action] = (1 - alpha) * q_table[state, action] +\
            alpha * (reward + gamma * q_table[next_state, next_action])

    return next_action, next_state

if __name__ == '__main__':
    env = gym.make('CartPole-v0')

    # Qテーブル
    q_table = np.random.uniform(low=-1, high=1, size=(4 ** 4, env.action_space.n))

    for episode in range(num_episodes):
        # 環境の初期化
        observation = env.reset()

        # 状態
        state = digitize_state(observation)
        action = np.argmax(q_table[state])

        episode_reward = 0
        for t in range(max_number_of_steps):
            # CartPoleの描画
            env.render()

            # ランダムで行動の選択
            # action = np.random.choice([0, 1])

            # 行動の実行とフィードバックの取得
            #
            # observation: 環境固有のオブジェクト
            # reward: 前のアクションによって獲得された報酬
            # done: 処理が終了した場合に True
            # info: デバック用に診断情報
            observation, reward, done, info = env.step(action)

            # 罰則の追加
            if done:
                reward = -200

            # 行動の選択
            action, state = get_action(state, action, observation, reward, episode)

            episode_reward += reward

            if done:
                print('%d Episode finished after %f time steps / mean %f' % (episode, t + 1,
                    last_time_steps.mean()))

                # 最後のエピソードの報酬を保存する
                # last_time_steps = np.hstack((last_time_steps[1:], [episode_reward]))
                last_time_steps = np.hstack((last_time_steps[1:], [t + 1]))
                break

        if (last_time_steps.mean() >= goal_average_steps): # 直近の100エピソードが195以上であれば成功
            print('Episode %d train agent successfuly!' % episode)
            break
