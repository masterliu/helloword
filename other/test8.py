# -*- coding: UTF-8 -*-
import unittest

from mydict import Dicta

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dicta(a=1,b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d = Dicta()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dicta()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dicta()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dicta()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        print ('setup')

    def tearDown(self):
        print ('teardown')

    if __name__ == '__main__':
        unittest.main()
