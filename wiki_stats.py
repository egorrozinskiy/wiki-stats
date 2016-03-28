#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            s = list(map(int, f.readline().split()))
            (n, _nlinks) = (s[0], s[1]) # TODO: прочитать из файла
            self._pages = n
            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))

            for i in range(n):
                s=f.readline()
                s = s.rstrip()
                self._titles.append(s)
                s=list(map(int, f.readline().split()))
                self._sizes[i] = s[0]
                self._redirect[i] = s[1]
                for k in range(s[2]):
                    self._links[k] = int(f.readline())
                if i==0:
                    self._offset[i]=0
                else:
                    self._offset[i] = s[2]+self._offset[i-1]


        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return len(self._links[self._offset[_id]:self._offset[_id+1]])

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]

    def get_id(self, title):
        for i in range(len(self._titles)):
            if self._titles[i] == title:
                return(i)

    def get_number_of_pages(self):
        return self._pages


    def is_redirect(self, _id):
        return self._redirect[_id]

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]

    def analysis(self):
        number_of_redirects = 0
        for i in range(self.pages):
            if self._redirect(i):
                number_of_redirects += 1
        print(number_of_redirects)

        number_of_links_from = list(map(G.get_number_of_links_from, range(G.get_number_of_pages())))
        maximum_num_of_links = max(number_of_links_from)
        minimum_num_of_links = min(number_of_links_from)
        num_of_pages_with_min_num_of_links = sum(minimum_num_of_links for x in number_of_links_from)
        num_of_pages_with_max_num_of_links = sum(maximum_num_of_links for x in number_of_links_from)
        print('Minimum number of links from page:', minimum_num_of_links)
        print('Pages with minimum number of links:', num_of_pages_with_min_num_of_links)
        print('Maximum number of links from page:', num_of_pages_with_min_num_of_links)
        print('Pages with maximum number of links:', num_of_pages_with_max_num_of_links)
        print('Page with maximum number of links:', G.get_title(i))
        






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
