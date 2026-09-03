import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']   # 让中文正常显示（防方框乱码）
plt.rcParams['axes.unicode_minus'] = False              # 让负号正常显示


def read_data(path):
    if path.endswith(".csv"):
        return pd.read_csv(path, encoding="utf-8")
    elif path.endswith(".xlsx") or path.endswith(".xls"):
        return pd.read_excel(path)
    else:
        print("暂不支持的文件格式，请用 .csv 或 .xlsx")
        return None
def summarize(df):
    print(df.describe())                      # 一键统计所有数值列
    print("总能耗:", df["能耗"].sum())
def correlate(df):
    print(df.corr(numeric_only=True))

def groupby_temp(df, goal_col):
    bins = [60, 75, 85, 100]
    labels = ["低温", "中温", "高温"]
    df["温度档"] = pd.cut(df["温度"], bins=bins, labels=labels)
    avg = df.groupby("温度档")[goal_col].mean()
    print(avg)
def make_plot(df, goal_col):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    # 左上：温度 vs 目标列 散点
    axes[0, 0].scatter(df["温度"], df[goal_col])
    axes[0, 0].set_title("温度 vs " + goal_col)
    axes[0, 0].set_xlabel("温度 (°C)")
    axes[0, 0].set_ylabel(goal_col)

    # 右上：各档平均目标值 柱状
    avg = df.groupby("温度档")[goal_col].mean()
    axes[0, 1].bar(avg.index, avg.values)
    axes[0, 1].set_title("各档平均" + goal_col)
    axes[0, 1].set_xlabel("档位")
    axes[0, 1].set_ylabel("平均" + goal_col)

    # 左下：目标值分布 直方图
    axes[1, 0].hist(df[goal_col])
    axes[1, 0].set_title(goal_col + "分布")
    axes[1, 0].set_xlabel(goal_col)
    axes[1, 0].set_ylabel("频数")

    # 右下：每个样本的目标值（用行号当横轴，通用、不依赖"批次"列）
    axes[1, 1].bar(df.index, df[goal_col])
    axes[1, 1].set_title("每样本" + goal_col)
    axes[1, 1].set_xlabel("样本序号")
    axes[1, 1].set_ylabel(goal_col)

    fig.suptitle("数据一键分析总览")
    fig.tight_layout()
    fig.savefig("data_overview.png")
    print("已生成 data_overview.png")


def main():
    path = input("请输入要分析的 CSV 文件路径（完整路径，例如 C:/Users/biyun/Desktop/yield_data.csv）：\n")
    df = read_data(path)
    goal_col = input("数据里哪一列是要分析的目标（例如 收率 / 吸收率）？：")
    summarize(df)
    correlate(df)
    groupby_temp(df, goal_col)
    print("读到的前几行：")
    print(df.head())
    make_plot(df, goal_col)

main()