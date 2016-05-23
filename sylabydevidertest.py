import unittest

from sylabledivider import SyllableDivider
class TestStringMethods(unittest.TestCase):

  def test_sylaby_correct1(self):
      zmienna = "ala ma kota a kot ma ale"
      self.assertEqual(SyllableDivider(zmienna).divide(),['a', 'la', 'ma', 'ko', 'ta', 'a', 'kot', 'ma', 'a', 'le'])

  def test_sylaby_correct2(self):
      zmienna = "radosny"
      self.assertEqual(SyllableDivider(zmienna).divide(),['ra', 'dos', 'ny'])

  def test_sylaby_correct3(self):
      zmienna = "chłopców"
      self.assertEqual(SyllableDivider(zmienna).divide(),['chłop', 'ców'])

  def test_sylaby_correct4(self):
      zmienna = "portfel"
      self.assertEqual(SyllableDivider(zmienna).divide(),['por', 'tfel'])

  def test_sylaby_correct5(self):
      zmienna = "element struktury aktu komunikacyjnego"
      self.assertEqual(SyllableDivider(zmienna).divide(),['e','le','ment','struk','tu','ry','ak','tu','ko','mu','ni','ka','cyj','ne','go'])

  def test_sylaby_correct6(self):
      zmienna = "od północy polska"
      self.assertEqual(SyllableDivider(zmienna).divide(),['od', 'pół', 'no','cy', 'pol','ska'])

  def test_sylaby_correct7(self):
      zmienna = "jednym z elementów"
      self.assertEqual(SyllableDivider(zmienna).divide(),['jed','nym','z','e','le','men','tów'])

  def test_sylaby_correct7(self):
      zmienna = "czy istnieje obowiązująca kogoś"
      self.assertEqual(SyllableDivider(zmienna).divide(),['czy', 'is','tnie','je' ,'o','bo','wią','zu','ją','ca', 'ko','goś'])

  def test_sylaby_correct8(self):
      zmienna = "wysokomineralizowana"
      self.assertEqual(SyllableDivider(zmienna).divide(),['wy', 'so','ko','mi' ,'ne','ra','li','zo','wa','na'])


if __name__ == '__main__':
    unittest.main()