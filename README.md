# 通用数据一键分析工具

一个用 Python 写的通用数据分析小工具：喂给它任意一个 CSV/Excel 数据文件，再告诉它"要分析哪一列"，它就能一键输出统计、相关性、分档汇总和一张总览图。

## 功能

- 读取 CSV 或 Excel 文件（自动按后缀识别）
- 一键统计：所有数值列的平均/最高/最低/…（`describe`）
- 相关性分析：所有数值列两两相关系数
- 分档汇总：把某列（如温度）分档，看每档的目标列平均
- 输出一张 2×2 总览大图（散点/分档柱状/直方图/逐样本）
- 用 `input()` 让你指定文件路径和分析的目标列，无需改代码

## 怎么用

1. `pip install pandas matplotlib openpyxl`
2. 运行：`python data_analyzer.py`
3. 按提示输入：文件路径 + 要分析的目标列名
   - 例如用 `yield_data.csv` 时，输入目标列 `收率`
4. 终端打印统计/相关/分档，并生成 `data_overview.png`

## 示例

运行后按提示输入：

```text
请输入要分析的 CSV 文件路径：C:/Users/biyun/Desktop/yield_data.csv
数据里哪一列是要分析的目标：收率
```

## 技术栈

Python · pandas · matplotlib · openpyxl

## 许可

MIT License

## 作者

fantasy801