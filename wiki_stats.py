#!/usr/bin/python3

import os
import sys
import math
import collections
import array
 
import statistics
 
from matplotlib import rc
 
 
rc('font', family='Droid Sans', weight='normal', size=14)
 
import matplotlib.pyplot as plt
 
 
class WikiGraph:
 
    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)
 
        with open(filename, encoding="utf-8") as f:
            (n, _nlinks) = (0, 0) # TODO: прочитать из файла
           
            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))
 
            n, _nlinks = f.readline().split()
            n, _nlinks = int(n), int(_nlinks)
 
            self._n = n
            self._links = _nlinks
 
            for i in range(n):
                self._titles.append(f.readline())
                size, flag, n0 = (i for i in map(int, f.readline().split()))
                self._sizes.append(size)
                self._redirect.append(flag)
                for j in range(n0):
                    self._links.append(int(f.readline()))
                self._offset.append(n0 + self._offset[-1])
 
 
 
        print('Граф загружен')
 
    def get_number_of_links_from(self, _id):
        return self._offset[_id+1] - self._offset[id]
 
    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]
 
    def get_id(self, title):
        for i,j in enumerate(self._titles):
            if j == title:
                return i
 
    def get_number_of_pages(self):
        return self._n
 
    def is_redirect(self, _id):
        return self._redirect[_id]
 
    def get_title(self, _id):
        return self._titles[_id]
 
    def get_page_size(self, _id):
        return self._sizes[_id]
 
    #Количество статей с перенаправлением
    def get_count_redirection(self):
        return sum(self._redirect)
 
    #Минимальное количество ссылок из статьи
    def get_minimum_links_count(self):
        m = self._offset[1] - self._offset[0]
        for i in range(self._n):
            k = self._offset[i+1] - self._offset[i]
            m = min(k,m)
        return m
    #количество статей с минимальным количеством ссылок
    def get_count_articles_with_min_links(self):
        s = 0
        t = self.get_minimum_links_count(self)
        for i in range(self.n):
            k = self._offset[i+1] - self._offset[i]
            if k == t:
                s += 1
        return s
 
    #максимальное количество ссылок из статьи
    def get_maximum_links_count(self):
        m = self._offset[1] - self._offset[0]
        for i in range(self._n):
            k = self._offset[i + 1] - self._offset[i]
            m = max(k, m)
        return m
 
    #количество статей с максимальным количеством ссылок
    def get_count_articles_with_max_links(self):
        s = 0
        t = self.get_maximum_links_count(self)
        for i in range(self._n):
            k = self._offset[i+1] - self._offset[i]
            if k == t:
                s += 1
        return s
 
    #статья с наибольшим количеством ссылок
    def article_with_max_links(self):
        m = self.get_maximum_links_count(self)
        for i in range(self._n):
            k = self._offset[i + 1] - self._offset[i]
            if k == m:
                return self._titles[i]
 
    #среднее количество ссылок в статье
    def middle_count_links_in_article(self):
        lst = []
        for i in range(self._n):
            lst.append(self._offset[i+1] - self._offset[i])
        return statistics.mean(lst)
 
    #минимальное количество ссылок на статью
    # (перенаправление не считается внешней ссылкой)
    def min_count_links_to_article(self):
        counter = collections.defaultdict(int)
        for i in range(self._n):
            l = self._links[self._offset[i]:self._offset[i+1]]
            if not self._redirect[i]:
                for i in l:
                    counter[l] += 1
        mini = counter[0]
        for i in counter.keys():
            if counter[i] < mini:
                mini = counter[i]
        return mini
 
    #количество статей с минимальным количеством внешних ссылок
    def count_articles_with_min_links_count(self):
        k = 0
        counter = collections.defaultdict(int)
        for i in range(self._n):
            l = self._links[self._offset[i]:self._offset[i + 1]]
            if not self._redirect[i]:
                for i in l:
                    counter[l] += 1
        mini = counter[0]
        for i in counter.keys():
            if counter[i] < mini:
                mini = counter[i]
        for i in counter.keys():
            if mini == counter[i]:
                k += 1
        return k
 
    # максимальное количество ссылок на статью
    # (перенаправление не считается внешней ссылкой)
    def max_count_links_to_article(self):
        counter = collections.defaultdict(int)
        for i in range(self._n):
            l = self._links[self._offset[i]:self._offset[i + 1]]
            if not self._redirect[i]:
                for i in l:
                    counter[l] += 1
        maxi = counter[0]
        for i in counter.keys():
            if counter[i] > maxi:
                maxi = counter[i]
        return maxi
 
    # количество статей с максимальным количеством внешних ссылок
    def count_articles_with_max_links_count(self):
        k = 0
        counter = collections.defaultdict(int)
        for i in range(self._n):
            l = self._links[self._offset[i]:self._offset[i + 1]]
            if not self._redirect[i]:
                for i in l:
                    counter[l] += 1
        maxi = counter[0]
        for i in counter.keys():
            if counter[i] > maxi:
                mini = counter[i]
        for i in counter.keys():
            if maxi == counter[i]:
                k += 1
        return k
 
   
 
 
 
 
 
def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл
 
 
if __name__ == '__main__':
 
    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)
 
    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)
 
    # TODO: статистика и гистограммы
