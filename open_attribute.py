import h5py


read_path = '/media/blade/road_hackers/training_attribute/137.h5'

results_object = h5py.File(read_path, 'r')

results_array = results_object['attrs']

for i in range(10):
    print(results_array[i])

print(len(results_object))

results_object.close()
