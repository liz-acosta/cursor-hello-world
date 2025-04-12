import unittest
import os
import tempfile
import json
from app import app, get_db_connection
from init_db import init_db

class PokedexTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.db_fd, self.db_path = tempfile.mkstemp()
        app.config['DATABASE'] = self.db_path
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            init_db()

    def tearDown(self):
        """Clean up after tests"""
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_index_page(self):
        """Test the index page loads correctly"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Pokemon List', response.data)

    def test_pokemon_profile(self):
        """Test pokemon profile page"""
        # Test with a valid pokemon ID
        response = self.app.get('/pokemon/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bulbasaur', response.data)

    def test_pikachu_special_case(self):
        """Test the special case for Pikachu"""
        response = self.app.get('/pokemon/25')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Team Rocket has captured Pikachu', response.data)
        self.assertIn(b'\xe2\x9d\x8c', response.data)  # UTF-8 encoded ❌

    def test_database_operations(self):
        """Test database operations"""
        with app.app_context():
            db = get_db_connection()
            cursor = db.cursor()

            # Test pokemon count
            cursor.execute('SELECT COUNT(*) FROM pokemon')
            count = cursor.fetchone()[0]
            self.assertGreater(count, 0)

            # Test pokemon data
            cursor.execute('SELECT * FROM pokemon WHERE id = 1')
            pokemon = cursor.fetchone()
            self.assertIsNotNone(pokemon)
            self.assertEqual(pokemon[1], 'Bulbasaur')  # name
            self.assertIsNotNone(pokemon[2])  # description
            self.assertIsNotNone(pokemon[3])  # image_url

    def test_api_endpoints(self):
        """Test API endpoints"""
        # Test get_pokemon endpoint
        response = self.app.get('/api/pokemon/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Bulbasaur')
        self.assertIn('description', data)
        self.assertIn('image_url', data)

        # Test get_all_pokemon endpoint
        response = self.app.get('/api/pokemon')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main() 