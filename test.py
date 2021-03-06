"""
Run Test.
"""
import BatchReader as dataset
import os
import time
from CaptchaModel import Captcha

# load model
model = Captcha()
model.load_checkpoint('crack_capcha0.990800004005.model-9200')

# load dataset
dataset = dataset.BatchReader(ratio=0.01, test_size=1000)
images, labels = dataset.get_val_batch(0, 1000)

count = len(labels)
correct = 0

# start timing
start = time.time()
t = start
log_file = open('results.txt','a')
# start testing
for i in range(count):
    image = images[i]
    label = labels[i]
    pred = model.predict(image)
    text = ''.join(map(str, pred))
    if text == label:
        correct += 1
    else:
        # print(label, text)
        pass
    if i % 50 == 0:
        t = time.time() - t
        print('[%d/%d] average: %f'%(i, count, t / 50))
        t = time.time()
    log_file.write(text+' '+label+'\n')
end = time.time()

# output result
print('Total time: %f s'%(end - start))
print('Average time: %f s'%((end - start) / count))
print('Total: %d, Correct: %d, Acc: %f'%(count, correct, float(correct) / float(count)))
