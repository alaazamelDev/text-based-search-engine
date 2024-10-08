from dotenv import load_dotenv

from matchers.embedding.antique_embedding_matcher import AntiqueEmbeddingMatcher
from matchers.tf_idf.antique_matcher import AntiqueMatcher
from text_processors.antique_text_processor import AntiqueTextProcessor

# Load environment variables from .env file
load_dotenv()

matcher: AntiqueEmbeddingMatcher = AntiqueEmbeddingMatcher()
# matcher: AntiqueMatcher = AntiqueMatcher()
query: str = input("Enter a query: ")
result = matcher.match(query)
for match in result:
    print(match.get('doc_content'))
    print(match.get('similarity'))
# from datetime import datetime
#
# from text_processors.antique_text_processor import AntiqueTextProcessor
#
processor = AntiqueTextProcessor()
print(processor.process(query))
# start = datetime.now()
# print(processor.process(
#     """I would be very surprise if the senator will be reelected. This should have being his/her job to “shout” as
#     hard as she could and then a bit more- she is the communicator to all federal issues and she failed miserably.
#     The senator should have called to all the near by cities/states and ask for rescue buses, call the army/national
#     guard to have an thousand of transport aircraft to be able to take as much people as possible to near by states.
#     . . No doubt, FEMA has a lot to be blame too, but I think that locally that was the senator job to manage and to
#     raise all the red flags."""))
# print(datetime.now().__sub__(start))
