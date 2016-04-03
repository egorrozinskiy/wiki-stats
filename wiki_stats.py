#!/usr/bin/python3

import os
import sys
import math
import collections
import array

import statistics




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


    def get_count_redirection(self):
        return sum(self._redirect)
        print('Количество статей с перенаправлением', sum(self._redirect))


    def get_minimum_links_count(self):
        m = self._offset[1] - self._offset[0]
        for i in range(self._n):
            k = self._offset[i+1] - self._offset[i]
            m = min(k,m)
        return m
        print('Минимальное количество ссылок из статьи', )

    def get_count_articles_with_min_links(self):
        s = 0
        t = self.get_minimum_links_count(self)
        for i in range(self.n):
            k = self._offset[i+1] - self._offset[i]
            if k == t:
                s += 1
        return s
        print('количество статей с минимальным количеством ссылок', s)


    def get_maximum_links_count(self):
        m = self._offset[1] - self._offset[0]
        for i in range(self._n):
            k = self._offset[i + 1] - self._offset[i]
            m = max(k, m)
        return m
        print('максимальное количество ссылок из статьи', m)



    def get_count_articles_with_max_links(self):
        s = 0
        t = self.get_maximum_links_count(self)
        for i in range(self._n):
            k = self._offset[i+1] - self._offset[i]
            if k == t:
                s += 1
        return s
        print('количество статей с максимальным количеством ссылок', s)


    def article_with_max_links(self):
        m = self.get_maximum_links_count(self)
        for i in range(self._n):
            k = self._offset[i + 1] - self._offset[i]
            if k == m:
                return self._titles[i]
                print('статья с наибольшим количеством ссылок', self._titles[i])


    def middle_count_links_in_article(self):
        lst = []
        for i in range(self._n):
            lst.append(self._offset[i+1] - self._offset[i])
        return statistics.mean(lst)
        print('среднее количество ссылок в статье', statistics.mean(lst))


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
        print('минимальное количество ссылок на статью', mini)

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
        print('количество статей с минимальным количеством внешних ссылок', k)


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
        print('максимальное количество ссылок на статью', maxi)


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
        print('количество статей с максимальным количеством внешних ссылок', k)


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
        print('статья с наибольшим количеством внешних ссылок', self.get_title(index))

    def middle_count_link_to_article(self):
        index = 0
        counter = collections.defaultdict(int)
        for i in range(self._n):
            l = self._links[self._offset[i]:self._offset[i + 1]]
            if not self._redirect[i]:
                for i in l:
                    counter[i] += 1
        return statistics.mean(counter.values())
        print('среднее количество внешних ссылок на статью', statistics.mean(counter.values()))


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
        k = 0
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
        for i in counter.keys():
            if mini == counter[i]:
                k += 1
        return k
        print('количество статей с минимальным количеством перенаправлений', k)



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
        index = 0
        counter = collections.defaultdict(int)
        for i in range(self._n):
            l = self._links[self._offset[i]:self._offset[i + 1]]
            if self._redirect[i]:
                for i in l:
                    counter[i] += 1
        return statistics.mean(counter.values())
        print('среднее количество перенаправлений на статью', statistics.mean(counter.values()))

    #поиск пути от а до б
    def bfs(self, a,b):
        p = collections.defaultdict(int)
        id = self.get_id(a)
        queue = [id]
        while queue:
            if queue[0] == self.get_id(b):
                kef = None
                res = [b]
                while kef == self.get_id(a):
                    kef = p[kef]
                    res.append(self.get_title(kef))
                res.append(a)
                res.reverse()
                return res
            else:
                childrens = self._links[self._offset[queue[0]]:self._offset[queue[0]+1]]
                for i in childrens:
                    p[i] = queue[0]
                del(queue[0])
                queue.extend(childrens)
        return False






def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()


    # TODO: нарисовать гистограмму и сохранить в файл



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



    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
        print (wg.bfs("Python", "Список файловых систем"))

    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    # TODO: статистика и гистограммы
