"""Keep a source-reviewed pre-code concept out of product rankings."""
import unittest
import build_data

class ReviewedConceptTests(unittest.TestCase):
    def test_rektor_is_not_ranked_even_if_search_returns_it(self):
        self.assertFalse(build_data.is_rag({'full_name': 'codediodeio/rektor-db',
            'name': 'rektor-db', 'description': 'Rektor Vector Database', 'topics': ['vector-database']}))
    def test_unrelated_vector_tool_stays_eligible(self):
        self.assertTrue(build_data.is_rag({'full_name': 'fixture/vector-engine',
            'name': 'engine', 'description': 'A vector database', 'topics': ['vector-database']}))
