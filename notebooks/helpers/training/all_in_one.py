from memory_profiler import memory_usage
import time
from helpers.utils.common_utils import format_time

def getallparams(li):
    params = 0
    for module in li:
        for param in module.parameters():
            params += param.numel()
    return params


def all_in_one_train(trainprocess, trainmodules):
    starttime = time.time()
    train_losses, valid_losses = trainprocess()
    # mem = max(memory_usage(proc=trainprocess))
    endtime = time.time()

    print("Training Time: "+format_time(endtime-starttime))
    # print("Training Peak Mem: "+str(mem))
    print("Training Params: "+str(getallparams(trainmodules)))
    return train_losses, valid_losses

def all_in_one_test(testprocess, testmodules):
    teststart = time.time()
    testprocess()
    testend = time.time()
    print("Inference Time: "+format_time(testend-teststart))
    print("Inference Params: "+str(getallparams(testmodules)))
