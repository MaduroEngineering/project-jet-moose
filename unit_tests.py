import service
import unittest
import json

class TestService(unittest.TestCase):
  """
  Test the add function from the mymath library
  """

  def test_handler(self):
      """
      Test that the addition of two integers returns the correct total
      """
      result = service.handler
      self.assertEqual(result, 5.8580000000000005)

with open('event.json') as json_data:
  eventFile = json.load(json_data)

if __name__ == '__main__':
    unittest.main(eventFile)
