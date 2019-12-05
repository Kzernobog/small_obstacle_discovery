class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'pascal':
            return '/path/to/datasets/VOCdevkit/VOC2012/'  # folder that contains VOCdevkit/.
        elif dataset == 'sbd':
            return '/path/to/datasets/benchmark_RELEASE/'  # folder that contains dataset/.
        elif dataset == 'cityscapes':
            return '/path/to/datasets/cityscapes/'     # foler that contains leftImg8bit/
        elif dataset == 'coco':
            return '/path/to/datasets/coco/'
        elif dataset == 'small_obstacle':
            return '/scratch/ash/data_run/downtown_data_run/'
        elif dataset == 'lnf':
            return '/scratch/adityaRRC/small_obstacle_dataset/'
        elif dataset == 'iiitds':
            return '/scratch/ash/IIIT_Labels'
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError
