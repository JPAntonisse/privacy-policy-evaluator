from typing import Dict, Any, Union

import numpy as np
from privacy_policy_evaluator import helpers, preprocessing, wordscoring


def group(paragraphs, topics, threshold=0.1):
    # Preprocces the topics
    topics = [preprocessing.lemmatization(topic).strip() for topic in topics]

    # compute TFIDF for all paragraphs and topics
    [vecs, tfidf] = helpers.calculate_vectors(paragraphs + topics)

    # Extract feature indices
    feature_names = tfidf.get_feature_names()
    topic_feature_indices = []
    for i in range(len(topics)):
        feature_index = vecs[-(i + 1), :].indices[0]
        topic_feature_indices.append(feature_index)

    # Find matches
    topic_to_paragraph_dict = {}
    for i in range(0, len(paragraphs)):
        for feature_index in topic_feature_indices:
            score = vecs[i, feature_index]
            topic_name = feature_names[feature_index]
            if score >= threshold:
                if topic_name in topic_to_paragraph_dict:
                    topic_to_paragraph_dict[topic_name].append(i)
                else:
                    topic_to_paragraph_dict[topic_name] = [i]

    # merge paragrahs
    topic_to_text_dict = {}
    for topic_name, paragraph_indexes in topic_to_paragraph_dict.items():
        paragraphs = np.array(paragraphs)
        topic_to_text_dict[topic_name] = " ".join(list(paragraphs[paragraph_indexes]))

    return topic_to_text_dict


def evaluate(topic_paragraphs: dict):
    score: Dict = {}
    for key, value in topic_paragraphs.items():
        score[key] = wordscoring.score_text(value)
    return score