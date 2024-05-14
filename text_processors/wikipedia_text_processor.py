from typing import List
from overrides import overrides
from text_processors.base_text_processor import BaseTextProcessor


class WikipediaTextProcessor(BaseTextProcessor):

    @overrides
    def process(self, text) -> List[str]:
        text = text.lower()
        tokens = self._word_tokenizer(text)
        tokens = self._remove_stopwords(tokens)
        tokens = self._remove_punctuations(tokens)
        tokens = self._remove_whitespaces(tokens)
        processed_text = self._lemmatize(tokens)


        # print("First 10 processed tokens:")
        # print(processed_text[:10])

        return processed_text
