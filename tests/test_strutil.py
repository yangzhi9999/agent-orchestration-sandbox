import importlib.util
import pathlib
import unittest


def loadStrutil():
    root = pathlib.Path(__file__).resolve().parent.parent
    path = root / "src" / "synth" / "strutil.py"
    spec = importlib.util.spec_from_file_location("strutil", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SlugifyTests(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.strutil = loadStrutil()

  def testHelloWorld(self):
    self.assertEqual(self.strutil.slugify("Hello World"), "hello-world")

  def testPunctuation(self):
    self.assertEqual(
        self.strutil.slugify("Punctuation, here!"), "punctuation-here")

  def testOnlyPunctuation(self):
    self.assertEqual(self.strutil.slugify("!!!"), "")

  def testNumbers(self):
    self.assertEqual(self.strutil.slugify("Room 101"), "room-101")

  def testLeadingTrailingHyphens(self):
    self.assertEqual(self.strutil.slugify("  --foo--  "), "foo")

  def testMultipleSpaces(self):
    self.assertEqual(self.strutil.slugify("a   b"), "a-b")

  def testEmptyString(self):
    self.assertEqual(self.strutil.slugify(""), "")

  def testAlreadySlug(self):
    self.assertEqual(self.strutil.slugify("hello-world"), "hello-world")


if __name__ == "__main__":
  unittest.main()
