Step 1:
	将原始数据按照聚类进行符号化
	python location_label/locationlabeled.py

Step 2:
	将符号化后的轨迹按照用户进行排序
	python construct_trajectory/sortedbyuser.py

Step 3: 
	根据用户数据形成轨迹
	python construct_trajectory/formattrajectory.py

Step 4:
	对用户轨迹按照一定的要求进行过滤
	python construct_trajectory/filtertrajectory.py
