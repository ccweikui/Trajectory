# /usr/bin/python
# -*- coding=utf8 -*-
# 这是整个项目的配置文件, 配置主要包括以下类型:
# 1.输入输出文件
# 2.固定的参数

# 文件所在的根目录
BASE_DIR = "/Users/weikui/File/source/pyFile/Trajectory/TrajectoryPython/"
# 原始的输入文件
ORIGIN_FILE = BASE_DIR + "data/cdr_ler_20100916.TXT"
# 原始的坐标文件
WEIBIAO_FILE = BASE_DIR + "data/weibiao.txt"
# 原始的坐标文件
WEIBIAO_FILE_NEW = BASE_DIR + "data/weibiao_new.txt"
# 原始的Label文件
LABEL_FILE = BASE_DIR + "data/label.txt"
# 站点分布统计的输出文件
LOCATION_STAT = BASE_DIR + "output/location_stat.txt"
# 经纬度按照名称聚类后的文件
LOCATION_CLUSTER = BASE_DIR + "output/location_cluster.txt"
# 将站点按相应的label转换之后的输出文件
LOCATION_LABEL = BASE_DIR + "output/location_label.txt"
# 将打过label之后的轨迹数据按用户进行合并并去重之后输出的文件
RECORD_SORTED_USER = BASE_DIR + "output/record_sorted_user.txt"
# 将按照用户合并过的数据文件输出成用户的轨迹
USER_TRAJECTORY = BASE_DIR + "output/user_trajectory.txt"
# 按照特定要求对生成的轨迹进行过滤输出的文件
FILTER_TRAJETORY = BASE_DIR + "output/filter_trajectory.txt"
