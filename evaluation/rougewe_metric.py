from summ_eval.rouge_we_metric import RougeWeMetric
from .summeval_metric import SummEvalMetric
import nltk

class RougeWe(SummEvalMetric):
    metric_name = 'rougeWE'
    range = (0, 1)
    higher_is_better = True
    low_resource = False

    def __init__(self):
        nltk.download('stopwords')
        se_metric = RougeWeMetric()
        super(RougeWe, self).__init__(se_metric)

    def evaluate(self,
                 inputs,
                 targets,
                 keys = ['rouge_we_3_f']):
        #TODO zhangir: update when dataset api is merged.
        return super(RougeWe, self).evaluate(inputs, targets, keys)