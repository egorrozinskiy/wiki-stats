
import sys
import math
import collections
import array

import statistics

from matplotlib import rc
"""
rc('font', family='Droid Sans', weight='normal', size=14)
"""
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


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
        return len(self._links[self._offset[_id]:self._offset[_id+1]])

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]

    def get_id(self, title):
        for i in range(len(self._titles)):
            if self._titles[i] == title:
                return(i)

    def get_number_of_pages(self):
        return len(self._titles)

    def is_redirect(self, _id):
        return self._redirect[_id]

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes(_id)


    def get_count_redirection(self):
        return sum(self._redirect)



    def get_minimum_links_count(self):
        m = self._offset[1] - self._offset[0]
        for i in range(self._n):
            k = self._offset[i+1] - self._offset[i]
            m = min(k,m)
        return m


    def get_count_articles_with_min_links(self):
        s = 0
        t = self.get_minimum_links_count()
        for i in range(self._n):
            k = self._offset[i+1] - self._offset[i]
            if k == t:
                s += 1
        return s



    def get_maximum_links_count(self):
        m = self._offset[1] - self._offset[0]
        for i in range(self._n):
            k = self._offset[i + 1] - self._offset[i]
            m = max(k, m)
        return m




    def get_count_articles_with_max_links(self):
        s = 0
        t = self.get_maximum_links_count()
        for i in range(self._n):
            k = self._offset[i+1] - self._offset[i]
            if k == t:
                s += 1
        return s



    def article_with_max_links(self):
        m = self.get_maximum_links_count()
        for i in range(self._n):
            k = self._offset[i + 1] - self._offset[i]
            if k == m:
                return self._titles[i]



    def middle_count_links_in_article(self):
        countlinks_from = list(map(self.get_number_of_links_from, range(self.get_number_of_pages())))
        return statistics.mean(countlinks_from), statistics.stdev(countlinks_from)

    def min_count_links_to_article(self):
        countlinks_to = [0 for i in range(self.get_number_of_pages())]
        for i in range(self.get_number_of_pages()):
            for x in self.get_links_from(i):
                countlinks_to[x] += 1
                if self.is_redirect(i) == 1:
                    countlinks_to[x] -=1
        _mini = min(countlinks_to)
        return _mini
    def count_articles_with_min_links_count(self):
        countlinks_to = [0 for i in range(self.get_number_of_pages())]
        for i in range(self.get_number_of_pages()):
            for x in self.get_links_from(i):
                countlinks_to[x] += 1
                if self.is_redirect(i) == 1:
                    countlinks_to[x] -=1
        _mini = min(countlinks_to)
        num_of_links_with_min = sum(x == _mini for x in countlinks_to)
        return num_of_links_with_min

    def max_count_links_to_article(self):
        countlinks_to = [0 for i in range(self.get_number_of_pages())]
        for i in range(self.get_number_of_pages()):
            for x in self.get_links_from(i):
                countlinks_to[x] += 1
                if self.is_redirect(i) == 1:
                    countlinks_to[x] -=1
        _maxi = max(countlinks_to)
        return _maxi

    def count_articles_with_max_links_count(self):
        countlinks_to = [0 for i in range(self.get_number_of_pages())]
        for i in range(self.get_number_of_pages()):
            for x in self.get_links_from(i):
                countlinks_to[x] += 1
                if self.is_redirect(i) == 1:
                    countlinks_to[x] -=1
        _maxi = max(countlinks_to)
        num_of_links_with_max = sum(x == _maxi for x in countlinks_to)
        return num_of_links_with_max


    def article_with_max_links_count(self):
        index = 0
        counter = collections.defaultdict(int)
        for i in range(self._n):
            l = self._links[self._offset[i]:self._offset[i + 1]]
            if not self._redirect[i]:
                for i in l:
                    counter[i] += 1
        maxi = counter[0]
        for i in counter.keys():
            if counter[i] > maxi:
                maxi = counter[i]
                index = i
        return self.get_title(index)

    def middle_count_link_to_article(self):
        count_links_to = [0 for i in range(self.get_number_of_pages())]
        for i in range(self.get_number_of_pages()):
            for x in self.get_links_from(i):
                count_links_to[x] += 1
                if self.is_redirect == 1:
                    count_links_to[x] -= 1
        _maxi = max(count_links_to)
        return statistics.mean(count_links_to)

    def min_count_redirect_to_article(self):
        counter = collections.defaultdict(int)
        for i in range(self._n):
            l = self._links[self._offset[i]:self._offset[i + 1]]
            if self._redirect[i]:
                for i in l:
                    counter[i] += 1
        mini = counter[0]
        for i in counter.keys():
            if counter[i] < mini:
                mini = counter[i]
        return mini
        print('минимальное количество перенаправлений на статью', mini)



    def count_articles_with_min_redirects_count(self):
        redirects_to = [0 for i in range(self.get_number_of_pages())]
        for i in range(self.get_number_of_pages()):
            for x in self.get_links_from(i):
                if self.is_redirect(i) == 1:
                    redirects_to[x] += 1
        _mini = min(redirects_to)
        pages_with_min_redir = sum(x == _mini for x in redirects_to)
        return pages_with_min_redir


    def max_count_redirects_to_article(self):
        counter = collections.defaultdict(int)
        for i in range(self._n):
            l = self._links[self._offset[i]:self._offset[i + 1]]
            if self._redirect[i]:
                for i in l:
                    counter[i] += 1
        maxi = counter[0]
        for i in counter.keys():
            if counter[i] > maxi:
                maxi = counter[i]
        return maxi
        print('максимальное количество перенаправлений на статью', maxi)



    def count_articles_with_max_redirects_count(self):
        k = 0
        counter = collections.defaultdict(int)
        for i in range(self._n):
            l = self._links[self._offset[i]:self._offset[i + 1]]
            if self._redirect[i]:
                for i in l:
                    counter[i] += 1
        maxi = counter[0]
        for i in counter.keys():
            if counter[i] > maxi:
                mini = counter[i]
        for i in counter.keys():
            if maxi == counter[i]:
                k += 1
        return k
        print('количество статей с максимальным количеством перенаправлений', k)


    def article_with_max_redirects_count(self):
        index = 0
        counter = collections.defaultdict(int)
        for i in range(self._n):
            l = self._links[self._offset[i]:self._offset[i + 1]]
            if self._redirect[i]:
                for i in l:
                    counter[i] += 1
        maxi = counter[0]
        for i in counter.keys():
            if counter[i] > maxi:
                maxi = counter[i]
                index = i
        return self.get_title(index)
        print('статья с наибольшим количеством перенаправлений', self.get_title(index))



    def middle_count_redirects_to_article(self):
        redirects_to = [0 for i in range(self.get_number_of_pages())]
        for i in range(self.get_number_of_pages()):
            for x in self.get_links_from(i):
                if self.is_redirect(i) == 1:
                    redirects_to[x] += 1
        return statistics.mean(redirects_to)


    


if __name__ == '__main__':
    wg = WikiGraph()
    wg.load_from_file('wiki_small.txt')
    print(wg.get_count_redirection())
    print(wg.get_minimum_links_count())
    print(wg.get_count_articles_with_min_links())
    print(wg.get_maximum_links_count())
    print(wg.get_count_articles_with_max_links())
    print(wg.article_with_max_links())
    print(wg.middle_count_links_in_article())
    print(wg.min_count_links_to_article())
    print(wg.count_articles_with_min_links_count())
    print(wg.max_count_links_to_article())
    print(wg.count_articles_with_max_links_count())
    print(wg.article_with_max_links_count())
    print(wg.middle_count_link_to_article())
    print(wg.min_count_redirect_to_article())
    print(wg.count_articles_with_min_redirects_count())
    print(wg.max_count_redirects_to_article())
    print(wg.count_articles_with_max_redirects_count())
    print(wg.article_with_max_redirects_count())
    print(wg.middle_count_redirects_to_article())
  









