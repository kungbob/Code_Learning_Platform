
from tool.analyser import analyser
from tool.tree import flatten, get_empty_version_tree, flatten_self_define
from sklearn.decomposition import PCA
import numpy as np # linear algebra
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn import mixture
from matplotlib.colors import LogNorm
from sklearn import svm
import matplotlib.font_manager
from sklearn.cluster import KMeans, MeanShift, estimate_bandwidth

from version.models import Version


def clustering(data_matrix):

	scaler = StandardScaler().fit(data_matrix)
	standardized_data = scaler.transform(data_matrix)

	if len(data_matrix) > 100:
		bandwidth = estimate_bandwidth(standardized_data, quantile=0.5, n_samples = 100)
	else:
		bandwidth = estimate_bandwidth(standardized_data, quantile=0.5)

	ms = MeanShift(bandwidth=bandwidth, bin_seeding=True).fit(standardized_data)

	other_list = ["maxIfDepth", "maxLoopDepth", "maxArraySize", "maxArrayDim"]

	label = ms.labels_
	center = ms.cluster_centers_
	cluster_no = len(np.unique(label))

	data_count = []
	data_list = []
	for i in range(0, cluster_no):
		data_count.append(0)
		data_list.append([])


	for i in range(0,len(data_matrix)):
		data_list[label[i]].append(data_matrix[i])
		data_count[label[i]] += 1

	skilltree_structure = list(flatten_self_define(get_empty_version_tree()).keys())
	cluster_list = []
	data_length = len(data_matrix[0])

	for cluster in range(0, cluster_no):

		skilltree = []

		for i in range(0, data_length):
			skilltree.append(0)

		necessary_skill = []
		redundant_skill = []
		other_count = []

		for i in other_list:
			other_count.append([])

		for data in data_list[cluster]:
			for i in range(0, data_length):
				if data[i] > 0:
					skilltree[i] += 1

			for skill in [data_length-4,data_length-3,data_length-2,data_length-1]:
				other_count[skill - data_length + 4].append(data[skill])

		for i in range(0, data_length):
			if skilltree[i] >= data_count[cluster]*0.65 and skilltree_structure[i] not in other_list:
				necessary_skill.append(skilltree_structure[i])
			elif skilltree[i] <= data_count[cluster]*0.1 and skilltree_structure[i] not in other_list:
				redundant_skill.append(skilltree_structure[i])

		other_skill = []


		for i in range(0, len(other_list)):
			mode = max(set(other_count[i]), key=other_count[i].count)
			other_skill.append({"name": other_list[i], "mode": mode})

		cluster_list.append({"center": center[cluster], "data_count": data_count[cluster], "necessary_skill": necessary_skill,
			"redundant_skill": redundant_skill, "other_skill": other_skill, "character_skill": ""})


	common_feature = cluster_list[0]["necessary_skill"]
	for cluster in cluster_list:
		common_feature = list(set(cluster["necessary_skill"]).intersection(common_feature))

	for cluster in cluster_list:
		character_skill = list(cluster["necessary_skill"])
		for common in common_feature:
			character_skill.remove(common)
		cluster["character_skill"] = character_skill

	output = {"cluster_list": cluster_list, "label": label, "common_skill": common_feature}

	return output
